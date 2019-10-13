# Lab 03 - Web Scraping
import requests
from bs4 import BeautifulSoup

# --------- Part 1 ---------------
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print("---------------")
print(page.content)
soup1 = BeautifulSoup(page.content,"html.parser")
print("---------------")
print(soup1.prettify())

# ---------- Part 2 ---------------
with open("carviewer_Lab02.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# print (soup.prettify())
# print(soup.tr)

rows = soup.findAll("tr")

for row in rows:
    #print("----------")
    #print(row)
    dataList = []
    cols = row.findAll("td")
    for col in cols:
        #print(col.text)
        dataList.append(col.text)
    print(dataList)
