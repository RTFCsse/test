import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
url="https://www.melon.com/chart/index.htm"
headers = {"User-Agent":""}
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

## 멜론 1등~100등

ranks = soup.tbody.find_all("tr")
for i, rank in ranks:
    rank_num = rank.find("span",{"class":"rank"}).get_text()
    rank_txt = rank.find("div",{"class":"ellipsis rank01"}).span.a
    print(i+1,"순위 : ",rank_txt)