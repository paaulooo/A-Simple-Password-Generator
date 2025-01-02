import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
minpass = 1
minlen = 10

def password_generator(number_passwords: int, length: int):
    if number_passwords < minpass:
        return f"You need a minimum of {minpass} passwords"
    if length < minlen:
        return f"You need a minimum password length of {minlen}"

    passwords = ''
    for a in range(number_passwords):
        password = ''
        for b in range(length):
            password += random.choice(chars)
        passwords += (password + '\n')
    return passwords

number_passwords = int(input(f"How many passwords do you want to generate?(minimum {minpass}): "))
length = int(input(f"How long do you want the password to be?(minimum {minlen}): "))

output = password_generator(number_passwords=number_passwords, length=length)
print(output)
