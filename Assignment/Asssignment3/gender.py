gender = input("Enter gender(M/F):")
age = int(input("enter age:"))
if((gender == 'M' and age >= 21) or (gender == 'F' and age >= 18)):
        print('Eligiable for marriage')
else:
        print('Not Eligiable for marriage')    