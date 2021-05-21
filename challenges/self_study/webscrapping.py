#!/usr/bin/env python3
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class': class_path})
    try:
        spans = web_content_div[0].find_all('span')
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts = []
    return texts


def real_time_price(stock_code):
    url = f'https://finance.yahoo.com/quote/{stock_code}?p={stock_code}&.tsrc=fin-srch'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')  # use lxml parser
        texts = web_content_div(
            web_content, 'My(6px) Pos(r) smartphone_Mt(6px)')
        if texts != []:
            price = texts[0]
            change = texts[1]
    except ConnectionError:
        price = []
        change = []
    return price, change


print(real_time_price('AAPL'))
