# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# Personal code begins here
password = []
for _ in range(nr_letters):
    letter = random.choice(letters)
    password.append(letter)

for _ in range(nr_symbols):
    symbol = random.choice(symbols)
    password.append(symbol)

for _ in range(nr_numbers):
    number = random.choice(numbers)
    password.append(number)

# passwordRandom = random.sample(password, len(password))
# passwordRandomString = ""
# for i in range(len(passwordRandom)):
#     passwordRandomString += passwordRandom[i]

passwordRandomString = ""
random.shuffle(password)
for i in range(len(password)):
    passwordRandomString += password[i]

print(f"Your password is: {passwordRandomString}")