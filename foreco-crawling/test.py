import requests
from bs4 import BeautifulSoup

# 데이터를 가져올 사이트 url
url = "https://www.songpa.go.kr/www/tourListMain.do?key=5915&resrceClssCd=LV0287"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # tbody 태그 선택
    tbody = soup.find('tbody')

    # tbody 안에 있는 모든 tr 태그 선택(580개 가량) 
    tr_tags = tbody.find_all('tr')

    # 각 tr태그 안에 있는 input 태그 접근
    for tag in tr_tags:
       # input 태그 선택
        latitude = tag.find('input', {'name': 'resrceLo'})
        longtitude = tag.find('input', {'name': 'resrceLa'})
        name = tag.find('input', {'name': 'resrceAdres'})
        print(latitude['value'] ,longtitude['value'],name['value'])

else:
    print(f'Error: {response.status_code}')