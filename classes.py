class DatabaseConnection:
    # pass
    ...  # Ellipsis is used same as pass.

class Student:
    princpal = "Dr. Smith"
    student_count = 0

    def __new__(cls, *args, **kwargs):
        # mail constructor function runs before __init__ and is responsible for creating a new instance of the class. It takes the class itself as the first parameter (cls) and can also take additional arguments (*args and **kwargs) that are passed to the __init__ method.
        print("Creating a new instance of Student")
        instance = super(Student, cls).__new__(cls)
        return instance
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

        Student.student_count += 1

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def __reveal(self):
        return "This is a private method"
    
    _protected_method = __reveal

    # _ = protected and __ private
    
    @classmethod
    # shared resource across all instances of the class, takes cls as the first parameter
    # cls method can modify class state that applies across all instances of the class, it can also be called on the class itself, rather than on instances of the class.
    def update_principal(cls, new_principal):
        cls.princpal = new_principal

    @staticmethod
    # regular function without self or cls
    def is_student_adult(age):
        return age >= 18;


# Student.update_principal("Dr. Johnson")

# std = Student("anurag", 25)
# std.display_info()
# # std.update_principal("Dr. Johnson fro std")
# print(std.princpal)
# print(std.student_count)
# print(std.is_student_adult(std.age))
# # print(std.__reveal())
# print(std._protected_method())

# std5 = Student("john", 22)
# print(std5.student_count)


class Employees:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # protected variable
    
    # the name of the getter method and the setter method must be exactly the same.
    # setter and getter function use as varible - @property transforms a method so that it behaves exactly like a normal variable when you access it from outside the class. 
    # ->  - Function Return Type Hints - It explicitly indicates what data type a function will return after it finishes executing.

    # 1. THE GETTER: Marked with @property
    @property
    def salary(self) -> float:
        print("Salary details")
        return self._salary
    
    # 2. THE SETTER: Marked with @<property_name>.setter
    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError('Salary cannot be negative')
        
        self._salary = value

EMP = Employees("Alice", 50000)
print(EMP.salary)  # Uses the getter
EMP.salary = 60000  # Uses the setter
# EMP.salary = -60000  # Uses the setter
print(EMP.salary)  # Uses the getter
