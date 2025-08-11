p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
p4 = float(input("Enter price of product 4: "))
p5 = float(input("Enter price of product 5: "))


total_price = p1 + p2 + p3 + p4 + p5


gst = total_price * 0.18
total_bill = total_price + gst


print(f"Total price before GST: {total_price:}")
print(f"GST ({18}%): {gst:}")
print(f"Total bill after adding {18}% GST:{total_bill:}")
