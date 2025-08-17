def odd():
    
    total = 0
    for i in range(1, n + 1, 2):  
        total += i
    return total
    
n = int(input("Enter the value of n: "))
print(f"Sum of all odd numbers is: {odd()}")


