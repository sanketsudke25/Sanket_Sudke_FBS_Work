import threading
import string
import time

def print_lowercase():
    for ch in string.ascii_lowercase: 
        print("Lowercase:", ch)
        time.sleep(0.1)  
def print_uppercase():
    for ch in string.ascii_uppercase:  
        print("Uppercase:", ch)
        time.sleep(0.1)  

def main():
    
    t1 = threading.Thread(target=print_lowercase)
    t2 = threading.Thread(target=print_uppercase)

    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("✅ Finished printing alphabets concurrently!")

if __name__ == "__main__":
    main()