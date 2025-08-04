num = int(input("Enter a three-digit number: "))

if 100 <= num <= 999:
    if str(num) == str(num)[:-1]:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
else:
    print("Please enter a valid three-digit number.")