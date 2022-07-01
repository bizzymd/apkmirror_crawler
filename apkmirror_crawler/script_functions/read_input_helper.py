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