#!/usr/bin/env python3

loginfail = 0

keystone_file = open("/Users/wenhaopi/Desktop/repo/amazon-sde/python/mycode/attemplogin/keystone.common.wsgi", "r")
for line in keystone_file:
  if "- - - - -] Authorization failed" in line:
    loginfail += 1
print("The number of failed log in attemps is", loginfail)
keystone_file.close()