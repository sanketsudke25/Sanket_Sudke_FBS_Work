class Student:
    def __init__(self, name, age, roll_number, course):
        self.sname = name
        self.sage = age
        self.sroll = roll_number
        self.scourse = course

    def showdata(self):
        print(f"name : {self.sname},")
        print(f"age  : {self.sage}")
        print(f"roll : {self.sroll}")
        print(f"course : {self.scourse}")

# s = Student("sanket", 22, "FRN13", "Computer Science")
# s.showdata()