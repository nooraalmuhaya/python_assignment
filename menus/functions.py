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
        #open the file in read mode
        with open("data/appointment.txt", "r") as file:

            #each line in the file will be saved in list called eachline
            eachline= file.readlines() 

            #show a title before displaying appointments
            print("Doctor Appointments:\n")

            #Print table headers
            print("-" * 43)
            print(f"| {'Doctor':15} | {'Patient':10} | {'Time':8} |")
            print("-" * 43)

            for line in eachline: 
                line = line.strip()  #cleaning the lines from any additional spaces and remove the "\n" from the end of the line
                parts = line.split(",")  #split each line by commas and save them in a list

                #check if the line has exactly 3 parts
                if len(parts) == 3:
                    #take each part in the list and save it in these variables
                    doctor, patient, time = parts 
                    
                    #print the appointment in a table
                    print(f"| {doctor.strip():15} | {patient.strip():10} | {time.strip():8} |")
                    print("-" * 43)
                else:
                    #skip and warn if there is not 3 parts
                    print("Skipped a like due to incorrect format.")

    except FileNotFoundError:
        print("The file 'appointment.txt' was not found.")
        #if there is any errors show this error message

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
    try:
        with open("data/medical_records.txt", "r") as file:
            eachline = file.readlines()
 
            print("Medical Records:\n")
            print("-" * 76)
            print(f"| {'Date':15} | {'Time':10} | {'Diagnosis':20} | {'Prescription':20} |")
            print("-" * 76)
 
            for line in eachline:
                line = line.strip()
                parts = line.split(",")
 
                if len(parts) == 4:
                    date, time, diagnosis, prescription = parts
                    print(f"| {date.strip():15} | {time.strip():10} | {diagnosis.strip():20} | {prescription.strip():20} |")
                    print("-" * 76)
                else:
                    print("Incorrect format in medical_records.txt.")
    except FileNotFoundError:
        print("The file 'medical_records.txt' was not found.")
#2
def view_upcoming_appointments():
    print("Function: View upcoming appointments")

#3
def update_personal_information():
    print("Function: Update personal information")

#4
def view_billing_details():
    print("Function: View billing details")