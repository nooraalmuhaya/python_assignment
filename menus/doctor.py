from functions import view_patient_records,update_medical_records,view_appointments,block_unblock_availability

def doctor_menu():
    while True:
        print("\n--- Doctor Menu ---")
        print("1. View patient records")
        print("2. Update medical records")
        print("3. View appointments")
        print("4. Block/Unblock availability")
        print("5. Back to main menu")

        doctor_choice = input("Enter your choice (1-5): ")

        if doctor_choice == '1':
            print("\n" * 50)
            view_patient_records() 
            input("\nPress Enter to return to the menu...")
            
        elif doctor_choice == '2':
            print("\n" * 50)
            update_medical_records() 
            input("\nPress Enter to return to the menu...")
        elif doctor_choice == '3':
            print("\n" * 50)
            view_appointments()
            input("\nPress Enter to return to the menu...")
        elif doctor_choice == '4':
            print("\n" * 50)
            block_unblock_availability()
            input("\nPress Enter to return to the menu...")
        elif doctor_choice == '5':
            print("\n" * 50)
            return
        
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
