import urllib.request
import urllib.parse
from pyquery import PyQuery as pq
import requests
import ssl
import json
import random
import collections
import threading
import time
import proxy
from multiprocessing import Process,Queue
from model import db
import psutil
import config
import http.cookiejar
import proxy_spider
def get(url):
    '''headerList = config.ua

    context = ssl._create_unverified_context()
    if proxy != None:
        req = urllib.request.Request(url, headers=headers)
    else:
        headers = {
            "User-Agent": headerList[random.randint(0, len(headerList) - 1)]
        }
        req = urllib.request.Request(url, headers=headers)
    cj = http.cookiejar.CookieJar()

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    response = opener.open(req)


    #response = urllib.request.urlopen(req,context=context)
    #print(response.)'''
    #url,cookie,type,data
    cookie = None
    if cookie:
        result = proxy_spider.yiniu_proxy(url, cookie,'get','')
        cookie = result['cookie']
        context = result['text']
    else:
        result = proxy_spider.yiniu_proxy(url, None, 'get', '')
        cookie = result['cookie']
        context = result['text']

    return context

def getcity():
    cityList = list()
    citycode = dict()

    url = "https://www.zhipin.com/common/data/city.json"
    result = get(url)
    result = json.loads(result)
    for item in result['data']['hotCityList']:
        citycode[item['name']] = item['code']
        cityList.append(citycode)
        '''
                if len(item['subLevelModelList']):
            for childItem in item['subLevelModelList']:
                citycode[childItem['name']] = childItem['code']
                cityList.append(citycode)
        '''



    return citycode

def getposition():
    positionList = list()
    positionCode = dict()

    url = "https://www.zhipin.com/common/data/position.json"
    result = get(url)
    result = json.loads(result)
    for item in result['data']:
        for child1 in item['subLevelModelList']:
            for child2 in child1['subLevelModelList']:
                #print(child2['code'],'=',child2['name'])
                positionCode[child2['name']] = child2['code']

    return positionCode

def getjobList(url,q):
    d = collections.deque()
    #进队　
    d.append(url)
    baseurl = "https://www.zhipin.com"
    pageLink = list()
    #保存职位数据
    positionObj = dict()
    positionList = list()

    while len(d)>0:
        #出队
        position_url = d.popleft()
        #当前页面的列表页

        result = get(position_url)

        doc = pq(result)
        details_url = doc(".job-list ul li a").items()
        #翻页链接
        page = doc(".page a").items()
        for item in details_url:
            #print(item.attr.href)
            #详情页
            linkurl = baseurl+item.attr.href
            time.sleep(1)
            details = pq(get(linkurl))



            job_name = details(".info-primary h1")#职位名称
            publish_time = details(".info-primary .time")#职位发布时间
            salary = details(".info-primary .badge")
            city_exprience_address = details(".info-primary p")#城市－经验－地址
            job_tags = details(".info-primary .job-tags")
            company_logo = details(".info-company a")
            company_shortname = details(".info-company h3")
            is_fanc = details(".info-company p").eq(0)
            company_website = details(".info-company p").eq(1)
            hr_headimg = details(".detail-figure img")
            hr_name = details(".job-detail h2.name")
            hr_position = details(".job-detail gray")
            position_desc = details(".detail-content .text")
            company_desc = details(".job-sec.company-info")

            company_name = details(".job-sec .name")
            boss = details(".job-sec .level-list li").eq(0)
            reg_money = details(".job-sec .level-list li").eq(1)
            reg_time = details(".job-sec .level-list li").eq(2)
            company_type = details(".job-sec .level-list li").eq(3)
            company_status = details(".job-sec .level-list li").eq(4)

            if job_name.text():
                positionObj['job_name'] = job_name.text()
                positionObj['publish_time'] = publish_time.text()
                positionObj['city_exp_edu'] = city_exprience_address.text()
                positionObj['job_tags'] = job_tags.text()
                positionObj['company_logo'] = company_logo.attr.href
                positionObj['company_shortname'] = company_shortname.text()
                positionObj['fancing_scale'] = is_fanc.text()
                positionObj['company_website'] = company_website.text()
                positionObj['hr_heading'] = hr_headimg.attr.src
                positionObj['hr_name'] = hr_name.text()
                positionObj['hr_position'] = hr_position.text()
                positionObj['position_desc'] = position_desc.text()
                positionObj['company_desc'] = company_desc.text()
                positionObj['company_name'] = company_name.text()
                positionObj['boss'] = boss.text()
                positionObj['job_address'] = details(".location-address").text()

                #print(positionObj)
                q.put(positionObj)
                time.sleep(2)
            #详情页面的数据处理完以后，将当前爬取的分页放入　列队：如page1,page2,page3,page4 当爬第２页时也会得到相同的页码
            #会导致数据重复爬取，所以要采用集合数据类型处理，防止数据重复


        #将页码链接放入列队里，并做数据清重处理
        for link in page:
            if ':' not in link.attr.href:
                fulllink = baseurl + link.attr.href
                pageLink.append(fulllink)


        pageLink = list(set(pageLink))
        #print(pageLink)
        for link in pageLink:
            d.append(link)







def run(q):
    # 城市－职位－城市－页码
    # 城市－对应多个职位
    # 城市－多个职位－页码
    # 北京－python-1 北京－python-2
    cityList = getcity()
    positionList = getposition()
    positionUrl = list()
    url = 'https://www.zhipin.com/c{city}-p{position}/h_{city}/?page={p}&ka=page-{p}'
    for city in cityList.keys():
        for position in positionList.keys():
            positionUrl.append('https://www.zhipin.com/c{city}-p{position}/h_{city}/?page={p}&ka=page-{p}'.format(
                city=cityList.get(city), position=positionList.get(position), p=1))


    # print(len(positionUrl))
    for url in positionUrl:
        getjobList(url,q)


def saveSpider(q):
    model = db.Model()
    while True:
        positionObj = q.get()
        if positionObj:
            #job_name, hr_name, company_name
           existsJob = model.table("bossjob").find({
               "job_name":positionObj['job_name'],
               "hr_name":positionObj['hr_name'],
               "company_name":positionObj['company_name'],
           })

           if len(existsJob)>0:
               pass
           else:
               model.table("bossjob").save(positionObj)
               print(positionObj)




if __name__=='__main__':
    #url = "https://www.zhipin.com/c101190400-p100109/h_101190400/?page=8&ka=page-8"
    #getjobList(url)

    #print(get("https://blog.csdn.net/qq_34352010/article/details/51890122"))
    print("主进程启动.....")
    q = Queue()
    # 爬进程启动
    spider = Process(target=run, args=(q,))

    # 数据保存进程启动
    savespider = Process(target=saveSpider, args=(q,))

    spider.start()
    pp1 = psutil.Process(spider.pid)
    print(pp1.name())
    print(pp1.status())
    savespider.start()
    spider.join()
    savespider.join()


