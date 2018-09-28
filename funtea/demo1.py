import requests
import time


url = "http://www.liketea.com/index.php/api/Goods/collectGoodsOrNo"

param = {}
header = {}
sign = repr('100')+repr(time.time())+repr('123456')
data = {
    'sign':'123456',
    'time':int(time.time()),
    'goods_id':100,

result = requests.post(url,data=data)

print(result.text)