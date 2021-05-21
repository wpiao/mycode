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
            price, change = texts[0], texts[1]
        else:
            price, change = [], []

        texts = web_content_div(
            web_content, 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
        if texts != []:
            for count, volume in enumerate(texts):
                if volume == 'Volume':
                    volume = texts[count + 1]
        else:
            volume = []

        texts = web_content_div(
            web_content, 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)')
        if texts != []:
            for count, target in enumerate(texts):
                if target == '1y Target Est':
                    one_year_target = texts[count + 1]
        else:
            one_year_target = []

    except ConnectionError:
        price, change, volume, one_year_target = [], [], [], []
    return price, change, volume, one_year_target


stock = ['AAPL', 'AMZN', 'MSFT']
# print(real_time_price(stock[0]))

while(True):
    info = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
    for stock_code in stock:
        stock_price, change, volume, one_year_target = real_time_price(
            stock_code)
        info.append(stock_price)
        info.extend([change])
        info.extend([volume])
        info.extend([one_year_target])
    col = [time_stamp]
    col.extend(info)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv(str(time_stamp[0:11]) + 'stock_data.csv', mode='a', header=False)
    print(col)
