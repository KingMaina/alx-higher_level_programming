#!/usr/bin/python3
def fizzbuzz():
    for number in range(1,101):
        if number % 15:
            print("FizzBuzz", end=" ")
        elif number % 3:
            print("Fizz", end=" ")
        elif number % 5:
            print("Buzz", end=" ")
		else
            print(number, end=" ")
