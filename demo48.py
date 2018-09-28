import requests



url = "http://www.itkucode.com:2349";

param = {
    'event_name':1,
    'to_connection_id':3,
    'content':'hello,world'
}


result = requests.get(url,params=param)

print(result.text)