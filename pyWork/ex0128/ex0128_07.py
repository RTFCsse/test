import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=769209&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


total_num=0
for cartoon in cartoons:
    try:
        c_title = cartoon.find("td",{"class":"title"}).a.get_text()
        c_num = cartoon.find("div",{"class":"rating_type"}).strong
        total_num += float(c_num)
        count += 1
        print("제목 : {},평점 : {}".format(c_title.c_num))
        
    except:
        pass
    print("전체 점수 : ",round(total_num,2))
    print("평균 점수 : ",round(total_num/count,2))