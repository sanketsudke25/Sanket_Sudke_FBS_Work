from person import Person

class EnggStudent(Person):
    def __init__(self, name, age, address, student_id, marks_obtained, total_marks, branch, internal_marks):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.marks_obtained = marks_obtained
        self.total_marks = total_marks
        self.branch = branch
        self.internal_marks = internal_marks

    def accept(self):
        self.branch = input("Enter branch: ")
        self.internal_marks = float(input("Enter internal marks: "))

    def display(self):
        self.showdata()  
        print(f"Student ID     : {self.student_id}")
        print(f"Marks Obtained : {self.marks_obtained}")
        print(f"Total Marks    : {self.total_marks}")
        print(f"Branch         : {self.branch}")
        print(f"Internal Marks : {self.internal_marks}")

name = input("Enter the student name: ")
age = int(input("Enter the student age: "))
address = input("Enter the student address: ")
student_id = int(input("Enter the student ID: "))
marks_obtained = float(input("Enter total marks obtained: "))
total_marks = float(input("Enter total maximum marks: "))
branch = input("Enter branch: ")
internal_marks = float(input("Enter internal marks: "))

engg_student = EnggStudent(name, age, address, student_id, marks_obtained, total_marks, branch, internal_marks)
engg_student.accept()
engg_student.display()