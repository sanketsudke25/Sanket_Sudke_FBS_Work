from student import Student 

class MedicalStudent(Student):
    def __init__(self, name, age, roll_number, course, specialization, internship_marks):
        super().__init__(name, age, roll_number, course)
        self.specialization = specialization
        self.internship_marks = internship_marks

    def accept(self):
        self.specialization = input("Enter specialization: ")
        self.internship_marks = float(input("Enter internship marks: "))

    def display(self):
        self.showdata() 
        print(f"Specialization       : {self.specialization}")
        print(f"Internship Marks     : {self.internship_marks}")

    

name = input("Enter name: ")
age = int(input("Enter age: "))
roll_number = input("Enter roll number: ")
course = input("Enter course: ")
specialization = input("Enter specialization: ")
internship_marks = float(input("Enter internship marks: "))

med_student = MedicalStudent(name, age, roll_number, course, specialization, internship_marks)
# med_student.accept() 
med_student.display()