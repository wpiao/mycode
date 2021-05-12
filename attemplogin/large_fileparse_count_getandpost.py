#!/usr/bin/env python3

get = 0
post = 0

with open("/Users/wenhaopi/Desktop/repo/amazon-sde/python/mycode/attemplogin/keystone.common.wsgi") as kfile:
  for line in kfile:
    if "POST" in line:
      post += 1
    elif "GET" in line:
      get += 1
print(f"There are {post} POST requests and {get} GET requests!")