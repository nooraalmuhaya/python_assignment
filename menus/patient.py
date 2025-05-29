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
            view_personal_medical_records()  
        elif patient_choice == '2':
            view_upcoming_appointments()  
        elif patient_choice == '3':
            update_personal_information() 
        elif patient_choice == '4':
            view_billing_details()  
        elif patient_choice == '5':
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
