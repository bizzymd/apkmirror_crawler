# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ApkMirrorItem(scrapy.Item):
    app_name = scrapy.Field()
    download_link = scrapy.Field()
    developer = scrapy.Field()
    version = scrapy.Field()
    package = scrapy.Field()
    size = scrapy.Field()
    os = scrapy.Field()
    dpi = scrapy.Field()
    sha1_certificate = scrapy.Field()
    sha256_certificate = scrapy.Field()
    certificate = scrapy.Field()
    md5_hash = scrapy.Field()
    sha1_hash = scrapy.Field()
    sha256_hash = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    app_link = scrapy.Field()
    categories = scrapy.Field()


class ApkMirrorDownloader(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    file_name = scrapy.Field()
