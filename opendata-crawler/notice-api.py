from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from openpyxl import Workbook

#TODO:excel에 데이터 저장
# 가져온 데이터를 기반으로 엑셀 파일 생성
def writeWorkbook(i,j):
    write_wb = Workbook()
    write_ws = write_wb.create_sheet('참석자 시트')
    write_ws = write_wb.active
    # for j in i_list:
    #     write_ws.append(people)
    write_wb.save("./testOutput.xlsx")   
    
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

# pagination 적용


# 정보 요소 가져오기
for page in range(1,19):
    element = driver.find_element(By.CSS_SELECTOR ,'#fileDataList div.result-list ul')
    #list로 가져오기
    data_list = element.find_elements(By.TAG_NAME , 'li')
    for data in data_list:
        detail_title_area = data.find_element(By.CSS_SELECTOR ,'dl')
        title = detail_title_area.find_element(By.CSS_SELECTOR ,'dt a span.title').text

        # display 속성을 변경하여 화면에 표시되도록 만듦
        # @media 태그로 인해서 바로 수정되지않아, viewport 크기를 변경함으로써
        # 수정될수있도록 함
        driver.execute_script(
            "Object.defineProperty(window, 'innerWidth', {value: 1025, configurable: true});var dd_list = document.querySelectorAll('.data-set-list .result-list ul li dl dd');for (var i = 0; i < dd_list.length; i++) {dd_list[i].style.display = 'block';}")
        details = detail_title_area.find_elements(By.TAG_NAME ,"dd")
        link = detail_title_area.find_element(By.CSS_SELECTOR ,'dt a').get_attribute('href')
        for detail in details:
            print(detail.text)
        
        info_data = data.find_elements(By.CSS_SELECTOR ,'div.info-data p')
        for info in info_data:
            print(info.find_element(By.CSS_SELECTOR ,'span.tit').text)
            try:
                print(info.find_element(By.CSS_SELECTOR ,'span.data').text)
            except:
                print(info.text.split(' ')[1].split(','))
        driver.execute_script(
            "$('#search-form-current-page').val(arguments[0]);",page
        )
# iframe 바깥으로 이동
driver.switch_to.default_content()

# 웹 브라우저 종료
driver.quit()

