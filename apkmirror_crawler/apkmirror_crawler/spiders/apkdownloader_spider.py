import scrapy
import csv
from scrapy import Request
import json
from apkmirror_crawler.items import ApkMirrorDownloader

WEBSITE = "https://www.apkmirror.com"


class ApkDownloader(scrapy.spiders.Spider):
    name = 'apks_download'
    start_urls = []

    def start_requests(self):
        with open(self.file_name) as data:
            reader = csv.DictReader(data)
            for item in reader:
                request = Request(item['download_link'], callback=self.parse, meta={'file_name': item['name']})
                yield request

    def parse(self, response, **kwargs):
        item = ApkMirrorDownloader()
        download_link = ''.join(
            WEBSITE + response.xpath("//div[@class='f-sm-50'][1]/p[@class='notes'][2]/span/a/@href").extract_first())
        item['file_urls'] = [download_link]
        item['file_name'] = response.meta.get('file_name')

        yield item



        # JSON
        # with open('output.json') as json_file:
        #     data = json.load(json_file)
        #     for item in data:
        #         download_link = item['download_link']
        #         request = Request(download_link, callback=self.parse, meta={'file_name': item['name']})
        #         yield request