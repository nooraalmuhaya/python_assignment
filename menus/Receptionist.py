
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
            register_new_patient()  
        elif receptionist_choice == '2':
            Update_details()  
        elif receptionist_choice == '3':
            schedule_appointment
        elif receptionist_choice == '4':
            process_payment()
        elif receptionist_choice == '5':
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

