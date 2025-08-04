#inport random
#captcha = random.readint(1111,9999)
#print(captcha)

import random


userid = input("Enter userid: ")
password = input("Enter password: ")


if userid == "Sanket" and password == "8010":
    print("Login successful.")

    
    captcha = random.randint(1111, 9999)
    print("Captcha:", captcha)

  
    admin_input = input("Enter the captcha shown above: ")

    
    if admin_input == str(captcha):
        print(" Verification successful. Access granted.")
    else:
        print(" Verification failed. Access denied.")
else:
    print("Incorrect userid or password.")