# app name xpath - //div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/h5[1]/span/text()
# sha1   - //div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/span[@class='wordbreak-all'][1]/a/text()
# sha256 - //div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/span[@class='wordbreak-all'][2]/a/text()
# certf  - //div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/span[3]/text()
# mda5   - //div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/span[@class='wordbreak-all'][3]/text()
# sha1   - //div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/span[@class='wordbreak-all'][4]/text()
# sha256 - //div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/span[@class='wordbreak-all'][5]/text()

# inputs
# scrapy crawl apk_mirror -O output.csv -a option=SCA -a start_url=https://www.apkmirror.com/categories/no_category/ -a ver_req=1


# scrapy crawl apk_mirror -O output.csv -a option=SAPP -a start_url=https://www.apkmirror.com/apk/adguard-software-limited/adguard/ -a ver_req=1
