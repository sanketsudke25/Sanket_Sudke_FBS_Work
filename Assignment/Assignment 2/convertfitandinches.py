feet = int(input("enter the value  :"))
inches = int(input("enter the value :"))
FEET_TO_METERS = 0.3048
INCH_TO_METERS = 0.0254
total_meters = (feet * FEET_TO_METERS) + (inches * INCH_TO_METERS)
meters = int(total_meters)
centimeters = (total_meters - meters) * 100
print(f"{meters} meters and {centimeters:} centimeters")
