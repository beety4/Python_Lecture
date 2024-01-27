import datetime
import random

class Customer:
    def __init__(self,id,gender,height,weight):
        self.id = id
        self.gender = gender
        self.height = height
        self.weight = weight
        ran_num = random.randrange(20,50)       # 20~49 사이 난수 생성
        self.payday = datetime.datetime.now() + datetime.timedelta(days=ran_num)
        

    def compute_bmi(self):
        return float(self.weight / self.height**2)


    def get_record(self):
        return f"{self.id}_{self.gender}_{self.height}_{self.weight}\n"


    def __str__(self):
        diff = datetime.datetime.now() - self.payday
        if diff.days > 30:
            opt = "미납"
        else:
            opt = "완납"

        return f"아이디: {self.id} 신장: {self.height:.2f} 체중: {self.weight:.2f} BMI: {self.compute_bmi():.2f} {opt}"
