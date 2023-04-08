# from bs4 import BeautifulSoup
# import requests
# URL = 'https://www.moel.go.kr/info/publicdata/publicopen/list.do'
# soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
# print(soup.select('#txt>div>iframe>#document'))
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# ChromeDriver 경로 설정
driver_path = 'C:/Users/MinSeo/Downloads/chromedriver_win32/chromdriver.exe'

# ChromeDriver 실행 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

# ServiceProcess 생성
service = Service(driver_path)
# # WebDriver 생성
driver = webdriver.Chrome(service=service, options=options)
# 웹 페이지 접속
driver.get('https://www.moel.go.kr/info/publicdata/publicopen/list.do')

# iframe 요소 선택
iframe = driver.find_element(By.NAME,'frm')
# iframe 내부로 이동
driver.switch_to.frame(iframe)
# #document 요소 선택
document = driver.find_element(By.CLASS_NAME ,'container')

# #document 값 출력
print(document.text)

# iframe 바깥으로 이동
driver.switch_to.default_content()

# 웹 브라우저 종료
driver.quit()
