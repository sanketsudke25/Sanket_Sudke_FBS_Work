from SYMARKS import SYMARKS
from TYMarks import TYMarks

class Student:
    def __init__(self, rollno, name, sy_marks, ty_marks):
        self.rollno = rollno
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_grade(self):
        total_computer = self.sy_marks.ComputerTotal + self.ty_marks.Theory
        if total_computer >= 70:
            return "A"
        elif total_computer >= 60:
            return "B"
        elif total_computer >= 50:
            return "C"
        elif total_computer >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display_result(self):
        print("----- Student Result -----")
        print(f"Roll No: {self.rollno}")
        print(f"Name   : {self.name}")
        print(f"SY Computer Marks : {self.sy_marks.ComputerTotal}")
        print(f"TY Theory Marks   : {self.ty_marks.Theory}")
        print(f"Total Computer Marks: {self.sy_marks.ComputerTotal + self.ty_marks.Theory}")
        print(f"Grade  : {self.calculate_grade()}")
        print("--------------------------")

sy = SYMARKS(35, 80, 75)
ty = TYMarks(40, 45)
student = Student(101, "Sanket", sy, ty)
student.display_result()