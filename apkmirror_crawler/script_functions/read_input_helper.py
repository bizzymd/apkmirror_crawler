from script_functions.menu_prints import print_wrong_functionality, print_spider_settings, print_log_settings


# Exception used in case the user inputted an integer, but not one of the available ones
class InputError(Exception):
    pass


# Input parser for integer, given a number of options
def user_input_integer(num_options):
    user_input = None
    options = [i for i in range(1, num_options + 1)]

    while user_input not in options:
        try:
            user_input = int(input())
            if user_input not in options:
                raise InputError
        except ValueError:
            print("Please input an integer")
        except InputError:
            print("Please choose one of the available options")

    return user_input


# Input parsers for single application/category links
def read_functionality(mode):
    while True:
        user_input = input()

        if user_input.startswith("https://www.apkmirror.com/" + mode):

            apk_link = user_input.split("https://www.apkmirror.com/" + mode)

            if apk_link[1].count("/") == 2:
                print("URL accepted, crawl settings saved")
                return user_input

        if user_input == "Exit":
            return

        print_wrong_functionality(mode)


# Input parser for number of versions to scrape
def read_versions():
    user_input = None
    while not type(user_input) is int:
        user_input = input()

        if user_input == "Default":
            return 'undefined'

        try:
            user_input = abs(int(user_input))
        except ValueError:
            print("Please input an integer(or 'Default' for all versions)")

    return user_input


def crawl_option_to_string(value):

    if value == 1:
        return "SAPP"
    elif value == 2:
        return "SCA"

    return "ALL"


def read_spider_settings(option):
    if option == 1:
        return "APK"
    if option == 2:
        return "Download"
    return "APK&Download"


def read_overwrite_settings(option):
    if option == 1:
        return True
    return False


# Input parser for settings, with two options,
# 1. Spider settings(turn on or off one spider)
# 2. Overwrite or append the results from apkinfo_spider to output.csv
def read_settings():
    while True:
        user_input = user_input_integer(2)

        # Spider settings
        if user_input == 1:
            print_spider_settings()
            user_input = user_input_integer(3)
            return 3, read_spider_settings(user_input)

        # Log settings
        print_log_settings()
        user_input = user_input_integer(2)
        return 4, read_overwrite_settings(user_input)
