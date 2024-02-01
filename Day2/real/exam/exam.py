import exam_class
import os

# Customer 객체가 저장되는 리스트
customer_list = []

# customer_list 에서 id가 같은걸 찾아내는 함수
def search_id(id):
    for cust in customer_list:
        if cust.id == id:
            return cust


# 남자 / 여자 별로 구분해서 회원 정보 출력 ( M : 남자 , F : 여자 )
def print_customer(gender):
    print("[남성]" if gender == "M" else "[여성]")
    sellist = [cust for cust in customer_list if cust.gender == gender]

    # sellist2 = []
    # for cust in customer_list:
    #     if cust.gender == gender:
    #         sellist2.append(cust)

    if not sellist:
        print("조회할 명단이 없습니다.")
    else:
        for i, cust in enumerate(sellist):
            print(f"[{i+1}] : {cust}")




# 회원정보를 저장할 파일 이름을 가져오는 함수
def get_filename():
    dir = "C:\\1002"
    fullname = dir + "\\bmiList.txt"

    if not os.path.isdir(dir):
        os.mkdir(dir)

    return fullname

# try(이름, 성별, 신장(m), 체중) 입력받고, Customer 객체로 만들어서
# customer_list 리스트에 저장
# 현재 bmi를 출력
def join_member():
    print("[회원 정보 등록]")
    id = input("이름: ")

    if search_id(id):
        print("동일한 아이디가 있습니다.")
        return

    gender = input("성별(M:남자 F:여자): ")
    if gender != "M" and gender != "F":
        print("성별이 잘못 입력되었습니다.")
        return

    try:
        height = float(input("신장(m): "))
    except:
        print("신장 입력이 잘못되었습니다.")
        return

    try:
        weight = float(input("체중(kg): "))
    except:
        print("체중 입력이 잘못되었습니다.")
        return

    cust = exam_class.Customer(id, gender, height, weight)
    customer_list.append(cust)
    print(f"현재 회원의 BMI 수치 : {cust.compute_bmi():.2f}")


# customer_list 비어있으면 "수정할 회원이 없습니다"
# 이름을 입력받아 해당 이름의 try정보(신장,체중) 변경
# bmi 출력
def edit_member():
    if not customer_list:
        print("수정할 회원정보가 없습니다.")
        return

    print("[회원 정보 수정]")
    id = input("아이디: ")
    cust = search_id(id)
    if not cust:
        print("회원정보가 없습니다.")
        return

    print(f"현재 신장: {cust.height}m")
    try:
        height = input("수정 신장(m): ")
        cust.height = float(height)
    except:
        print("신장 입력이 잘못되었습니다.")
        return

    print(f"현제 체중: {cust.weight}kg")
    try:
        weight = input("수정 체중(kg): ")
        cust.weight = float(weight)
    except:
        print("체중 입력이 잘못되었습니다.")
        return

    print(f"입력한 정보를 바탕으로 계산한 BMI 수치: {cust.compute_bmi():.2f}")


# 현재 customer_list에 있는 회원 정보를 전부 출력
# cutomer_list가 비어있다면, "출력할 정보가 없습니다."
# 마지막줄에 총 몇명의 정보가 나왔는지 출력
def view_member():
    if not customer_list:
        print("출력할 정보가 없습니다.")
        return

    print("[전체 상태 조회]")
    print("=" * 30)

    print_customer("M")
    print_customer("F")
    print("=" * 30)
    print(f"총 {len(customer_list)}명의 정보입니다.")



# 파일 입출력을 통해서 customer_list의 정보를 파일에 저장
# customer_list 비어있다면, "저장할 자료가 없습니다."
# 저장이 완료되면 총 몇명의 데이터가 파일에 저장되었는지 출력
# "3명의 데이터가 저장되었습니다."
def save_member():
    if not customer_list:
        print("저장할 자료가 없습니다.")
        return

    filename = get_filename()
    with open(filename, 'w', encoding="UTF-8") as f:
        for cust in customer_list:
            f.write(cust.get_record())

    print(f"{len(customer_list)}건의 데이터를 저장했습니다.")


# 파일 입출력을 통해서 txt파일에 있는 회원정보를 customer_list로 가져오기
# txt파일이 비어있다면 "복원할 데이터가 없습니다."
# cusmoter_list에 정보가 있다면 에러 출력
# "기존 자료와 충돌 발생이 있어, 복원할 수 없습니다."
# 복원했으면, 몇명의 데이터를 복원했는지 출력
def load_member():
    filename = get_filename()
    if not os.path.isfile(filename):
        print("복원할 데이터가 없습니다.")
        return

    if customer_list:
        print("기존 자료와 충볼이 발생하여, 복원할 수 없습니다.")
        return

    with open(filename, 'r', encoding="UTF-8") as f:
        for readdata in f:
            data = readdata.strip().split("|")
            id = data[0]
            gender = data[1]
            height = float(data[2])
            weight = float(data[3])

            cust = exam_class.Customer(id, gender, height, weight)
            customer_list.append(cust)

    print(f"{len(customer_list)}건의 데이터를 복원했습니다.")



def menu():
    print("#" * 30)
    print("A. 기존 자료 복원")
    print("B. 회원 등록")
    print("C. 정보 수정")
    print("D. 전체 조회")
    print("Q. 종료 및 회원 정보 저장")
    print("#" * 30)
    return input("> ").upper()


if __name__ == "__main__":
    load_member()
    while True:
        m = menu()

        if m == 'A':
            load_member()
        elif m == 'B':
            join_member()
        elif m == 'C':
            edit_member()
        elif m == 'D':
            view_member()
        elif m == 'Q':
            save_member()
            break

    print("프로그램을 종료합니다.")
