import secrets
import string

def password(length):
    letters = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    upper = string.ascii_uppercase

    word = letters + numbers + symbols + upper

    password = ''.join(secrets.choice(word) for i in range(length))

    print(password)


length = int(input("How long do you want the password to be "))

password(length)