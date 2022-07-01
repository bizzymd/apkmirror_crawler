import sys

from script_functions.menu_prints import print_versions, print_functionalities, print_menu
from script_functions.read_input_helper import read_input_link, read_versions_num

WEBSITE = "https://www.apkmirror.com/"


class InputError(Exception):
    pass


def read_single_application():
    print("You have chosen to crawl a single application")
    print("Please input an application URL, in the following format: https://www.apkmirror.com/apk/developer/apk/")
    return read_input_link('apk/')


def read_category_link():
    print("You have chosen to crawl a single category")
    print("Please input an application URL, in the following format: https://www.apkmirror.com/categories/category/")
    return read_input_link('categories')


def read_functionalities(input):
    if input == 1:
        apk_link = read_single_application()
        return apk_link
    if input == 2:
        category_link = read_category_link()
        return category_link

    print("You have chosen to crawl all categories")


def user_menu_input(num_options):
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


def user_menu_options(option):
    if option == 1:
        input_functionalities()
    if option == 2:
        input_num_versions()


def input_num_versions():
    print_versions()
    num_versions = read_versions_num()
    print(num_versions)


def input_functionalities():
    print_functionalities()
    user_input = user_menu_input(3)
    crawl_link = read_functionalities(user_input)
    print(crawl_link)


def main_menu():
    user_input = None
    options = [i for i in range(1, 5)]
    while not user_input == 5:
        print_menu()
        user_input = user_menu_input(5)
        user_menu_options(user_input)

