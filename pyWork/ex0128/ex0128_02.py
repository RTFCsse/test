import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
url="https://www.melon.com/chart/index.htm"
res = requests.get(url,headers=headers)
print("응답 코드 : ",res.status_code())
res.raise_for_status()
print(res.text)
f = open("mel.html","W",encoding="utf-8")
f.write(res.text)