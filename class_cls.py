class Student:
    count = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    def get_info(self):
        print(f"This is {self.name}")

    @classmethod
    def get_count(cls):
        print(Student.count)

student1 = Student("Jorge", 2.0)

Student.get_count()