class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printinfo(self):
        print(f"name: {self.name}, age: {self.age}")
   
humanA = Human("侍太郎", 36)

humanA.printinfo()