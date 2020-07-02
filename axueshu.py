import requests

res = requests.get("https://www.ixueshu.com/search/index.html?search_type=&q=%E5%A1%91%E5%8C%96%E5%89%82&sort=year%20desc")
print(res.text)
