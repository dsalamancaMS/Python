class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


# class name_of_child(name_of_parent_class)
# super is for inheretance 

class Employee(Person):
    def __init__(self,employee_name,employee_last_name, employee_id):
        super().__init__(name=employee_name, last_name=employee_last_name)
        self.id = id

employee_1 = Employee('John','Doe', 1)

