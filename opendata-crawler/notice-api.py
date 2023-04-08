from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ChromeDriver 경로 설정
DRIVER_PATH = 'C:/Users/MinSeo/Downloads/chromedriver_win32/chromdriver.exe'
URL = 'https://www.moel.go.kr/info/publicdata/publicopen/list.do'
# ChromeDriver 실행 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
# ServiceProcess 생성
service = Service(DRIVER_PATH)
# WebDriver 생성
driver = webdriver.Chrome(service=service, options=options)

# 웹 페이지 접속
driver.get(URL)

# iframe 요소 선택
iframe = driver.find_element(By.NAME,'frm')
# iframe 내부로 이동
driver.switch_to.frame(iframe)
# 정보 요소 가져오기
element = driver.find_element(By.CSS_SELECTOR ,'#fileDataList div.result-list ul')
#list로 가져오기
data_list = element.find_elements(By.TAG_NAME , 'li')
for data in data_list:
    print(data.find_element(By.CSS_SELECTOR ,'span.data').text)

# iframe 바깥으로 이동
driver.switch_to.default_content()

# 웹 브라우저 종료
driver.quit()
