class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"
class StudentBad:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
good_student = Student("Ali",85)
bad_student = Student("Sara", 92)
print("With __str__:")
print(good_student)

print("\nWithout __str__:")
print(bad_student)