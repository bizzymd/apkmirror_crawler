def read_input_link(mode):
    while True:
        user_input = input()

        if user_input.startswith("https://www.apkmirror.com/" + mode):

            apk_link = user_input.split("https://www.apkmirror.com/" + mode)

            if apk_link[1].count("/") == 2:
                print("URL accepted, functionality saved")
                return user_input

        if user_input == "Exit":
            return
        link_input_printer(mode)


def link_input_printer(mode):
    if mode == "apk/":
        print("Please follow the format https://www.apkmirror.com/apk/developer/apk/")
        print("Type 'Exit' to return to the main menu")
    else:
        print("Please follow the format https://www.apkmirror.com/categories/category/")
        print("Type 'Exit' to return to the main menu")


def read_versions_num():
    user_input = None
    while not type(user_input) == int:
        user_input = input()

    return user_input