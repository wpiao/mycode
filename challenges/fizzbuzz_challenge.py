#!/usr/bin/env python3

def fizzbuzz(min, max):
  for i in range(min, max + 1):
    if (i % 3 == 0 and i % 5 == 0):
      print("FizzBuzz")
    elif (i % 3 == 0):
      print("Fizz")
    elif (i % 5 == 0):
      print("Buzz")
    else:
      print(i)

fizzbuzz(1, 100)
