

def print_wrong_functionality(mode):
    if mode == 'apk/':
        print("Please follow the format https://www.apkmirror.com/apk/developer/application/")
    else:
        print("Please follow the format https://www.apkmirror.com/categories/category/")

    print("Type 'Exit' to return to the main menu")


def print_menu_functionalities():
    print("Functionalities:")
    print("(1) Crawl a single application")
    print("(2) Crawl a single category")
    print("(3) Crawl all categories (DEFAULT)")


def print_menu():
    print("(1) Functionalities")
    print("(2) Number of applications to download")
    print("(3) Crawling settings")
    print("(4) Start crawler")


def print_spider_settings():
    print("In this option you can choose which of the spiders to run")
    print("There are three options, input an integer based on the options below")
    print("(1) Crawl APKs, (2) Download APKs, (3) Crawl and Download APKs(default)")


def print_log_settings():
    print("In this option you can choose if you want to overwrite or append the crawled applications to the output file")
    print("(1) Overwrite (default)")
    print("(2) Append")


def print_crawler_settings():
    print("Settings:")
    print("(1) Spider settings (on/off)")
    print("(2) Overwrite output file (on/off)")


def print_menu_versions():
    print("Choose a number of versions(of an application) to crawl (Facebook 1.0, Facebook 1.1, ...)")
    print("If an application has less than the desired amount, it will crawl all available versions")
    print("Please input an integer(or 'Default' for all versions), negative values will be taken as absolute")


def print_single_functionality(mode):
    print("You have chosen to crawl a single " + mode)
    if mode == "application":
        print("Please input an application URL, in the following format: https://www.apkmirror.com/apk/developer/application/")
    else:
        print("Please input an application URL, in the following format: https://www.apkmirror.com/categories/category")
    print("Type 'Exit' to return to the main menu")


def print_default_settings():
    print("The scraper has the following (default) settings: Scrape all categories, scrape every version of an")
    print("application, parse the application information and download them and overwrite the output.csv file\n")