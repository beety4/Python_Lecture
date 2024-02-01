class Customer:
    def __init__(self, id, gender, height, weight):
        self.id = id
        self.gender = gender
        self.height = height
        self.weight = weight


    def compute_bmi(self):
        return float(self.weight / self.height**2)

    def get_record(self):
        return f"{self.id}|{self.gender}|{self.height}|{self.weight}\n"

    def __str__(self):
        return f"이름: {self.id}, 신장: {self.height:.2f}, 체중: {self.weight}, BMI: {self.compute_bmi():.2f}"
