
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))

rectangle_area = length * breadth
rectangle_perimeter = 2 * (length + breadth)

circle_area =length * radius ** 2
circle_perimeter = 2 * length * radius


print(f'Area: {rectangle_area:}')
print(f'Perimeter: {rectangle_perimeter:}')


print(f'Area: {circle_area:}')
print(f'Perimeter (Circumference): {circle_perimeter:}') 


