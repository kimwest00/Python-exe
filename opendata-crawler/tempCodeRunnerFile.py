# iframe 내부로 이동
driver.switch_to.frame(iframe)
# #document 요소 선택
document = driver.find_element(By.ID ,'#document')

# #document 값 출력
print(document.text)

# iframe 바깥으로 이동
driver.switch_to.default_content()