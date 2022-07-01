import scrapy
from scrapy import Request
from apkmirror_crawler.items import ApkMirrorItem

WEBSITE = "https://www.apkmirror.com"


class ApkCategories(scrapy.Spider):
    name = 'apk_mirror'

    def start_requests(self):
        # Single App
        if self.option == 'SAPP':
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            print("SINGLE APP")
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            request = Request(self.start_url, callback=self.parse_app_helper)
            yield request
        # Single category
        elif self.option == 'SCA':
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            print("SINGLE CATEGORY")
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            request = Request(self.start_url, callback=self.parse_category_helper)
            yield request
        # Parse all categories
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            print("EVERYTHING")
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            request = Request("https://www.apkmirror.com/categories/", callback=self.parse)
            yield request

    def parse(self, response, **kwargs):
        categories = response.xpath("//div[@class='widget widget_appmanager_categorylistingwidget']//div["
                                    "@class='table-row']/div[position()=1]/h5/a/@href")

        # Scrape all categories
        for category in categories:
            category_link = ''.join(WEBSITE + category.extract())
            request = Request(category_link, callback=self.parse_category_helper)
            yield request

    #
    def parse_category_helper(self, response):
        # Scrape all apps from letter A
        request = Request(response.url, callback=self.parse_category, dont_filter=True)
        yield request

        # B-Z+#
        # category_letters = response.xpath(
        #     "//div[@class='listWidget']/div[@class='appRow center'][2]/div[@class='pagination']/div/a/@href")
        # for letter in category_letters:
        #     letter_link = ''.join(WEBSITE + letter.extract())
        #     print(letter_link)
        #     request = Request(letter_link, callback=self.parse_category)
        #     yield request

    def parse_category(self, response):
        apps = response.xpath("//div[@class='listWidget'][position()=1]//div[@class='appRow']/div/div[position("
                              ")=2]/h5/a/@href")

        # for all apps in category

        for app in apps:
            app_link = ''.join(WEBSITE + app.extract())
            request = Request(app_link, callback=self.parse_app_helper)
            yield request

        next_page = response.xpath("//div[@class='pagination']/div[@class='wp-pagenavi']/a["
                                   "@class='nextpostslink']/@href")
        if next_page:
            next_page = ''.join(WEBSITE + next_page.extract_first())
            request = Request(next_page, callback=self.parse_category)
            yield request

    def parse_app_helper(self, response):
        more_uploads = response.xpath("//div[@id='primary']//div[@class='table-row']/div/a/@href")

        # User input for the retrieval of a number of versions for each app, in case of no input, retrieve all versions
        try:
            versions_required = int(self.ver_req) - 1
        except AttributeError:
            versions_required = int

        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        print(versions_required)
        print("\n\n\n\n\n\n\n\n\n\n\n\n")

        if more_uploads:
            more_uploads = ''.join(WEBSITE + more_uploads.extract_first())
            request = Request(more_uploads, callback=self.parse_more_app,
                              meta={'versions_req': versions_required})
        else:
            request = Request(response.url, callback=self.parse_app,
                              dont_filter=True, meta={'versions_req': versions_required},)

        yield request

    def parse_more_app(self, response):
        versions = response.xpath("//div[@class='appRow']//div[2]/div/h5/a/@href")

        version_num = 0

        for version in versions:
            version = ''.join(WEBSITE + version.extract())
            request = Request(version, callback=self.parse_version)
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            print(version_num, response.meta.get('versions_req'))
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            yield request
            if version_num == response.meta.get('versions_req'):
                return
            version_num = version_num + 1

        # Number of apk versions left to crawl, relevant if specified
        versions_left = response.meta.get('versions_req') - version_num
        print(versions_left)

        next_page = response.xpath("//div[@class='pagination']/div[@class='wp-pagenavi']/a["
                                   "@class='nextpostslink']/@href")
        if next_page:
            next_page = ''.join(WEBSITE + next_page.extract_first())
            request = Request(next_page, callback=self.parse_more_app, meta={'versions_req': versions_left})
            yield request

    def parse_app(self, response):

        related_app = response.xpath(
            "//ul[@class='dropdown-menu breadcrumbs-menu']/li[2]/a[@class='accent_color']").extract()
        if related_app:
            versions = response.xpath("//div[@id='primary']//div[@class='listWidget'][position()=2]")
        else:
            versions = response.xpath("//div[@id='primary']//div[@class='listWidget'][position()=1]")

        versions = versions.xpath(".//div[@class='table-row']//div[@class='table-cell'][position()=2]/div/h5/a/@href")

        # for all versions
        for version_num, version in enumerate(versions):
            version_link = ''.join(WEBSITE + version.extract())
            request = Request(version_link, callback=self.parse_version)
            yield request
            if version_num == response.meta.get('versions_req'):
                break

    def parse_version(self, response):
        variants = response.xpath("//div[@class='listWidget']//div[@class='table-row headerFont']")

        if variants.extract():
            for variant in variants:
                architecture = variant.xpath(
                    "./div[text() = 'arm64-v8a' or text() = 'universal' or text() = 'noarch' ] "
                    "or text() = 'arm64-v8a + armeabi-v7a'	")
                apk_badge = variant.xpath("./div/span[@class='apkm-badge']")
                if architecture and apk_badge:
                    variant_link = ''.join(WEBSITE + variant.xpath("./div/a/@href").extract_first())
                    request = Request(variant_link, callback=self.parse_info)
                    yield request
                    break
        else:
            request = Request(response.request.url, callback=self.parse_info, dont_filter=True)
            yield request

    def parse_info(self, response):
        item = ApkMirrorItem()

        developer = response.xpath("//h3/a/text()").extract()
        details = response.xpath("//div[@class='apk-detail-table wrapText']")
        signatures = response.xpath("//div[@class='modal-body']")
        download_link = ''.join(WEBSITE + response.xpath("//div[@class='center f-sm-50']/div/a/@href").extract_first())

        item['app_name'] = response.xpath(
            "//h1[@class='marginZero wrapText app-title fontBlack noHover']/text()").extract()

        item['developer'] = ''.join(developer)

        # Version scrape
        version_boolean = ''.join(details.xpath("./div[1]/div[2]/text()[1]").extract()).strip()

        if "Version" in version_boolean:
            item['version'] = version_boolean.replace('Version: ', '')
        else:
            item['version'] = ''.join(details.xpath("./div[1]/div[2]/text()[2]").extract()).replace('Version: ',
                                                                                                    '').strip()

        # Package scrape
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

        item['download_link'] = download_link
        item['app_link'] = response.url

        yield item
