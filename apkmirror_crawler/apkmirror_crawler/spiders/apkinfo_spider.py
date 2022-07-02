import scrapy
import sys
from scrapy import Request
from apkmirror_crawler.items import ApkMirrorItem

WEBSITE = "https://www.apkmirror.com"


# Spider class used to crawl the website
class ApkCategories(scrapy.Spider):
    # Spider name, mostly if ran from a terminal, i.e., scrapy crawl 'name'
    name = 'apk_mirror'

    # The spider starts in this function, based on the chosen option, it will either crawl a single application,
    # crawl a single category or crawl everything
    def start_requests(self):
        # Request to parse a single application
        if self.option == 'SAPP':
            request = Request(self.start_url, callback=self.parse_app_helper)
            yield request
        # Request to parse a single category
        elif self.option == 'SCA':
            request = Request(self.start_url, callback=self.parse_category_helper)
            yield request
        # Request to parse all categories
        else:
            request = Request("https://www.apkmirror.com/categories/", callback=self.parse)
            yield request

    def parse(self, response, **kwargs):
        categories = response.xpath("//div[@class='widget widget_appmanager_categorylistingwidget']//div["
                                    "@class='table-row']/div[position()=1]/h5/a/@href")

        # Request to parse all categories
        for category in categories:
            category_link = ''.join(WEBSITE + category.extract())
            request = Request(category_link, callback=self.parse_category_helper)
            yield request

    # Parse all apps from letter page A-Z and #(Apps that start with a symbol)
    # Separate request is needed for first letter page, the reason is simply that the crawler needs
    # access to the first letter page in order to retrieve the rest of the pages
    def parse_category_helper(self, response):

        # Request to parse all apps from letter page A
        request = Request(response.url, callback=self.parse_category, dont_filter=True)
        yield request

        # Parse all apps from letter pages B to Z and #(symbols)
        category_letters = response.xpath(
            "//div[@class='listWidget']/div[@class='appRow center'][2]/div[@class='pagination']/div/a/@href")

        # if-statement that checks for category_letters row
        if not category_letters:
            category_letters = response.xpath("//div[@class='listWidget']/div[@class='appRow center'][1]/div["
                                              "@class='pagination']/div/a/@href")

        # Request to parse all page letters of the Category
        for letter in category_letters:
            letter_link = ''.join(WEBSITE + letter.extract())
            request = Request(letter_link, callback=self.parse_category)
            yield request

    def parse_category(self, response):
        apps = response.xpath("//div[@class='listWidget'][position()=1]//div[@class='appRow']/div/div[position("
                              ")=2]/h5/a/@href")

        # Loop through the apps on the page, 30 per page, and request to parse the app versions
        for app in apps:
            app_link = ''.join(WEBSITE + app.extract())
            request = Request(app_link, callback=self.parse_app_helper)
            yield request

        # Retrieve the next page of applications, using the 'Next' button(if available)
        next_page = response.xpath("//div[@class='pagination']/div[@class='wp-pagenavi']/a["
                                   "@class='nextpostslink']/@href")
        # Request to parse the next page of applications, note the recursion
        if next_page:
            next_page = ''.join(WEBSITE + next_page.extract_first())
            request = Request(next_page, callback=self.parse_category)
            yield request

    # Mostly a helper function used to send requests to parse applications. This function takes care of the two scenarios
    # 1. The application has 10 or fewer versions 2. The application has more than 10 versions
    def parse_app_helper(self, response):
        more_uploads = response.xpath("//div[@id='primary']//div[@class='table-row']/div/a/@href")

        # User input for the retrieval of a number of versions for each app, in case of no input, retrieve all versions
        if self.ver_req == 'undefined':
            versions_required = sys.maxsize
        else:
            versions_required = int(self.ver_req) - 1

        # Request to parse the application based on the second scenario
        if more_uploads:
            more_uploads = ''.join(WEBSITE + more_uploads.extract_first())
            request = Request(more_uploads, callback=self.parse_more_app,
                              meta={'versions_req': versions_required})
        else:
            request = Request(response.url, callback=self.parse_app,
                              dont_filter=True, meta={'versions_req': versions_required}, )

        yield request

    # Function to crawl the "See more uploads..." pages
    def parse_more_app(self, response):
        versions = response.xpath("//div[@class='appRow']//div[2]/div/h5/a/@href")

        version_num = 0
        versions_required = response.meta.get('versions_req')

        # Loop through the application versions and request to parse
        for version in versions:
            version = ''.join(WEBSITE + version.extract())
            request = Request(version, callback=self.parse_version)
            yield request
            if version_num == versions_required:
                return
            version_num = version_num + 1

        # Number of app versions left to crawl, relevant if input was specified
        versions_left = versions_required - version_num

        # Retrieve the next page of application versions, using the 'Next' button(if available)
        next_page = response.xpath("//div[@class='pagination']/div[@class='wp-pagenavi']/a["
                                   "@class='nextpostslink']/@href")
        # Request to parse the next page of application versions, note the recursion
        if next_page:
            next_page = ''.join(WEBSITE + next_page.extract_first())
            request = Request(next_page, callback=self.parse_more_app, meta={'versions_req': versions_left})
            yield request

    # Function to crawl the applications in the scenario only 10 or fewer versions are present
    def parse_app(self, response):

        # This part of code is used to retrieve the application versions.
        related_app = response.xpath(
            "//ul[@class='dropdown-menu breadcrumbs-menu']/li[2]/a[@class='accent_color']").extract()
        if related_app:
            versions = response.xpath("//div[@id='primary']//div[@class='listWidget'][position()=2]")
        else:
            versions = response.xpath("//div[@id='primary']//div[@class='listWidget'][position()=1]")

        versions = versions.xpath(".//div[@class='table-row']//div[@class='table-cell'][position()=2]/div/h5/a/@href")

        # Loop through the application versions and request to parse
        for version_num, version in enumerate(versions):
            version_link = ''.join(WEBSITE + version.extract())
            request = Request(version_link, callback=self.parse_version)
            yield request
            if version_num == response.meta.get('versions_req'):
                break

    # Function to parse the versions page, based on some criteria, required if different uploads of a version exist
    def parse_version(self, response):
        variants = response.xpath("//div[@class='listWidget']//div[@class='table-row headerFont']")

        if variants.extract():
            for variant in variants:
                # Check for architecture of the APK
                architecture = variant.xpath(
                    "./div[text() = 'arm64-v8a' or text() = 'universal' or text() = 'noarch' ] "
                    "or text() = 'arm64-v8a + armeabi-v7a'	")
                # Check if the download is an APK and split APK, the latter requires an external application
                apk_badge = variant.xpath("./div/span[@class='apkm-badge']")
                if architecture and apk_badge:
                    variant_link = ''.join(WEBSITE + variant.xpath("./div/a/@href").extract_first())
                    request = Request(variant_link, callback=self.parse_info)
                    yield request
                    break
        # Request to parse the version page in the scenario when only one APK download is present
        else:
            request = Request(response.request.url, callback=self.parse_info, dont_filter=True)
            yield request

    # Main function used to scrape all the details from an application version
    def parse_info(self, response):
        item = ApkMirrorItem()

        # Variables used to shorten(refactor) the code
        developer = response.xpath("//h3/a/text()").extract()
        details = response.xpath("//div[@class='apk-detail-table wrapText']")
        signatures = response.xpath("//div[@class='modal-body']")
        download_link = ''.join(WEBSITE + response.xpath("//div[@class='center f-sm-50']/div/a/@href").extract_first())

        item['app_name'] = response.xpath(
            "//h1[@class='marginZero wrapText app-title fontBlack noHover']/text()").extract()

        item['developer'] = ''.join(developer)

        # Scrape version number
        version_boolean = ''.join(details.xpath("./div[1]/div[2]/text()[1]").extract()).strip()

        if "Version" in version_boolean:
            item['version'] = version_boolean.replace('Version: ', '')
        else:
            item['version'] = ''.join(details.xpath("./div[1]/div[2]/text()[2]").extract()).replace('Version: ',
                                                                                                    '').strip()

        # Scrape package
        package_boolean = ''.join(details.xpath("./div[1]/div[2]/span[2]/text()").extract()).strip()

        if "Package" in package_boolean:
            item['package'] = package_boolean.replace('Package: ', '')
        else:
            item['package'] = ''.join(details.xpath("./div[1]/div[2]/span/text()").extract()).replace('Package: ',
                                                                                                      '').strip()
        # Scrape Details
        item['size'] = ''.join(details.xpath("./div[2]/div[2]/text()").extract()).strip()
        item['os'] = ''.join(details.xpath("./div[3]/div[2]/div/text()").extract()).strip()
        item['dpi'] = ''.join(details.xpath("./div[4]/div[2]//text()").extract())
        date = ''.join(details.xpath("./div[6]/div[2]//text()").extract()).replace('Uploaded ', '')
        item['date'] = date.split('at', 1)[0]

        # Scrape MD5, SHA1, SHA256 signatures
        item['sha1_certificate'] = ''.join(signatures.xpath("./span[1]/a/text()").extract())
        item['sha256_certificate'] = ''.join(signatures.xpath("./span[2]/a/text()").extract())
        item['certificate'] = ''.join(signatures.xpath("./span[3]/text()").extract())
        item['md5_hash'] = ''.join(signatures.xpath("./span[4]/text()").extract())
        item['sha1_hash'] = ''.join(signatures.xpath("./span[5]/text()").extract())
        item['sha256_hash'] = ''.join(signatures.xpath("./span[6]/text()").extract())
        item['name'] = ''.join(signatures.xpath("./h5[1]/span/text()").extract())

        # The direct download link and the link to the application
        item['download_link'] = download_link
        item['app_link'] = response.url

        yield item
