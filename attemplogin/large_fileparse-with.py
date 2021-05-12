#!/usr/bin/env python3

loginfail = 0

with open("/Users/wenhaopi/Desktop/repo/amazon-sde/python/mycode/attemplogin/keystone.common.wsgi") as kfile:
  for line in kfile:
    if "- - - - -] Authorization failed" in line:
      loginfail += 1
print("The number of failed log in attemps is", loginfail)
