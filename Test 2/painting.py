height = float(input("Enter the height of the wall: "))
width = float(input("Enter the width of the wall: "))
cost_per_sq_meter = float(input("Enter the cost of painting per square meter: "))

area_of_one_wall = height * width
total_area = 4 * area_of_one_wall     

total_cost = total_area * cost_per_sq_meter
print("Total area to paint:", total_area)
print("Total painting cost:", total_cost)
