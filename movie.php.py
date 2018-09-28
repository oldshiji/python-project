import requests

url = "http://aaxxy.com/vod-play-id-1621-src-3-num-1.html"

header = {

}

data = {
}

result = requests.get(url)

content = result.text
print(content)