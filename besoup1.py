from bs4 import BeautifulSoup
""""
#print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(tag)
print(type(tag))

print(tag.name)
print(tag.string)
print(tag['class'])
"""

html_doc = """"
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
</body>
<html>
"""



soup = BeautifulSoup(html_doc,"lxml")

tag = soup.p
print(tag.attrs)