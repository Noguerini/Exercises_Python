class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["crew", "pilot", "mechanic"]
        return position in valid_positions
    
print(Employee.is_valid_position("crew"))


employee_1 = Employee("Jorge", "crew")