class Student:
    def __init__ (self,name,roll_no,age=None,marks=None):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.marks = marks
    def set_age (self,age):
        self.age = age
    def set_marks(self,marks):
        self.marks = marks

    def display(self):
        print(f"Name:{self.name},Roll_no:{self.roll_no},age:{self.age},Marks = {self.marks}")

S1 = Student("Saqib",2639)
S1.set_age(18)
S1.set_marks(844)
S1.display()

