from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
#options.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://news.naver.com")
driver.find_element(By.XPATH, "/html/body/section/header/div[2]/div/div/div/div/div/ul/li[8]/a/span").click()

data = {}
for i in range(1, 7):
    dPath = f"//*[@id='wrap']/div[4]/div[2]/div/div[{i}]/"
    company = driver.find_element(By.XPATH, dPath + "a/strong").text
    data[company] = []

    for j in range(1, 6):
        titlePath = dPath + f"ul/li[{j}]/div/a"
        title = driver.find_element(By.XPATH, titlePath).text
        lst = data.get(company)
        lst.append(title)

driver.quit()

for key, value in data.items():
    print(key)
    print(value)

with open("news_rank.txt", 'w', encoding="UTF-8") as f:
    for key, value in data.items():
        f.write(key + "\n")
        f.write('|'.join(value) + "\n")


