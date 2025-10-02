class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    
    def show_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, student_id, name, age, marks_obtained, total_marks):  
        super().__init__(name, age)  
        self.student_id = student_id
        self.marks_obtained = marks_obtained
        self.total_marks = total_marks
        self.percentage = self.calculate_percentage()
    
    def calculate_percentage(self):
        return (self.marks_obtained / self.total_marks) * 100
    
    def show_student(self):
        print(f"Student ID: {self.student_id}")
        self.show_person()  
        print(f"Marks Obtained: {self.marks_obtained} / {self.total_marks}")
        print(f"Percentage: {self.percentage:}%")
        if (self.percentage >= 75):
            print("Result: Distinction")
        elif (self.percentage >= 60):
            print("Result: First Class")
        elif (self.percentage >= 50):
            print("Result: Second Class")
        elif (self.percentage >= 35):
            print("Result: Pass")
        else:
            print("Result: Fail")

sid = int(input("Enter the student ID: "))
name = input("Enter the student name: ")
age = int(input("Enter the student age: "))
marks_obtained = float(input("Enter total marks obtained: "))
total_marks = float(input("Enter total maximum marks: "))

s = Student(sid, name, age, marks_obtained, total_marks)
s.show_student()