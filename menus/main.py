from receptionist import receptionist_menu
from doctor import doctor_menu
from nurse import nurse_menu
from patient import patient_menu

def main_menu():
    while True:
        print("\n===Welcome to our Clinic===")
        print("1. Receptionist")
        print("2. Doctor")
        print("3. Nurse")
        print("4. Patient")
        print("5. Exit")

        choice = input("Enter your choise(1-4)") 

        if choice== "1":
            receptionist_menu()
        elif choice == "2":
            doctor_menu()
        elif choice == "3":
            nurse_menu()
        elif choice == "4":
            patient_menu()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5")

if __name__ == "__main__":
    main_menu()



