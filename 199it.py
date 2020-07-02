import requests
from pyquery import PyQuery as pq
import pymysql

db = pymysql.connect(host='rdsu41uutacn4ssbirh9public.mysql.rds.aliyuncs.com', user='wukai', password='Fsnip_db_1544',
                         port=3306, db='datav')

def insert_db(type,url):
    cursor = db.cursor()
    sql = 'INSERT INTO website_url (type1,url)VALUES("{type}","{url}");'.format(type=type,url=url)
    cursor.execute(sql)
    cursor.connection.commit()
    cursor.close()


def get_more_url():
    more_url = []
    res = requests.get("https://hao.199it.com/")
    doc = pq(res.text)
    _items = doc('.list')('.item').items()
    for item in _items:
        href = item('a').attr('href')
        more_url.append("https://hao.199it.com/" + href)
    return more_url

def main(url):
    detail_res = requests.get(url)
    detail_res.encoding = 'utf8'
    detail_doc = pq(detail_res.text)
    type = detail_doc('.location-item')('a:last').html()
    # common_items = detail_doc('.common-item').items()
    li_items = detail_doc('.common-item:first')('.js-MBclearfix-floatl').items()
    count = 0
    for li_item in li_items:
        url = li_item('.hx')('a').attr('href')
        info = li_item('.hx')('a').text()
        text = type+"|"+url + "|"+info
        save_file(text)
        count += 1

    print(count)
def save_file(text):
    with open("199it.txt", "a", encoding="utf-8") as file:
        file.write(text+"\n")



if __name__ == '__main__':
    urls = get_more_url()
    print(urls)
    for url in urls:
        main(url)
    # print(get_more_url())

    db.close()
