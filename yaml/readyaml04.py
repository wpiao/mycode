#!/usr/bin/env python3
"""Manipulating data pulled from YAML files | Altas Research"""

import yaml

def main():
  with open("myYAML.yml", "r") as myf:
    pyyammy = yaml.load(myf)
  print(pyyammy)
  pyyammy[0]['apps'].append('minecraft')
  print(pyyammy)
  
  with open("myYAML.yml.updated", "w") as myf:
    yaml.dump(pyyammy, myf)

if __name__ == "__main__":
  main()