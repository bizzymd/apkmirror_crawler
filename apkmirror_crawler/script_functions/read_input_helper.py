from typing import NewType

from script_functions.menu_prints import print_wrong_functionality


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
