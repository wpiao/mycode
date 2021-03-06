#!/usr/bin/env python3
import os
# CREATE A FUNCTION that finds the three entries that sum to 2020 and multiply them together.
# How to use this function:
# Run "wget https://static.alta3.com/courses/pyb/puzzle1.txt" to download the file in the same folder with this py file
def find_three_numbers(file_name):
  dirname = os.path.dirname(os.path.realpath(__file__))
  file_path = os.path.join(dirname, file_name)
  with open(file_path) as file:
    numbers = [line.rstrip() for line in file]
    for i in range(len(numbers) - 2):
      for j in range(i + 1, len(numbers) - 1):
        for k in range(i + 2, len(numbers)):
          if (int(numbers[i]) + int(numbers[j]) + int(numbers[k])) == 2020:
            print(int(numbers[i]) * int(numbers[j]) * int(numbers[k]))
            return

find_three_numbers("puzzle1.txt")