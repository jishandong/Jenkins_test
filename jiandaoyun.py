import requests
from pyquery import PyQuery as pq
import pymysql
# res = requests.get("https://link.jiandaoyun.com/f/5cc652cc2cf3b22fb7819189")
# print(res.text)
with open("jiandaoyun.txt","r") as file:
    html = file.read()
    doc = pq(html)
    li_items = doc(".widget-wrapper")('ul > li').items()
    for index,li_item in enumerate(li_items):
        if index in [0,6,7,8,9]:
            continue
        items = li_item('.x-subhtml')('ol > li').items()
        for item in items:
            type = li_item('.label-title').text()
            url = item('a').attr('href')
            # print(item)
            info = item('span:last').text().replace("：","")
            if info is None or url is None:
                continue
            text = type+"|"+url+" |"+info
            print(text)
            # with open("199it.txt", "a", encoding="utf-8") as file:
            #     file.write(text + "\n")
            # # if url and info:
            #     print(url+"|"+info)

