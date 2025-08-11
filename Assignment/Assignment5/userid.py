
userid = input("enter User ID: ")
password = input("enter Password: ")


num = 3


for i in range(1, num + 1):
    entered_id = input("Enter User ID: ")
    entered_pass = input("Enter Password: ")

    if (entered_id == userid and entered_pass == password):
        print("Login successful!")
        break
    else:
        print(f"Incorrect credentials. Attempt {i} of {num}")

else:
    print("Too many failed attempts. Program terminated.")