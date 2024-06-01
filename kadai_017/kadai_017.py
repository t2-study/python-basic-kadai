class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は、大人です")
        else:
            print(f"{self.name}は、大人ではありません")

human_A = Human("一郎", 25)
human_B = Human("次郎", 20)
human_C = Human("三郎", 15)

human_info = [human_A, human_B, human_C]

for human in human_info:
    human.check_adult()
