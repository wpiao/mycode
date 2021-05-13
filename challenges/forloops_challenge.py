#!/usr/bin/env python3

def construct_pattern(size):
  for i in range(1, size + 1):
    print("* " * i)
  for i in range(size - 1, 0, -1):
    print("* " * i)

construct_pattern(6)