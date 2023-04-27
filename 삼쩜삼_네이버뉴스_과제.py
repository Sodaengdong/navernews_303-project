import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

#검색어 입력
search = input('검색어를 입력해주세요 : ')

#데이터프레임 내 header(변수명) 생성
sheet.append(["검색어명", "뉴스 제목", "URL"])

#1~2페이지까지 수집(20개)
for p in range(1, 12, 10): 
    page = p
    print(page)
    raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&sort=1&query={s}&start={page}".format(s = search, page = page))
    html = BeautifulSoup(raw.text, 'html.parser')

    container = html.select("div.news_area")

    for con in container:
        title = con.select_one("div.news_area > a.news_tit")['title']
        url = con.select_one("div.news_area > a.news_tit")['href']

        sheet.append([search, title, url])

wb.save("navernews_삼쩜삼.csv")