#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for i in range(nr_letters):
  random_letters = random.sample(letters, nr_letters)
  join_letters = "".join(random_letters)

for i in range(nr_symbols):
  random_symbols = random.sample(symbols, nr_symbols)
  join_symbols = "".join(random_symbols)

for i in range(nr_numbers):
  random_numbers = random.sample(numbers, nr_numbers)
  join_numbers = "".join(random_numbers)

easy_password = join_letters + join_symbols + join_numbers

print(easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

from random import sample 

password_list = random_letters + random_symbols + random_numbers

hard_password = sample(password_list, len(password_list))
hard_password = "".join(hard_password)

print(hard_password) 