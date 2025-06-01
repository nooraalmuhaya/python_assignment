from functions import register_new_patient,Update_details,schedule_appointment,process_payment

def receptionist_menu():
    while True:
        print("\n--- Receptionist Menu ---")
        print("1. Register new patient")
        print("2. Update patient's details")
        print("3. Schedule appointment")
        print("4. Process payment")
        print("5. Back to main menu")

        receptionist_choice = input("Enter your choice (1-4): ")

        if receptionist_choice == '1':
            print("\n" * 50)
            register_new_patient()  
            input("\nPress Enter to return to the menu...")
        elif receptionist_choice == '2':
            print("\n" * 50)
            Update_details()  
            input("\nPress Enter to return to the menu...")
        elif receptionist_choice == '3':
            print("\n" * 50)
            schedule_appointment()
            input("\nPress Enter to return to the menu...")
        elif receptionist_choice == '4':
            print("\n" * 50)
            process_payment()
            input("\nPress Enter to return to the menu...")
        elif receptionist_choice == '5':
            print("\n" * 50)
            return
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

