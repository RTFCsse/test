import requests
from bs4 import BeautifulSoup

url="https://shoppinghow.kakao.com/siso/p/bestRank/"
res = requests.get(url)
res.raise_for_status()
print("응답 코드 : ",res.status_code)

soup = BeautifulSoup(res.text,"lxml")
print("")
print("")
print("")

soup.fund("")

f = open("test1.html",)