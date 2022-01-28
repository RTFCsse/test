import requests

##정보요청
#res = requests.get("https://www.naver.com/")
url="https://www.melon.com/chart/index.htm"
res = requests.get(url)
res.raise_for_status() #에러코드이면 프로그램 종료

#print("응답코드 : ", res.status_code)

if res.status_code == requests.codes.ok:
    print("정상출력")
else:
    print("비정상줄력")

