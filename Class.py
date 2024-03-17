class Student:
    def __init__(self, name, age, year, grade):
        self.name = name
        self.age = age
        self.year = year
        self.grade = grade

    def get_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Курс: {self.year}, Середній бал: {self.grade}")

    def increase_year(self):
        self.year += 1

    def update_grade(self, new_grade):
        self.grade = (self.grade + new_grade) / 2

student1 = Student("Артем", 21, 2, 88)
student1.get_info() 
student1.increase_year()
student1.get_info() 

student1.update_grade(90)
student1.get_info()  

student2 = Student("Даніїл", 23, 2, 78)
student2.get_info() 