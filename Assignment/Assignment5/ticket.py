
passengers = int(input("Enter number of passengers: "))
ticket = float(input("Enter cost per ticket: "))


total_amount = 0


for i in range(passengers):
    age = int(input(f"Enter age of passenger {i+1}: "))

    
    if age < 12:
        fare = ticket * 0.70  
    elif age > 59:
        fare = ticket * 0.50  
    else:
        fare = ticket         

    total_amount += fare


print("Total ticket amount for all passengers:", total_amount)