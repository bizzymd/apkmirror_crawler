
class InputError(Exception):
    pass

def print_functionalities():
    print("(1) Crawl a single application")
    print("(2) Crawl a single category")
    print("(3) Crawl all categories (DEFAULT)")


def input_functionalities():
    user_input = None
    options = [1, 2, 3]
    while user_input not in options:
        print_functionalities()
        try:
            user_input = int(input())
            if user_input not in options:
                raise InputError
        except ValueError:
            print("Please input an integer")
        except InputError:
            print("Please choose one of the available options (integer)")

