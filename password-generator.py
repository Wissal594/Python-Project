import string
import random

while True:
    try:
        lenght = int(input("Enter length of password: "))
        if lenght <= 0:
            raise ValueError
        break
    except ValueError:
        print("❌ Invalid input! Please enter a positive number greater than 0.\n")
print(f"Generating a password with length: {lenght}")
while True :
    try:
        preference1 = input(" Do you want numbers in your password? y/n: ")

        if preference1 != "y" and preference1 !="n":
            raise ValueError
        break
    except ValueError:
        print("❌ Invalid input! Please enter n or y.\n")
while True :
    try:
        preference2 = input(" Do you want symbols in your password?")
        if preference2 != "y" and  preference2 != "n":
            raise ValueError
        break
    except ValueError:
        print("❌ Invalid input! Please enter n or y.\n")

if preference1=='y' and preference2=='n':
    character_pool = string.ascii_letters + string.digits
    password = "".join(random.choices(character_pool, k=lenght))
if preference1=='y' and preference2=='y':
    character_pool = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(character_pool,k= lenght))
if preference1=='n' and preference2=='n':
    character_pool = string.ascii_letters
    password = "".join(random.choices(character_pool, k=lenght))
if preference1=='n' and preference2=='y':
    character_pool = string.ascii_letters+string.punctuation
    password = "".join(random.choices(character_pool, k=lenght))
print(f"Your password is: {password}")





