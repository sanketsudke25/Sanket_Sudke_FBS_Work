from Vehicle import TwoWheeler
from Vehicle import ThreeWheeler
from Vehicle import FourWheeler
from Vehicle import HeavyVehicle

def main():
    while (True):
        print("\n--- Toll Calculation Menu ---")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle")
        print("5. Exit")

        choice = input("Enter your choice (1 to 5): ")

        if (choice == '5'):
            print("Exiting... Thank you!")
            break

        persons_input = input("Enter number of persons in vehicle: ")
        if (not persons_input.isdigit()):
            print("Invalid input! Please enter a valid number.")
            continue

        persons = int(persons_input)

        if (choice == '1'):
            vehicle = TwoWheeler(persons)
        elif (choice == '2'):
            vehicle = ThreeWheeler(persons)
        elif (choice == '3'):
            vehicle = FourWheeler(persons)
        elif (choice == '4'):
            vehicle = HeavyVehicle(persons)
        else:
            print("Invalid choice! Please try again.")
            continue

        toll = vehicle.calculate_toll()
        print(f"Total toll to be paid: Rs {toll}")

if __name__ == "__main__":
    main()