#!/usr/bin/env python3

loginfail = 0

keystone_file = open("/Users/wenhaopi/Desktop/repo/amazon-sde/python/mycode/attemplogin/keystone.common.wsgi", "r")
keystone_file_lines = keystone_file.readlines()
for line in keystone_file_lines:
  if "- - - - -] Authorization failed" in line:
    loginfail += 1
print("The number of failed log in attemps is", loginfail)
keystone_file.close()