def menu():
    while True:
        print("\n==Welcome to our Clinic")
        print("1. Receptionist")
        print("2. Doctor")
        print("3. Nurse")
        print("4. Patient")
        print("5. Exit")

        choise = input("Enter your choise(1-4)") 

        if choice== "1":
            receptionist_menu()
        elif choise == "2":
            doctor_menu()
        elif choise == "3":
            nurse_menu()
        elif choise == "4":
            patient_menu()
        elif choise == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5")



