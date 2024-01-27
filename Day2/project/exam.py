import exam_class
import os
customer_list = []


def search_id(id):
    for cust in customer_list:
        if cust.id == id:
            return cust

def print_customer(gender):
    print("[남성]" if gender == "M" else "[여성]")
    sellist = [cust for cust in customer_list if cust.gender == gender]
    if not sellist:
        print("조회할 명단이 없습니다.")
    else:
        for i, cust in enumerate(sellist):
            print(f"[{i+1}]", end="")
            print(cust)     # __str__() 호출
            graph = "*" * int(cust.compute_bmi())
            print(f"도표: {graph}\n")

def get_filename():
    dir = "C:\\202244016"
    fullname = dir + "\\bmilist.txt"

    if not os.path.isdir(dir):
        os.mkdir(dir)

    return fullname

        

def menu():
    print("#" * 30)
    print("A. 기존 자료 복원")
    print("B. 회원등록")
    print("C. 정보수정")
    print("D. 전체조회")
    print("Q. 종료 및 회원정보 저장")
    print("#" * 30)
    return input("> ").upper()


def join_member():
    print("[회원 정보 등록]")
    id = input("아이디: ")
    if search_id(id):
        print("동일한 아이디가 있습니다.")
        return

    gender = input("성별 (M:남자 F:여자): ")
    if gender != "M" and gender != "F":
        print("성별이 잘못 입력되었습니다.")
        return

    try:
        height = float(input("신장(m): "))
    except:
        print("신장 입력이 잘못 되었습니다.")
        return

    try:
        weight = float(input("체중(kg): "))
    except:
        print("체중 입력이 잘못 되었습니다.")
        return

    cust = exam_class.Customer(id,gender,height,weight)
    print(f"입력한 정보를 바탕으로 계산한 BMI 수치: {cust.compute_bmi():0.2f}")
    customer_list.append(cust)


def edit_member():
    if not customer_list:
        print("수정할 회원이 없습니다.")
        return
    print("[회원 정보 수정]")
    id = input("아이디: ")
    cust = search_id(id)
    if not cust:
        print("회원정보가 없습니다.")
        return

    print(f"현재 신장 : {cust.height}m")
    try:
        height = input("수정 신장(m): ")
        if height.strip():
            cust.height = float(height)
    except:
        print("신장 입력이 잘못되었습니다.")
        return

    try:
        print(f"현재 체중 : {cust.weight}kg")
        weight = input("수정 체중(kg): ")
        if weight.strip():
            cust.weight = float(weight)
    except:
        print("체중 입력이 잘못되었습니다.")
        return

    print(f"입력한 정보를 바탕으로 계산한 BMI 수치: {cust.compute_bmi():.2f}")


def view_member():
    if not customer_list:
        print("상태를 보여줄 회원이 없습니다.")
        return

    print("[전체 상태 조회]")
    print("=" * 30)

    print_customer("M")
    print_customer("F")
    print("=" * 30)
    print(f"총 {len(customer_list)}명의 정보입니다.")


def save_member():
    if not customer_list:
        print("저장할 자료가 없습니다.")
        return

    filename = get_filename()
    #with open(filename, "w", encoding="cp949") as f:
    with open(filename, "w", encoding="UTF-8") as f:
        for cust in customer_list:
            f.write(cust.get_record())
    print(f"{len(customer_list)}건의 데이터를 저장했습니다.")


def load_member():
    filename = get_filename()
    if not os.path.isfile(filename):
        print("복원할 데이터가 없습니다.")
        return

    if customer_list:
        print("기존 자료와 충돌 발생 있어서, 복원할 수 없습니다.")
        return

    with open(filename, "r", encoding="UTF-8") as f:
        for readdata in f:  # while + readline() 대신 사용 가능
            data = readdata.strip().split("_")
            if len(data) == 4:
                id = data[0]
                gender = data[1]
                height = float(data[2])
                weight = float(data[3])
                cust = exam_class.Customer(id,gender,height,weight)
                customer_list.append(cust)

    print(f"{len(customer_list)}건의 데이터를 복원했습니다.")

def mydef():
    for cust in customer_list:
        print(cust)
        print(cust.id)

if __name__ == '__main__':
    while True:
        sel = menu()

        if sel == 'A':
            load_member()
        elif sel == 'B':
            join_member()
        elif sel == 'C':
            edit_member()
        elif sel == 'D':
            view_member()
        elif sel == 'Q':
            save_member()
            break
        elif sel == 'P':
            mydef()

    print("프로그램을 종료합니다.")
