from script_functions.read_input_helper import read_functionality, read_versions
from script_functions.menu_prints import print_menu, print_menu_functionalities, print_menu_versions

WEBSITE = "https://www.apkmirror.com/"

class InputError(Exception):
    pass


def read_single_application():
    print("You have chosen to crawl a single application")
    print("Please input an application URL, in the following format: https://www.apkmirror.com/apk/developer/apk/")
    print("Type 'Exit' to return to the main menu")
    return read_functionality('apk/')


def read_category_link():
    print("You have chosen to crawl a single category")
    print("Please input an application URL, in the following format: https://www.apkmirror.com/categories/category")
    print("Type 'Exit' to return to the main menu")
    return read_functionality('categories')


def read_functionalities(input):

    if input == 1:
        apk_link = read_single_application()
        return apk_link

    if input == 2:
        category_link = read_category_link()
        return category_link

    print("You have chosen to crawl all categories")


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


def user_menu_options(option):

    if option == 1:
        return input_functionalities()

    if option == 2:
        return input_num_versions()


def input_num_versions():
    print_menu_versions()
    num_versions = read_versions()
    return None, num_versions


def input_functionalities():
    print_menu_functionalities()
    user_input = user_input_integer(3)
    crawl_link = read_functionalities(user_input)
    return user_input, crawl_link


def crawl_option_to_string(value):

    if value == 1:
        return "SAPP"
    elif value == 2:
        return "SCA"

    return "ALL"


def main_menu():
    crawl_settings = [str] * 3
    user_input = None
    while not user_input == 4:
        print_menu()
        user_input = user_input_integer(4)
        user_values = user_menu_options(user_input)

        if user_input == 1:
            crawl_settings[0] = crawl_option_to_string(user_values[0])
            crawl_settings[1] = user_values[1]
        elif user_input == 2:
            crawl_settings[2] = user_values[1]

    return crawl_settings

