import random


def password_generator():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    while True:
        number_passwords = 0
        while number_passwords == 0:
            number_passwords = input("How much passwords do you want? ")
            number_passwords = int(number_passwords)
            if number_passwords == 0:
                print("You did not enter a number greater than 0!")
            elif number_passwords > 0:
                break

        lenght = 0
        while lenght < 10:
            lenght = input("How long do you want? ")
            lenght = int(lenght)
            if lenght < 10:
                print("You did not enter a number greater than 10!")
            else:
                break

        for pwd in range(number_passwords):
            passwords = ""
            for c in range(lenght):
                passwords += random.choice(chars)
            print(passwords)
        again = input("Would you like to generate more passwords? ")
        again = again[0].lower()
        if again == "n":
            print("Thank you for using this program!")
            break
        elif again != "n" and again != "y":
            print("Please enter (Y/N) to continue")


password_generator()