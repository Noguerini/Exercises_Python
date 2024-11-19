class Car:

    wheels = 4

    def __init__(self, model, year, color, forSale):
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale

    def drive(self):
        print(f"This {self.model} is driving")


car_1 = Car("BMW M3", 2024, "Red", True)

print(car_1.color)
car_1.drive()

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        num_students += 1


student_1 = Student("Jorge", 22)
student_2 = Student("Marín", 22)

print(Student.class_year)
print(Student.num_students)

class Animal:
    def __init__(self, name, isAlive):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak():
        print("WOOF")

