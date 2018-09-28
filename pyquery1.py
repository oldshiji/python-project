from pyquery import PyQuery as pq

doc = pq(filename='pyquery1.html')



""""
print(doc.html())
print("\n")

print(doc(".item-0"))
print(doc("tr"))
data = doc("tr")

for tr in data.items():
    print(tr("td").eq(1).text())
"""

print(doc("tr").eq(1).find("td").eq(1).html())