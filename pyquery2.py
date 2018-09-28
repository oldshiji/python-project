# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import requests
import time
import pymysql
import math
import random


""""
#print(pq.html())

#print(pq.find(".item_list").html())


print(userName)
print(userPic)
print(userSchool)

print(len(userName))
"""
url = 'http://www.xiaohuar.com/hua/'

def downpage(url)->'爬取网页数据':
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }).text


html_doc = downpage(url)
pq = pq(html_doc)
item_list = pq.find(".item_list")
item = item_list.find(".item")
userName = [] # 保存姓名
userPic = [] # 保存头像
userSchool = [] #保存学校
for i in item.items():
    #print(i.find(".price").text())
    userName.append(i.find(".price").text())
    userPic.append(i.find(".img").find("img").attr("src"))
    userSchool.append(i.find(".btns").text())



rows_count = pq.find(".page_num").find("a").eq(0).find("b").text() #总记录数

page_count = math.ceil(int(rows_count)/int(len(userName))) # 总页数


flip_url = "http://www.xiaohuar.com/list-1-"

all_url = []  #分页url列表　

for i in range(1,page_count):
    all_url.append(flip_url+repr(i)+'.html')




allUserName = []
allUserpic = []
allUserSchool = []
sql = ''
for pageurl in all_url:
    list_content = downpage(pageurl)
    pq1 = pq(list_content)

    # print(pq.html())

    # print(pq.find(".item_list").html())
    item_list1 = pq1.find(".item_list")

    item1 = item_list1.find(".item")

    userName1 = []  # 保存姓名
    userPic1 = []  # 保存头像
    userSchool1 = []  # 保存学校
    print("正在爬取网页")
    for j in item1.items():
        # print(i.find(".price").text())
        userName1.append(j.find(".price").text())
        userPic1.append("http://www.xiaohuar.com"+repr(j.find(".img").find("img").attr("src")))
        userSchool1.append(j.find(".btns").text())

        #文件保存路径
        temp_file = repr(time.time())+repr(int(random.random()*10000))+repr(".jpg")

        #f = open(temp_file,mode='w')
        #f.write(requests.get("http://www.xiaohuar.com"+repr(j.find(".img").find("img").attr("src"))).raw)
        #f.close()

        sql = sql+",("+repr(j.find(".price").text())+","+repr("http://www.xiaohuar.com"+j.find(".img").find("img").attr("src"))+","+repr(j.find(".btns").text())+")"
        print("正在处理数据")
        #print(userName1)

    allUserName.append(userName1)
    allUserpic.append(userPic1)
    allUserSchool.append(userSchool1)

    #print(userName1)
    #print(userSchool)


#print(sql[1:])


def DB(sql)->'数据库操作函数':
    db = pymysql.connect("localhost", "root", "123456", "py", charset='utf8')
    cursor = db.cursor()
    print("准备保存数据")
    insertsql = repr('REPLACE INTO test1(name,pic,school) VALUES'+sql[1:])
    insertsql = insertsql[1:-1]

    #print(insertsql)
    try:
        cursor.execute(insertsql)
        db.commit()
        if cursor.lastrowid:
            print("爬取成功")
        else:
            print("爬取失败")
    except:
        print("插入失败")
        print(insertsql)
        print(db.DatabaseError)
        print(db.Error)
        print(cursor.Error)
        db.rollback()

    db.close()



#DB(allUserName,allUserpic,allUserSchool)

DB(sql)