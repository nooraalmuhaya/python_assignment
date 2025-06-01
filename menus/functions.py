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
    print("\n Record Patient Observation")
    print("-" * 50 ) 
    #ِِAccept the patient observation and save it in variables
    name=input("Enter patient name: ")
    blood=input("Enter blood pressure (e.g , 120/80): ")
    pulse=input("Enter Pulse rate (bpm): ")
    temperature=input("Enter temperature (°C): ")
    
    #make sure that the data and time format is correct
    while True:
        date_time= input("Enter date and time (e.g , 2025-06-01 12:30)")
        if is_valid_datetime(date_time):
            break
        else:
            print("Invalid format. Please try again (e.g., 2025-06-01 14:30)")

    #the observation will be saved in the file in this format
    observation=name + "," + blood + "," + pulse + "," + temperature + "," + date_time + "\n"

    try:
        with open("data/patient.txt", "a") as file :
            file.write(observation) #record the observation in the file
        print("-" * 50)
        print("Observation recorded successfully.\n")#display a message if the records were savedd in the file
    except:
        print("Error saving the observation.\n")
        #if there is any errors show this error message

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
            print("-" * 101)
            print(f"| {'Date':20} | {'Time':8} | {'Diagnosis':20} | {'Prescription':40} |")
            print("-" * 101)
 
            for line in eachline:
                line = line.strip()
                parts = line.split(",")
 
                if len(parts) == 4:
                    date, time, diagnosis, prescription = parts
                    print(f"| {date.strip():20} | {time.strip():8} | {diagnosis.strip():20} | {prescription.strip():40} |")
                    print("-" * 101)
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


####################### additional functions ###########################

#this function is to verify the date and time format 
def is_valid_datetime(dt):
    if len(dt) != 16:
        return False
    if dt[4] != '-' or dt[7] != '-' or dt[10] != ' ' or dt[13] != ':' :
        return False
    return True
