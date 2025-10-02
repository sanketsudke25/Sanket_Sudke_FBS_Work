from student import Student  

class College:
    def __init__(self, max_students):
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"Student {student.sname} added successfully.")
        else:
            print("Cannot add student: College is at full capacity.")

    def get_student(self, roll_number):
        for student in self.students:
            if student.sroll == roll_number:
                return student
        print("Student not found.")
        return None

    def remove_student(self, roll_number):
        for student in self.students:
            if student.sroll == roll_number:
                self.students.remove(student)
                print(f"Student {student.sname} removed successfully.")
                return
        print("Student not found.")
        
college = College(2)
s1 = Student("Sanket", 22, "FRN13", "Computer Science")
s2 = Student("Aarav", 21, "FRN14", "Mechanical")

college.add_student(s1)
college.add_student(s2)

student = college.get_student("FRN13")
if student:
    student.showdata()
college.remove_student("FRN14")