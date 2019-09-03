#Practice: ChickenMonkey

''' Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.

For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
For the multiples of seven (7, 14, 21, etc.) print "Monkey".
For numbers which are multiples of both five and seven print "ChickenMonkey".
To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.'''

def chicken_monkey(num):
    if num % 7 == 0 and num % 5 == 0:
        print(f"ChickenMonkey")
    elif num % 5 == 0:
        print(f"Chicken")
    elif num % 7 == 0:
        print(f"Monkey")

num_list = range(100)

for num in num_list:
    chicken_monkey(num)

import datetime


