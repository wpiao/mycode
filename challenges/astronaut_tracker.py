#!/usr/bin/env python3

from requests import get

def main():
  response = get("http://api.open-notify.org/astros.json").json()
  print(f"People in Space: {response['number']}")
  people = response['people']
  for astronaut in people:
    print(f"{astronaut['name']} is on the {astronaut['craft']}.")

if __name__ == "__main__":
  main()
