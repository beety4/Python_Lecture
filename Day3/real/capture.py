from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 옵션 설정
options = webdriver.ChromeOptions()
#options.add_argument("headless")

# 크롬 URL로 열기
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=Service(executable_path='../djangoPJ/main/chromedriver.exe'), options=options)
driver.get("https://naver.com")

what = input("검색어 입력 : ")

# 네이버 검색어 결과 캡처
search = driver.find_element(By.XPATH, "//*[@id=\"query\"]")
search.send_keys(what)

search.send_keys(Keys.ENTER)
#driver.find_element(By.XPATH, '//*[@id="search-btn"]').click()
sleep(2)
driver.save_screenshot("result.png")

#sleep(10)
print("END")
driver.quit()