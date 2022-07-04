import sys
from script_functions.signature import signature
from script_functions.read_input_helper import read_functionality, read_versions, read_settings, user_input_integer, crawl_option_to_string
from script_functions.menu_prints import print_menu, print_menu_functionalities, print_menu_versions, print_crawler_settings, \
    print_default_settings
from script_functions.menu_prints import print_single_functionality

WEBSITE = "https://www.apkmirror.com/"


# Check for User input on single application crawl(option 1.1)
def read_single_application():
    print_single_functionality('application')
    return read_functionality('apk/')


# Check for User input on single category link crawl(option 1.2)
def read_category_link():
    print_single_functionality('category')
    return read_functionality('categories')


# Check for User input on main functionalities(option 1 on Main menu)
def read_functionalities(input):

    if input == 1:
        apk_link = read_single_application()
        return apk_link

    if input == 2:
        category_link = read_category_link()
        return category_link

    print("You have chosen to crawl all categories")


def user_menu_options(option):

    if option == 1:
        return input_functionalities()

    if option == 2:
        return input_num_versions()


    return input_settings()


# Check input for option 3(which spider to run or overwrite output.csv file true/false)
def input_settings():
    print_crawler_settings()
    return read_settings()


# Check input for option 2(number of versions for each app required)
def input_num_versions():
    print_menu_versions()
    num_versions = read_versions()
    return None, num_versions


# Check input for option 1(main functionalities)
def input_functionalities():
    print_menu_functionalities()
    user_input = user_input_integer(3)
    crawl_link = read_functionalities(user_input)

    # If user chose option 1 or 2, but did not input a link, revert to default option(crawl everything)
    if crawl_link is None:
        user_input = 3

    return user_input, crawl_link


def main_menu():
    # Necessary prints
    signature()
    print_default_settings()
    # Initialise the crawl settings with the default options
    crawl_settings = ["ALL", None, sys.maxsize, "APK&Download", True]
    user_input = None

    # Loop to check for users input
    while not user_input == 4:
        print_menu()
        user_input = user_input_integer(4)
        user_values = user_menu_options(user_input)

        if user_input == 1:
            crawl_settings[0] = crawl_option_to_string(user_values[0])
            crawl_settings[1] = user_values[1]
        elif user_input == 2:
            crawl_settings[2] = user_values[1]
        elif user_input == 3:
            crawl_settings[user_values[0]] = user_values[1]

    return crawl_settings

