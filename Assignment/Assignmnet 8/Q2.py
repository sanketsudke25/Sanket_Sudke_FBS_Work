def circle_area(radius):
   
    area = 3.14 * radius ** 2
    return area


radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print(f"The area of the circle is: {area}")