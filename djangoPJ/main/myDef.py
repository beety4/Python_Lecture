from django import forms

def test():
    return [1,2,3]

def getScore():
    score = {'국어': 88, '수학': 76, '영어': 89}
    return score

class MyForm(forms.Form):
    value = forms.CharField(label='Input your Data')

def yourName(name):
    return f"당신의 이름은 {name} 입니다."

def news(keyword):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.common import NoSuchElementException

    # 크롬 옵션 설정
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")

    # 크롬 URL로 열기
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(service=Service(executable_path='C:\\chromedriver.exe'), options=options)
    driver.get(f"https://comic.naver.com/search?keyword={keyword}")

    data = {}
    sleep(2)
    for i in range(1,30):
        try:
            dPath = f'//*[@id="content"]/div[2]/ul/li[{i}]/'
            imgLoc = driver.find_element(By.XPATH, dPath + "a/div/img")
            titleLoc = driver.find_element(By.XPATH, dPath + "div/a/span")

            img = imgLoc.get_attribute("src")
            title = titleLoc.text
            data[img] = title
        except NoSuchElementException as e:
            break

    driver.quit()
    return data

