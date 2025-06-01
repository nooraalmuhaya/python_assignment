### Receptionist Functions ###

#1
def register_new_patient():
    print("\n--- Register New Patient ---")
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    contact = input("Enter Contact Number: ")
    address = input("Enter Address: ")
 
    with open("patients.txt", "a") as file:
        file.write(f"{patient_id},{name},{age},{contact},{address}\n")
    print("Patient registered successfully!")
    print("-"*50)

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
    patient_id = get_valid_patient_id()
    blood=input("Enter blood pressure (e.g , 120/80): ")
    pulse=input("Enter Pulse rate (bpm): ")
    temperature=input("Enter temperature (°C): ")
    
    #make sure that the data and time format is correct
    while True:
        date_time= input("Enter date and time (e.g , 2025-06-01 12:30)")
        if is_valid_datetime(date_time):
            break
        print("Invalid format. Please try again (e.g., 2025-06-01 14:30)")

    obs_id= observation_id()

    #the observation will be saved in the file in this format
    observation = f"{obs_id}, {patient_id},{blood},{temperature},{date_time}\n"

    with open("nurse_log.txt", "a") as file :
            file.write(observation) #record the observation in the file
    
    print("-" * 50)
    print("Observation recorded successfully.\n")#display a message if the records were savedd in the file


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

# this function is to verify the date and time format 
def is_valid_datetime(dt):
    if len(dt) != 16:
        return False
    if dt[4] != '-' or dt[7] != '-' or dt[10] != ' ' or dt[13] != ':' :
        return False
    return True

# this function generate a new observation ID
def observation_id():
    try:
        with open("nurse_logs.txt" , "r") as file:
            observation = file.readlines()
            if not observation: #if the file is empty
                return "N001"  
            last_line= observation[-1].strip() 
            #get the last line in the file and remove new line or extra spaces
            last_id= last_line.split(",")[0] 
            #split the lines by commas and get the first part(the ID)
            num = int(last_id[1:])
             #remove the first character and convert the rest to an integer
            return f"N{str(num+1).zfill(3)}" 
        #add 1 to the number and return the number with leading zeros
    except FileNotFoundError: 
        #if the file doesn't exist yet
        return "N001" 
        #start from the first observation ID

# this function verify if the patient is exist or no
def is_existing_patient(patient_id):
    try:
        with open("patients.txt" , "r") as file:
            for line in file:
                if line.startswith(patient_id+","):
                    return True
                
        return False
    except FileNotFoundError:
        return False

# this function prompt user for a valid patient ID or register a new one if not found
def get_valid_patient_id():
    while True:
        patient_id = input("Enter patient ID: ").strip()

        if is_existing_patient(patient_id):
            return patient_id
        
        print("Patient not found.")
        choice = input("Do you want to register this patient? (yes/no): " ).lower().strip()

        if choice == "yes":
            register_new_patient()
            print("Patient registered. Please re-enter the ID.")
        else:
            print("Please enter an existing patient ID. ")