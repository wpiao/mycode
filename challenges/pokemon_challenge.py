#!/usr/bin/env python3

import requests

def main():
  pokemon = input("Please enter a name of pokemon:  ")
  pokeapi_url = "https://pokeapi.co/api/v2/pokemon"
  pokeapi = requests.get(f"{pokeapi_url}/{pokemon}").json()
  front_default = pokeapi["sprites"]["front_default"]
  num_of_game_inceces = len(pokeapi["game_indices"])
  moves = pokeapi["moves"]
  print(f"front_default: {front_default}")
  print(f"{pokemon} has been in {num_of_game_inceces} game indices!")
  for move in moves:
    print(move["move"]["name"])

main()

