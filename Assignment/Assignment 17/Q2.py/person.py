class Person:
    def __init__(self,name,age,address):
        self.pname = name
        self.page = age
        self.paddress = address

    def showdata(self):
        print(f"name:{self.pname}, \nage :{self.page} \nadd: {self.paddress}")
   
# p = Person("sanket", 22, "pusad")
# p.showdata()  
