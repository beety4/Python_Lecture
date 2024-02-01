import os
from datetime import datetime as dt

dir_name = "C:\\1001"
datetimeformat = "%Y-%m-%d %H:%M:%S"
                # 2024-01-29 14:19:34
car_list = []

def searchnumber(number):
    for i, car in enumerate(car_list):
        if car['number'] == number:
            return i

# 문자열 -> datetime 타입
def strtotime(data):
    data = data.strip()
    return dt.strptime(data, datetimeformat)

# datetime 타입 -> 문자열
def timetostr(data):
    return dt.strftime(data, datetimeformat)

# 현재 시간 기준 몇분 주차했는지
def gettime(intime):
    return int((dt.now() - intime).total_seconds() / 60)

# 1분당 100원
def getprice(parkingtime):
    return parkingtime * 100

# 자동차 입고
def doin(number):
    car_info = {'number': number, 'intime': dt.now()}
    car_list.append(car_info)
    writefile(car_info)
    return car_info

# 자동차 출고
def doout(index):
    # 해당 차량이 몇분 주차했는지
    parkingtime = gettime(car_list[index]['intime'])
    price = getprice(parkingtime)

    deletefile(car_list[index]['number'])
    del car_list[index]

    return parkingtime, price

def showcar():
    for i, car in enumerate(car_list):
        print(f"[{i:2}] {car['number']} {timetostr(car['intime'])}")




def filename(number):
    # C:\\1001\\10가1111.txt
    return dir_name + "/" + number + ".txt"

def isfolder():
    return os.path.isdir(dir_name)

def mkfolder():
    if not isfolder():
        os.mkdir(dir_name)

def isfile(number):
    return os.path.isfile(filename(number))

def deletefile(number):
    if isfolder() and isfile(number):
        os.remove(filename(number))


def readfile():
    if isfolder():
        file_list = os.listdir(dir_name)
        for file in file_list:
            with open(dir_name + "/" + file, 'r', encoding="UTF-8") as f:
                lines = f.readlines()
                if len(lines) == 2:
                    try:
                        number = lines[0].strip()
                        intime = strtotime(lines[1])
                        carInfo = {'number': number, 'intime': intime}
                        car_list.append(carInfo)
                    except:
                        continue


def writefile(car_info):
    mkfolder()
    with open(filename(car_info['number']), 'w', encoding="UTF-8") as f:
        f.write(car_info['number'] + "\n")
        f.write(timetostr(car_info['intime']) + "\n")

