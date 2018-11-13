# -*- coding: utf-8 -*-

# Scrapy settings for QS_Crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'QS_Crawler'

SPIDER_MODULES = ['QS_Crawler.spiders']
NEWSPIDER_MODULE = 'QS_Crawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'QS_Crawler (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'QS_Crawler.middlewares.QsCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'QS_Crawler.middlewares.QsCrawlerDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'QS_Crawler.pipelines.QsCrawlerPipeline': 300,
    'QS_Crawler.pipelines_mysql.MySQLPipeLine':500
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_SETTINGS = {
   'HOST':'127.0.0.1',    #数据库地址
   'DATABASE':'quanshu1105',    #数据库名称
   'USER':'root',           #登陆用户名
   'PASSWORD':'130147060',       #登陆密码
   'CHARSET':'utf8'         #字符编码
}

SPIDER_DB_OP_DISPACH = {
     #sql = "insert into table(id, name, address) values(xxx)"
    'qs':{'QsCrawlerBookKinds':('insert into book_kinds(kind_id,kind_name) VALUES (%s,%s)',
              ('kind_id','kind_name')),
                    'QsCrawlerBookLists':('insert into book_lists(book_id, img_url,  book_name, author_name,book_intro,kind_id) VALUES (%s,%s, %s, %s, %s,%s)',
              ('book_id','img_url', 'book_name', 'author_name','book_intro','kind_id')),
                    'QsCrawlerBooksDetails':('insert into book_details(srction_book,  book_detail, book_id) VALUES ( %s, %s,%s)',
              ('srction_book', 'book_detail','book_id'))
            }
}

###############   log settings begin   ######################
LOG_LEVEL = "DEBUG"
from datetime import datetime
import os
today = datetime.now()
LOG_DIR = "log"
if not os.path.exists(LOG_DIR):
   os.mkdir(LOG_DIR)
LOG_FILE = "{}/scrapy_{}_{}_{}.log".format(LOG_DIR, today.year, today.month, today.day)
###############   log settings end   ######################
