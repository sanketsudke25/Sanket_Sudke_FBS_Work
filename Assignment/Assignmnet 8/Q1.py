def area(length, width):
   
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = area(length, width)
print(f"The area of the rectangle is: {area}")
area(length, width)