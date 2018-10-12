# -*- coding: utf-8 -*-

# Scrapy settings for LagouMenu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# BOT_NAME = 'LagouMenu'

SPIDER_MODULES = ['LagouMenu.spiders']
NEWSPIDER_MODULE = 'LagouMenu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16

#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# from faker import Faker
# ua = Faker(locale='zh_CN')
# ua = ua.user_agent()
DEFAULT_REQUEST_HEADERS = {
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-type': 'application/json;charset=utf-8',
    'Host': 'www.lagou.com',
    'Cookie': '_ga=GA1.2.517327740.1537433691; user_trace_token=20180920165449-d4d71c20-bcb2-11e8-a275-525400f775ce; LGUID=20180920165449-d4d72096-bcb2-11e8-a275-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=4; JSESSIONID=ABAAABAAAFCAAEG6C7E690F4F627F8CF6DC6EF282C33A52; X_HTTP_TOKEN=2ba16b3e1176657ba97bb2933e8ab57d; LGSID=20181012135907-ee9991ed-cde3-11e8-bbbf-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=; TG-TRACK-CODE=index_navigation; SEARCH_ID=9f5e28f6b5054eae90bba7e1a01adbdf; LG_LOGIN_USER_ID=d4e494df15974391e721bc7e19b18b37b83c438da1e7f46e; _putrc=71F16D06C60C5DD7; login=true; unick=%E4%BB%98; gate_login_token=f7166da628abe0698fb491d327bf18a1429794d682ad2408; _gat=1; LGRID=20181012142136-1283ff73-cde7-11e8-bbbf-5254005c3644',
    'Referer': 'https://www.lagou.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.18\
    1 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'LagouMenu.middlewares.LagoumenuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'LagouMenu.middlewares.LagoumenuDownloaderMiddleware': 543,
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'LagouMenu.pipelines.LagoumenuPipeline': 300,
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

# MONGODB 主机名
MONGODB_HOST = "127.0.0.1"
# MONGODB 端口号
MONGODB_PORT = 27017
# 数据库名称
MONGODB_DBNAME = "LagouMenu"
# 存放数据的表名称
MONGODB_SHEETNAME = "LagouMenu"