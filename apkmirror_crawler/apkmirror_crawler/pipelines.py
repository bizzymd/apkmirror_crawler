# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.pipelines.files import FilesPipeline
from apkmirror_crawler.items import ApkMirrorDownloader

# Pipeline class, used for naming of the downloaded files, the file name is retrieved during the parsing part of the
# APK mirror website, which is then stored inside the '.csv' file. In the downloading phase, the "file_name" value is
# retrieved to rename the downloaded file from a hash
# '1b6c0a648f8eceb9b8e8d71e5ff185ace7c479fa' to 'com.example.app123_1.0-1_minAPI10(nodpi).apk'
class ApkmirrorCrawlerPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):

        return 'files/' + request.meta.get('file_name').replace('_apkmirror.com', '')

    def get_media_requests(self, item, info):
        if isinstance(item, ApkMirrorDownloader):
            for file_url in item['file_urls']:
                yield scrapy.Request(file_url, meta={'file_name': item['file_name']})

