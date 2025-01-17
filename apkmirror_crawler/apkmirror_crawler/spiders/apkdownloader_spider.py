import scrapy
import csv
from scrapy import Request
from apkmirror_crawler.items import ApkMirrorDownloader

WEBSITE = "https://www.apkmirror.com"


class ApkDownloader(scrapy.spiders.Spider):
    name = 'apks_download'
    # Spider specific download delay
    download_delay = 20
    start_urls = []

    # Starting method to download the APK files. Opens the output.csv file and filters by the download_link item
    def start_requests(self):
        with open(self.file_name) as data:
            reader = csv.DictReader(data)
            for item in reader:
                request = Request(item['download_link'], callback=self.parse, meta={'file_name': item['name']})
                yield request

    # Main parse method, scrapes everything on the download link page and extracts the data in an Item
    def parse(self, response):
        item = ApkMirrorDownloader()
        download_link = ''.join(
            WEBSITE + response.xpath("//div[@class='f-sm-50'][1]/p[@class='notes'][2]/span/a/@href").extract_first())
        item['file_urls'] = [download_link]
        item['file_name'] = response.meta.get('file_name')

        yield item