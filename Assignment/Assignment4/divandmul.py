
num1 = int(input("Enter starting number: ")) 
num2 = int(input("Enter ending number: ")) 

for num in range(num1, num2 + 1): 
    if num % 7 == 0 and num % 5 == 0: 
        print(num)