#!/usr/bin/env python3
# create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors
for vendor in vendors:
  print("\nThe vendor is " + vendor, end="")
  if vendor not in approved_vendors:
    print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")
