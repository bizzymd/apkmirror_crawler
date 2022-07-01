

def print_wrong_functionality(mode):

    if mode == 'apk/':
        print("Please follow the format https://www.apkmirror.com/apk/developer/apk/")
    else:
        print("Please follow the format https://www.apkmirror.com/categories/category/")

    print("Type 'Exit' to return to the main menu")


def print_menu_functionalities():
    print("Functionalities:")
    print("(1) Crawl a single application")
    print("(2) Crawl a single category")
    print("(3) Crawl all categories (DEFAULT)")


# 3 - for parse only/ download only, both
# 4 - custom settings for file name, overwrite file or not.
# 5 - Logs on/off?
def print_menu():
    print("(1) Functionalities")
    print("(2) Number of applications to download")
    print("(3) Crawling settings")
    print("(4) Start crawler")


def print_menu_versions():
    print("Choose a number of versions(of an application) to crawl (Facebook 1.0, Facebook 1.1, ...)")
    print("If an application has less than the desired amount, it will crawl all available versions")
    print("Please input an integer(or 'Default' for all versions), negative values will be taken as absolute")
