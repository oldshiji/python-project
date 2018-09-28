
import pycurl;
import time;

class Test:
    def __init__(self):
        self.content = ""
    def setcontent(self,buf):
        self.content = buf

        

curl = pycurl.Curl();
start = time.time()
t = Test();
#url = "http://www.app.com/app/py1.php"
url = "http://blog.csdn.net/gdp12315_gu/article/details/47314175"
curl.setopt(curl.URL,url);
curl.setopt(curl.WRITEFUNCTION,t.setcontent);
curl.perform()
end = time.time()
#print('cost time'+end-start+"seconed")
print(curl.getinfo(curl.HTTP_CODE))
response = "请求返回的内容是：";

f = open("response.html",mode='w',encoding='utf-8');

f.write(t.content.decode('utf-8'));

f.close();

