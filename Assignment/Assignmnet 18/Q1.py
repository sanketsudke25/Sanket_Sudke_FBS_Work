class Complex_Number:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __del__(self):
        print('destructor called')

    def __add__(self,other):    
        return Complex_Number(self.real + other.real,self.imag + other.imag) 
    def __sub__(self, other):
        return Complex_Number(self.real - other.real, self.imag - other.imag)

    def display(self):
        print(f"{self.real} + {self.imag}")

c1 = Complex_Number(10, 3)
c2 = Complex_Number(8, 4)

c3 = c1 + c2
c4 = c1 - c2

c3.display() 
c4.display()


