#!/usr/bin/env python3
"""yaml.dumps() expects a single argument
   performs the YAML transformation,
   and returns that as a YAML string | Alta3 Research"""
import yaml

def main():
  """runtime code"""
  hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]
  print(hitchhikers)

  yamlstring = yaml.dump(hitchhikers)
  print(yamlstring)

if __name__ == "__main__":
  main()
  