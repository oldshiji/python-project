import requests

import pymysql

from pyquery import PyQuery as pq

db = pymysql.connect('localhost','root','123456','zxshop')
cursor = db.cursor()



url = 'http://www.tcmap.com.cn/list/daima_list.html'

def downpage(url)->'爬取网页数据':
    r = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    })

    r.encoding = 'gbk'

    return r.text


html_doc = downpage(url)


pq = pq(html_doc)

html = pq.find("#list360")

data = html.text()

for line in data:
    print(line[:6],'=',line[6:])