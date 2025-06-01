from functions import view_personal_medical_records,view_upcoming_appointments,update_personal_information,view_billing_details

def patient_menu():
    while True:
        print("\n--- Patient Menu ---")
        print("1. View personal medical records")
        print("2. View upcoming appointments")
        print("3. Update personal information")
        print("4. View billing details")
        print("5. Back to main menu")

        patient_choice = input("Enter your choice (1-5): ")

        if patient_choice == '1':
            print("\n" * 50)
            view_personal_medical_records()  
            input("\nPress Enter to return to the menu...")
        elif patient_choice == '2':
            print("\n" * 50)
            view_upcoming_appointments()  
            input("\nPress Enter to return to the menu...")
        elif patient_choice == '3':
            print("\n" * 50)
            update_personal_information() 
            input("\nPress Enter to return to the menu...")
        elif patient_choice == '4':
            print("\n" * 50)
            view_billing_details()  
            input("\nPress Enter to return to the menu...")
        elif patient_choice == '5':
            print("\n" * 50)
            return
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
