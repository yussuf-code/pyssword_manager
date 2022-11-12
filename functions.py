import pyperclip
import random
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '#', '$', '%', '&']

    password_list = []
    for n in range(0, 6):
        password_list.append(letters[random.randint(0, 51)])
        password_list.append(numbers[random.randint(0, 9)])
        password_list.append(symbols[random.randint(0, 4)])

    random.shuffle(password_list)
    password = ''.join(password_list)

    pyperclip.copy(password)

    return password


def add_account(website, account_name, username, password):

    with open("data.json", "r") as passwords:
        data = json.load(passwords)

    if website in data:
        data[website][account_name] = {"Username": username, "Password": password}
    else:
        data[website] = {account_name: {"Username": username, "Password": password}}

    with open("data.json", "w") as passwords:
        json.dump(data, passwords, indent=4)

    print("\n\nAdded Successfully!\n")
    print(f"\nusername: {username}\npassword: {password}\n")


def update_account(website):

    with open("data.json", "r") as passwords:
        data = json.load(passwords)

    if website in data:

        accounts = data[website]

        if not accounts:
            print("\nNO ACCOUNTS HERE!\n")
        else:
            accounts_keys_list = list(accounts.keys())

            for n in range(0, len(accounts)):
                print(f"\n{[n+1]} {accounts_keys_list[n]}.")

            choice = int(input("\nChoose an Account: "))

            account = accounts_keys_list[choice-1]
            account_data = data[website][account]

            new_username = input("\nNew username: ")
            new_password = input("\nNew password: ")

            if len(new_username) == 0 or len(new_password) == 0:
                print("\nNO INPUT!\n")

            else:
                account_data["Username"] = new_username
                account_data["Password"] = new_password

                with open("data.json", "w") as passwords:
                    json.dump(data, passwords, indent=4)

                print("\n\nUpdated Successfully!\n")
                print(f"\nusername: {new_username}\npassword: {new_password}\n")

    else:
        print("\nDOES NOT EXIST!\n")


def remove_account(website):

    with open("data.json", "r") as passwords:
        data = json.load(passwords)

    if website in data:

        accounts = data[website]

        if not accounts:
            print("\nNO ACCOUNTS HERE!")

        else:
            accounts_keys_list = list(accounts.keys())

            for n in range(0, len(accounts)):
                print(f"\n{[n+1]} {accounts_keys_list[n]}.")

            choice = int(input("\nChoose an Account: "))

            account = accounts_keys_list[choice-1]
            data[website].pop(account)

            with open("data.json", "w") as passwords:
                json.dump(data, passwords, indent=4)

            print("\nRemoved Successfully!\n")

    else:
        print("\nDOES NOT EXIST!")


def search(website):
    with open("data.json", "r") as passwords:
        data = json.load(passwords)

        if website in data:
            accounts = data[website]

            if not accounts:
                print("\nNO ACCOUNTS HERE!")

            else:
                accounts_keys_list = list(accounts.keys())

                for n in range(0, len(accounts)):
                    print(f"\n{[n+1]} {accounts_keys_list[n]}.")

                choice = int(input("\nChoose an Account: "))

                account = accounts_keys_list[choice-1]
                account_data = accounts[account]

                pyperclip.copy(account_data['Password'])

                print(f"\n\nUsername: {account_data['Username']}\nPassword: {account_data['Password']}")

        else:
            print("\nDOES NOT EXIST!")