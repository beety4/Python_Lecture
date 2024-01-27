from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://naver.com")
weather = driver.find_element(By.XPATH, "//*[@id='right-content-area']/div[1]/div[3]/div/div[2]/div[1]/a[1]/div[1]/div[2]").text
print(weather)
sleep(10)
driver.quit()
