import carManage

def menu():
    print("=" * 30)
    print("1. 자동차 입고")
    print("2. 자동차 출고")
    print("3. 현재 입고 차량 현황")
    print("0. 종료")
    print("=" * 30)
    return input("> ").strip()


if __name__ == "__main__":
    carManage.readfile()

    while True:
        select = menu()
        if select == "1":
            number = input("차량번호: ").strip()
            findit = carManage.searchnumber(number)
            if findit == None:
                car_info = carManage.doin(number)
                print(f"{number} 입고 완료")
            else:
                print("이미 입고된 차량입니다.")
        elif select == "2":
            number = input("차량번호: ").strip()
            findit = carManage.searchnumber(number)
            if findit != None:
                parkingtime, price = carManage.doout(findit)
                print(f"{number} 출고 완료")
                print(f"--> 주차시간 : {parkingtime}분")
                print(f"--> 주차요금 : {price}원")
        elif select == "3":
            carManage.showcar()
        elif select == "0":
            break
