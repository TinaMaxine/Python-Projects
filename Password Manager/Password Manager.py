loginCredentials = {'Hydvd@gmail.com': 'abc123@123'}
passwordManager = {}


def console():
    print("password Manager")
    print()
    validateLogin()


def validateLogin():
    userName = input("Please enter your username/email: ")
    password = input("Please enter your password: ")
    print()
    if loginCredentials.get(userName) != 'None':
        try:
            existingPassword = loginCredentials[userName]
            if password == existingPassword:
                print("Login Success!")
                print()
                menu()
            else:
                print("Invalid username/password. Please try again")
                print()
                exit()
        except KeyError:
            print("Invalid username/password. Please try again")
            print()
            exit()


def menu():
    print("1. Enter Password")
    print("2. View Password")
    print("3. Delete Password")
    print("4. Logout")
    print()
    userInput()


def userInput():
    opt = int(input("Please select any of the above options to continue: "))
    print()
    if opt == 1:
        enterPassword()
    elif opt == 2:
        viewPassword()
    elif opt == 3:
        deletePassword()
    elif opt == 4:
        logout()
    else:
        print("Please select a valid option to continue")
        print()
        menu()


def enterPassword():
    appName = input(
        "Please enter the name of the application for which you would like to store the password first: ")
    appPassword = input("Please enter the password now for that application: ")
    print()
    passwordManager.update({appName: appPassword})
    print("Success! Password updated.")
    print()
    menu()


def viewPassword():
    if len(passwordManager) > 0:
        print("Please find the below list of applications for which you have stored passwords:")
        print(list(passwordManager.keys()))
        print()
        appInput = input(
            "Now enter the name of the application for which you want to fetch the password: ")
        if passwordManager.get(appInput) != 'None':
            try:
                appPassword = passwordManager[appInput]
                print()
                print("The password for", appInput, "is", appPassword)
                print()
                menu()
            except KeyError:
                print()
                print("Please enter a valid application name from the above list")
                print()
                menu()
    else:
        print("You don't have any passwords stored yet")
        print()
        update = input(
            "If you want to add a new application & its password, please confirm by typing 'YES'. \nTo go back to the main menu, please enter 'NO': ")
        print()
        if update == 'YES' or update == 'yes':
            print()
            enterPassword()
        elif update == 'NO' or update == 'no':
            print()
            menu()
        else:
            print()
            menu()


def deletePassword():
    if len(passwordManager) > 0:
        print("Please find the below list of applications for which you have stored passwords:")
        print(list(passwordManager.keys()))
        print()
        appInput = input(
            "Now enter the name of the application for which you want to delete the password: ")
        if passwordManager.get(appInput) != 'None':
            try:
                passwordManager.pop(appInput)
                print()
                print("The password for", appInput, "is deleted successfully")
                print()
                menu()
            except KeyError:
                print()
                print("Please enter a valid application name from the above list")
                print()
                menu()
    else:
        print("You don't have any passwords stored yet")
        print()
        update = input(
            "If you want to add a new application & its password, please confirm by typing 'YES'. \nTo go back to the main menu, please enter 'NO': ")
        print()
        if update == 'YES' or update == 'yes':
            print()
            enterPassword()
        elif update == 'NO' or update == 'no':
            print()
            menu()
        else:
            print()
            menu()


def logout():
    exit()


console()
