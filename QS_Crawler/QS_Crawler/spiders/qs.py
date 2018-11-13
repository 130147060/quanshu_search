# -*- coding: utf-8 -*-
import logging
import re
import scrapy
from selenium import webdriver

from items import QsCrawlerBookKinds, QsCrawlerBookLists, QsCrawlerBooksDetails


class QsSpider(scrapy.Spider):
    name = 'qs'
    allowed_domains = ['www.quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/']
    def start_requests(self):
        for url in self.start_urls:
            r=scrapy.Request(url=url,meta={'type':'first_page'},callback=self.parse_first)
            yield r

    def parse_first(self, response):
        self.log(f"start to parse url:{response.url}", level=logging.WARNING)
        book_kinds=response.xpath("//nav/ul/li")
        for book_kind in book_kinds:
            kind_name=book_kind.xpath("./a/text()").extract_first()
            kind_url=book_kind.xpath("./a/@href").extract_first()
            kind_id = int(re.search(r'\d+', kind_url).group())
            r=scrapy.Request(url=kind_url,callback=self.parse_main)
            item=QsCrawlerBookKinds(
                kind_id=kind_id,
                kind_name=kind_name
            )
            yield item
            yield r

    def parse_main(self, response):
        url=response.url
        kind_id = int(re.search(r'\d+', url).group())
        books_main=response.xpath('//div/section/ul/li')[0:30]
        for book_main in books_main:
            detail_url=book_main.xpath("./span/a[@class='clearfix stitle']/@href").extract_first()
            r=scrapy.Request(url=detail_url,meta={'kind_id':kind_id},callback=self.parse_detail)
            yield r

    def parse_detail(self,response):
        self.log(f"start to parse url:{response.url}", level=logging.WARNING)
        url=response.url
        book_id = int(re.search(r'\d+', url).group())
        kind_id=response.meta['kind_id']
        main_xpth=response.xpath("//div[@class='detail']")
        img_url=main_xpth.xpath("./a/img/@src").extract_first()
        book_name=main_xpth.xpath("./a/img/@alt").extract_first()
        author_name=main_xpth.xpath("./div[@class='author'][2]/div[@class='bookDetail']/dl[@class='bookso'][1]/dd/text()").extract_first()
        book_intro=main_xpth.xpath("./div[@class='b-info']/div[@class='infoDetail']/div[@id='waa']/text()").extract_first()
        detail_url=main_xpth.xpath("./div[@class='b-info']/div[@class='b-oper']/a[@class='reader']/@href").extract_first()
        r = scrapy.Request(url=detail_url, meta={'type': 'srction_details'}, callback=self.parse_srction, dont_filter=True)
        item = QsCrawlerBookLists(
            book_id=book_id,
            img_url=img_url,
            book_name=book_name,
            author_name=author_name,
            book_intro=book_intro,
            kind_id=kind_id,
        )
        yield r
        yield item

    def parse_srction(self, response):
        self.log(f"start to parse url:{response.url}", level=logging.WARNING)
        srction_lists=response.xpath("//div[@class='chapterNum']/ul/div/li")[0:6]
        url = response.url
        book_id = int(re.search(r'\d+.$', url).group())
        for srction_list in srction_lists:
            srction_book=srction_list.xpath("./a/@title").extract_first()
            book_detail=srction_list.xpath("./a/@href").extract_first()
            item=QsCrawlerBooksDetails(
                srction_book=srction_book,
                book_detail = book_detail,
                book_id = book_id
            )
            yield item

