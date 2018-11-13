# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class QsCrawlerBookKinds(scrapy.Item):
    kind_id=scrapy.Field()
    kind_name=scrapy.Field()
    def get_name(self):
        return QsCrawlerBookKinds.__name__

class QsCrawlerBookLists(scrapy.Item):
    book_id=scrapy.Field()
    img_url = scrapy.Field()
    book_name = scrapy.Field()
    author_name = scrapy.Field()
    book_intro=scrapy.Field()
    kind_id=scrapy.Field()
    def get_name(self):
        return QsCrawlerBookLists.__name__
class QsCrawlerBooksDetails(scrapy.Item):
    srction_book=scrapy.Field()
    book_detail=scrapy.Field()
    book_id=scrapy.Field()
    def get_name(self):
        return QsCrawlerBooksDetails.__name__