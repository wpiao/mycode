#!/usr/bin/env python3
"""yaml.load() expects a single file and
   converts the YAML to pythonic data | Alta3 Research"""

import yaml

def main():
  """runtime code"""
  with open("myYAML.yml", "r") as yf:
    pyyammy = yaml.load(yf)
  print(pyyammy)

if __name__ == "__main__":
  main()
