from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer

from apkmirror_crawler.spiders.apkdownloader_spider import ApkDownloader
from apkmirror_crawler.spiders.apkinfo_spider import ApkCategories
from script_functions.options import input_functionalities
from script_functions.signature import signature


def read_input():
    input_functionalities()


def main():
    configure_logging()

    ApkCategories.custom_settings = {"FEEDS": {"output.csv": {"format": "csv", "overwrite": True}}}
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        # yield runner.crawl(ApkCategories, option='SCA', start_url='https://www.apkmirror.com/categories/no_category/', ver_req='1')
        yield runner.crawl(ApkCategories, option='SAPP', start_url='https://www.apkmirror.com/apk/samsung-electronics-co-ltd/a-plugger/',
                           ver_req='1')
        yield runner.crawl(ApkDownloader, file_name='output.csv')
        reactor.stop()

    crawl()
    reactor.run()  # the script will block here until the last crawl call is finished


if __name__ == "__main__":
    signature()
    read_input()
