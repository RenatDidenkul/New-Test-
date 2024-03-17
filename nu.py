class Student:
    print("hello")
    def __init__(self, name, mony , htight):
        self.name = name
        self.mony = mony
        self.height = htight
        self.mony = 100
        self.height = 160
        print("init")
    def BuyPizza(self):
        self.mony -= 100
        print(self.name, "ты купил пиццу", self.mony, "uah")
       
       
class Car :
    def __init__(self):
        self.color = "black"
        self.model = "Tesla"
 
       
       
       
       
       
   
s = Student('Alex', 200, 180)
s2 = Student("stepan", 300 , 180)
car = Car()
print(car.color , car.model)
s.mony = 200
print(s.name ,s.mony,s2.name , s2.mony)
s.BuyPizza()