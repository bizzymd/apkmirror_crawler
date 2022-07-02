from typing import NewType

from script_functions.menu_prints import print_wrong_functionality, print_spider_settings, print_log_settings


class InputError(Exception):
    pass


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


def read_versions():
    user_input = None
    while not type(user_input) is int:
        user_input = input()

        if user_input == "Default":
            return 'undefined'

        try:
            user_input = max(0, int(user_input))
            print(user_input)
        except ValueError:
            print("Please input an integer(or 'Default' for all versions)")

    return user_input


def read_spider_settings(option):
    if option == 1:
        return "APK"
    if option == 2:
        return "Download"
    return "APK&Download"


def read_log_settings(option):
    if option == 1:
        return True
    return False


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
        return 4, read_log_settings(user_input)
