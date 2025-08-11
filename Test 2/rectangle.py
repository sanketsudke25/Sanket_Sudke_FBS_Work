radius = 20
length = 50
breadth = 40
cost_per_meter = 35
rounds = 5

half_circle_perimeter = 3.14 * radius
rectangle_perimeter = 2 * (length + breadth)
total_fencing_length = half_circle_perimeter + rectangle_perimeter
total_wire_length = total_fencing_length * rounds
total_cost = total_wire_length * cost_per_meter

print("total fencing the field", round(total_cost))
