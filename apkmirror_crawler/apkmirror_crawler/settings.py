# Scrapy settings for apkmirror_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'apkmirror_crawler'

SPIDER_MODULES = ['apkmirror_crawler.spiders']
NEWSPIDER_MODULE = 'apkmirror_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'AdsBot-Google'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {'apkmirror_crawler.pipelines.ApkmirrorCrawlerPipeline': 1}
FILES_STORE = './'
MEDIA_ALLOW_REDIRECTS = True
DOWNLOAD_WARNSIZE = 0


# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0


# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
#     'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610,
# }
# ZYTE_SMARTPROXY_ENABLED = True
# # ZYTE_SMARTPROXY_APIKEY = 'f72800b6475b4c4fb4d952980e70020b'
# ZYTE_SMARTPROXY_APIKEY = '9903b9bdd5a94f06ac47ca1f0d85f4a9'
#
# CONCURRENT_REQUESTS = 32
# CONCURRENT_REQUESTS_PER_DOMAIN = 32
# AUTOTHROTTLE_ENABLED = False
# DOWNLOAD_TIMEOUT = 600