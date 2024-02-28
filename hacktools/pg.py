import string
import random
import pyperclip

while True:
    try:
        lenght = int(input("Type the desired password lenght : "))
        break
    except ValueError:
        print("Sorry, wrong value type")


chars = string.ascii_letters + string.digits + string.punctuation

result = ""

for i in range(lenght):
    result += random.choice(chars)

print(result)