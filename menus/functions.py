### Receptionist Functions ###

#1
def register_new_patient():
    print("Function: Register new patient")

#2
def Update_details():
    print("Function: Update details")

#3
def schedule_appointment():
    print("Function: Schedule appointment")

#4
def process_payment():
    print("Function: Process payment")


### Doctor Functions ###

#1
def view_patient_records():
    print("Function: View patient records")
 
 #2
def update_medical_records():
     print("Function: Update medical records")

#3
def view_appointments():
    print("Function: View appointments")

#4
def block_unblock_availability():
    print("Function: Block/Unblock availability")


### Nurse Functions ###

#1 
def view_doctor_appointments():
    try:
        with open("appointment.txt", "r") as file:
            eachline= file.readlines()
            print("Doctor Appointments:")


#2
def record_patient_observations():
    print("Function: Record patient observations")

#3
def view_doctor_prescriptions():
    print("Function: View doctor's prescriptions")

#4
def administer_medicine():
    print("Function: Administer medicine")

### Patient Functions ###

#1
def view_personal_medical_records():
    print("Function: View personal medical records")
#2
def view_upcoming_appointments():
    print("Function: View upcoming appointments")

#3
def update_personal_information():
    print("Function: Update personal information")

#4
def view_billing_details():
    print("Function: View billing details")