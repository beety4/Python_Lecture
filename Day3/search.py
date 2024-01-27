from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
#options.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://naver.com")

searchLoc = driver.find_element(By.XPATH, '//*[@id="query"]')
searchLoc.send_keys("세명컴퓨터고등학교")
#searchLoc.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="sform"]/fieldset/button').click()

sleep(2)
driver.save_screenshot("result.png")
print("END")





