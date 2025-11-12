# SY/SYMARKS.py

class SYMARKS:
    def __init__(self, computer, maths, electronics):
        self.ComputerTotal = computer
        self.MathsTotal = maths
        self.ElectronicsTotal = electronics

    def display(self):
        print("Computer Total:", self.ComputerTotal)
        print("Maths Total:", self.MathsTotal)
        print("Electronics Total:", self.ElectronicsTotal)