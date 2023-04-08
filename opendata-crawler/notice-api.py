from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from openpyxl import Workbook

# 가져온 데이터를 기반으로 엑셀 파일 생성
def writeWorkbook():
    write_wb = Workbook()
    write_ws = write_wb.create_sheet('참석자 시트')
    write_ws = write_wb.active
    for i in range(2,15):
        for j in i_list:
            people = load_ws.cell(i,j).value
            if people:
                people = removeSlash(people)
                write_ws.append(people)
    write_wb.save("excelConvert/testOutput.xlsx")   
    
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
    detail_title_area = data.find_element(By.CSS_SELECTOR ,'dl')
    title = detail_title_area.find_element(By.CSS_SELECTOR ,'dt a span.title').text
    link = detail_title_area.find_element(By.CSS_SELECTOR ,'dt a').get_attribute('href')
    info_data = data.find_elements(By.CSS_SELECTOR ,'div.info-data p')
    for info in info_data:
        print(info.find_element(By.CSS_SELECTOR ,'span.tit').text)
        try:
            print(info.find_element(By.CSS_SELECTOR ,'span.data').text)
        except:
            print(info.text.split(' ')[1].split(','))

# iframe 바깥으로 이동
driver.switch_to.default_content()

# 웹 브라우저 종료
driver.quit()
