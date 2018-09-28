import json
import requests
import pymysql
import time
import crwal_config as config
import math

def DB(sql,type='add')->'数据库操作函数':
    db = pymysql.connect("localhost","root","123456","py",charset='utf8')
    cursor = db.cursor()

    if type =='add':
        try:
            cursor.execute(sql)
            db.commit()
            if cursor.lastrowid:
                print("保存成功")
            else:
                print("保存失败")
        except:
            db.rollback()
            print("sql错误")
            print(sql)



    db.close()




def crwalurl(url,method,pagenum)->'爬取数据函数':
    if method == 'get':
        r = requests.get(url,headers={})
        return r.text
    elif method == 'post':
        r = requests.post(url,headers={
            'Accept':config.Accept,
            'Accept-Encoding':config.Accept_Encoding,
            'Accept-Language':config.Accept_Language,
            'Connection':config.Connection,
            'Content-Length':config.Content_Length,
            'Content-Type':config.Content_Type,
            'Cookie':config.Cookie,
            'Host':config.Host,
            'Origin':config.Origin,
            'Referer':config.Referer,
            'User-Agent':config.User_Agent,
            'X-Anit-Forge-Code':config.X_Anit_Forge_Code,
            'X-Anit-Forge-Token':config.X_Anit_Forge_Token,
            'X-Requested-With':config.X_Requested_With
        },params={
            'needAddtionalResult':config.needAddtionalResult,
            'isSchoolJob':config.isSchoolJob
        },data={
            'first':True,
            'pn':pagenum,
            'kd':'python爬虫'
        })

    return r.json()


result = crwalurl(config.Request_URL,'post',1)
pagesize = result['content']['pageSize']
positionResult = result['content']['positionResult']
total_rows = positionResult['totalCount'] #总记录
#总页数
pageNum = math.ceil(total_rows/pagesize)


""""
pagesize = json_result['content']['pageSize']
hrInfoMap = json_result['content']['hrInfoMap']
positionResult = json_result['content']['positionResult']

print(hrInfoMap)
print(positionResult)
print(hrInfoMap)
print(positionResult)
print(pagesize)

hrInfoMap = result['content']['hrInfoMap']
positionResult = result['content']['positionResult']['result']

print(result['content']['hrInfoMap']['3538668']['realName'])
key = positionResult[0]['positionId']
print(key)
print(hrInfoMap[str(key)]['realName'])
a = repr("hello")+\
    ','+\
    repr("world")

print(a)
"""

def parseData(result)->'处理数据':
    pagesize = result['content']['pageSize']

    hrInfoMap = result['content']['hrInfoMap']
    positionResult = result['content']['positionResult']

    total_rows = positionResult['totalCount'] #总记录
    #总页数
    pageNum = math.ceil(total_rows/pagesize)

    sql_header = """"
    INSERT INTO lagou(
                positionName,
                businessZones,
                city,
                companyFullName,
                salary,
                workYear,
                education,
                companyShortName,
                industryField,
                financeState,
                companySize,
                companyLogo,
                district,
                createTime,
                linestation,
                positionAdvantage,
                positionLabes,
                companyId,
                hrName,
                hrImg,
                time,
                positionId
    ) VALUES(
    """
    sql = ''
    for positioninfo in positionResult['result']:

        sql = sql+',('+repr(str(positioninfo['positionName']))+\
              ','+repr(str(positioninfo['businessZones']))+\
              ','+repr(str(positioninfo['city']))+\
              ','+repr(str(positioninfo['companyFullName']))+\
              ',' + repr(str(positioninfo['salary']))+ \
              ',' + repr(str(positioninfo['workYear'])) + \
              ',' + repr(str(positioninfo['education'])) + \
              ',' + repr(str(positioninfo['companyShortName'])) + \
              ',' + repr(str(positioninfo['industryField'])) + \
              ',' + repr(str(positioninfo['financeStage'])) + \
              ',' + repr(str(positioninfo['companySize'])) + \
              ',' + repr('https://www.lagou.com/'+str(positioninfo['companyLogo'])) + \
              ',' + repr(str(positioninfo['district'])) + \
              ',' + repr(str(positioninfo['createTime'])) + \
              ',' + repr(str(positioninfo['linestaion'])) + \
              ',' + repr(str(positioninfo['positionAdvantage'])) + \
              ',' + repr(str(positioninfo['positionLables'])) + \
              ',' + repr(str(positioninfo['companyId'])) + \
              ',' + repr(str(hrInfoMap[str(positioninfo['positionId'])]['realName'])) + \
              ',' + repr('https://www.lagou.com/'+str(hrInfoMap[str(positioninfo['positionId'])]['portrait'])) + \
              ',' + repr(str(int(time.time()))) + \
              ',' + repr(str(positioninfo['positionId'])) + \
              ')'

    #print(str(sql_header)+str(sql[0:-2]))

    #for i in range(2,pageNum):

    #return sql[0:-2]
    return sql





sql = ''
sql_header = """"
    REPLACE INTO lagou(
                positionName,
                businessZones,
                city,
                companyFullName,
                salary,
                workYear,
                education,
                companyShortName,
                industryField,
                financeState,
                companySize,
                companyLogo,
                district,
                createTime,
                linestation,
                positionAdvantage,
                positionLabes,
                companyId,
                hrName,
                hrImg,
                time,
                positionId
    ) VALUES
    """

for num in range(2,pageNum):
    sql = sql + parseData(crwalurl(config.Request_URL,'post',num))
    print("正在玩命爬.....请等待")


sql = sql_header+sql[1:]

DB(sql[1:],'add')

