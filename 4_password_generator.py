import random
import string

print("===PASSWORD GENERATOR===")
print("------------------------------------------")

try:
    length = int(input("Password length: "))
    symbol_count = int(input("Number of symbols: "))
    number_count = int(input("Number of numbers: "))

    char_count = length - symbol_count - number_count

    if length <= 0:
        print("------------------------------------------")
        print("Password length must be greater than 0.")
    elif symbol_count < 0 or number_count < 0:
        print("------------------------------------------")
        print("Symbols and numbers cannot be negative.")
    elif char_count < 0:
        print("------------------------------------------")
        print("Symbols and numbers cannot be more than the password length.")
    else:
        password_chars = []

        for i in range(char_count):
            password_chars.append(random.choice(string.ascii_letters))

        for i in range(symbol_count):
            password_chars.append(random.choice(string.punctuation))

        for i in range(number_count):
            password_chars.append(random.choice(string.digits))

        random.shuffle(password_chars)
        password = "".join(password_chars)

        print("------------------------------------------")
        print("Generated Password:")
        print(password)

    print("------------------------------------------")

except ValueError:
    print("------------------------------------------")
    print("Please enter valid numbers.")
    print("------------------------------------------")
