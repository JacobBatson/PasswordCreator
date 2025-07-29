import secrets
import string


#ADD UPPERCASE LETTERS AND MAKE SURE THAT 1 OF EACH TYPE IS IN THE PASSWORD SO 1 UPPER 1 LOWER 1 NUMBER AND 1 SPECIAL CHARACTER


def password(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    word = letters + numbers + symbols

    password = ''.join(secrets.choice(word) for i in range(length))

    print(password)


length = int(input("How long do you want the password to be "))

password(length)