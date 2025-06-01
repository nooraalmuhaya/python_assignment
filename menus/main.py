from Receptionist import receptionist_menu
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
            print("\n" * 50)
            receptionist_menu()
            print("\n" * 10)
        elif choice == "2":
            print("\n" * 50)
            doctor_menu()
        elif choice == "3":
            print("\n" * 50)
            nurse_menu()
        elif choice == "4":
            print("\n" * 50)
            patient_menu()
        elif choice == "5":
            print("\n" * 50)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5")

if __name__ == "__main__":
    main_menu()



