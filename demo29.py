import requests
import json


url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-30&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=GIW&purpose_codes=ADULT"



result = requests.get(url)



#print(result.text)

r = result.json()

print(r['data']['result'])

