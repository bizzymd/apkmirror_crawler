from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from apkmirror_crawler.spiders.apkdownloader_spider import ApkDownloader
from apkmirror_crawler.spiders.apkinfo_spider import ApkCategories
from script_functions.read_input import main_menu
from script_functions.signature import signature


def crawler_script(crawler_settings):
    configure_logging()

    ApkCategories.custom_settings = {"FEEDS": {"output.csv": {"format": "csv", "overwrite": True}}}
    if crawler_settings[4] == "LogsOn":
        runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        if crawler_settings[3] == ('APK' or "APK&Download"):
            yield runner.crawl(ApkCategories, option=crawler_settings[0], start_url=crawler_settings[1],
                               ver_req=crawler_settings[2])
        if crawler_settings[3] == ('Download' or "APK&Download"):
            yield runner.crawl(ApkDownloader, file_name='output.csv')
        reactor.stop()

    crawl()
    reactor.run()  # the script will block here until the last crawl call is finished


if __name__ == "__main__":
    signature()
    crawler_script(main_menu())
