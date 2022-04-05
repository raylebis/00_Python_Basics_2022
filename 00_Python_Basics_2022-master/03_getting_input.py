# Ask the user for their name
from doctest import OutputChecker


username = input("What is your name? ")

# Ask the user for their favourite integer
fav_num = int(input("Favourite Number? "))
# Double, halve, and square the number
double = fav_num * 2
square = fav_num * fav_num
half = fav_num / 2
print()
# Greet the user
print("Hi {}, your favourite number is {} ". format(username, fav_num))
print()
# Output the results of doubling, halving 

# and squaring their favourite number
print("double {} is {}".format(fav_num, double))
print("{} squared is {}".format(fav_num, square))
print("half {} is {}".format(fav_num, half))
print()