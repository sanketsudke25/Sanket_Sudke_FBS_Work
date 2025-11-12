class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

    def __add__(self, other):
        return Distance(
            self.km + other.km,
            self.m + other.m,
            self.cm + other.cm
        )

    def __sub__(self, other):
        return Distance(
            self.km - other.km,
            self.m - other.m,
            self.cm - other.cm
        )

    def display(self):
        print(f"{self.km}km {self.m}m {self.cm}cm")
d1 = Distance(2, 300, 40)
d2 = Distance(1, 200, 30)

d3 = d1 + d2
print("Addition:")
d3.display()

d4 = d1 - d2
print("Subtraction:")
d4.display()        