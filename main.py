from functions import *


on = False
start = input("PRESS [0] TO START > ")
if start == "0":
    on = True

while on:
    print("\nP Y S S W O R D\nM A N A G E R\n")
    choice = input("\n[1] Add a new account.\n"
                   "\n[2] Update an account.\n"
                   "\n[3] Remove an account.\n"
                   "\n[4] Search.\n"
                   "\n\n[0] Exit.\n\n>> ")

    # Exit
    if choice == "0":
        on = False

    # Add Account
    elif choice == "1":

        website = input("\nWebsite Name: ")
        account_name = input("\nAccount Name: ")
        username = input("\nUsername or Email: ")

        if len(website) == 0 or len(account_name) == 0 or len(username) == 0:
            print("\nNO INPUT!\n")
            continue

        password_choice = input("\n[1] Generate a password.\n[2] Enter a password.\n\n>> ")

        if password_choice == "1":
            password = generate_password()

        elif password_choice == "2":
            password = input("\nPassword: ")

            if len(password) <= 7:
                print("\nINVALID PASSWORD!\n")
                continue

        add_account(website, account_name, username, password)

    # Update Account
    elif choice == "2":

        website = input("\nWebsite Name: ")

        if len(website) == 0:
            print("\nNO INPUT!\n")
            continue

        update_account(website)

    # Remove Account
    elif choice == "3":

        website = input("\nWebsite Name: ")

        if len(website) == 0:
            print("\nNO INPUT!\n")
            continue

        remove_account(website)

    # Search
    elif choice == "4":

        website = input("\nWebsite Name: ")

        if len(website) == 0:
            print("\nNO INPUT!\n")
            continue

        search(website)
