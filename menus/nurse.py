from functions import view_doctor_appointments,record_patient_observations,view_doctor_prescriptions,administer_medicine

def nurse_menu():
    while True:
        print("\n--- Nurse Menu ---")
        print("1. View doctor's appointments")
        print("2. Record patient observations")
        print("3. View doctor's prescriptions")
        print("4. Administer medicine")
        print("5. Back to main menu")

        nurse_choice = input("Enter your choice (1-5): ")


        if nurse_choice == '1':
            view_doctor_appointments()
        elif nurse_choice == '2':
            record_patient_observations()
        elif nurse_choice == '3':
            view_doctor_prescriptions()  
        elif nurse_choice == '4':
            administer_medicine()  
        elif nurse_choice == '5':
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
