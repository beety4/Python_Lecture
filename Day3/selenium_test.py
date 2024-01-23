from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import NoSuchElementException
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://naver.com")
sleep(10)
driver.quit()
