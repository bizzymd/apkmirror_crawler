WEBSITE = "https://www.apkmirror.com/"

class InputError(Exception):
    pass


def print_functionalities():
    print("Functionalities:")
    print("(1) Crawl a single application")
    print("(2) Crawl a single category")
    print("(3) Crawl all categories (DEFAULT)")


def read_single_application():
    print("You have chosen to crawl a single application")
    print("Please input an application URL, in the following format: https://www.apkmirror.com/apk/developer/apk/")

    while True:
        user_input = input()

        if user_input.startswith("https://www.apkmirror.com/" + "apk/"):

            apk_link = user_input.split("https://www.apkmirror.com/apk/")

            if apk_link[1].count("/") == 2:
                print("URL accepted, functionality saved")
                return user_input

        if user_input == "Exit":
            return

        print("Please follow the format https://www.apkmirror.com/apk/developer/apk/")
        print("Type 'Exit' to return to the main menu")


def read_category_link():
    print("You have chosen to crawl a single application")
    print("Please input an application URL, in the following format: https://www.apkmirror.com/apk/developer/apk/")

    while True:
        user_input = input()

        if user_input.startswith("https://www.apkmirror.com/" + "apk/"):

            apk_link = user_input.split("https://www.apkmirror.com/apk/")

            if apk_link[1].count("/") == 2:
                print("URL accepted, functionality saved")
                return user_input

        if user_input == "Exit":
            return

        print("Please follow the format https://www.apkmirror.com/apk/developer/apk/")
        print("Type 'Exit' to return to the main menu")


def read_functionalities(input):
    if input == 1:
        apk_link = read_single_application()
        return apk_link
    if input == 2:
        category_link = read_category_link()
        return category_link

    print("You have chosen to crawl all categories")


def print_menu():
    print("(1) Functionalities")
    print("(2) Number of applications to download")
    print("(3) Crawling options")
    print("(4) Crawling settings")
    print("(5) Start crawler")


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
        input_functionalities()


def main_menu():
    user_input = None
    options = [i for i in range(1, 5)]
    while not user_input == 5:
        print_menu()
        user_input = user_input_integer(5)
        user_menu_options(user_input)


def input_functionalities():
    print_functionalities()
    user_input = user_input_integer(3)
    crawl_link = read_functionalities(user_input)
    print()
