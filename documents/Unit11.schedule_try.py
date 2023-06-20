import sqlite3
from datetime import datetime

# this is an initial connection to make sure there is a table for the program to work in.
initial_connection = sqlite3.connect("booking_system.db")
# create a cursor
initial_cursor = initial_connection.cursor()

# drop tables to get clean ones for our dummy data
initial_cursor.execute("DROP TABLE IF EXISTS Patient")
initial_connection.commit()
initial_cursor.execute("DROP TABLE IF EXISTS Healthcare_professional")
initial_connection.commit()
initial_cursor.execute("DROP TABLE IF EXISTS Doctor")
initial_connection.commit()
initial_cursor.execute("DROP TABLE IF EXISTS Nurse")
initial_connection.commit()
initial_cursor.execute("DROP TABLE IF EXISTS Receptionist")
initial_connection.commit()
initial_cursor.execute("DROP TABLE IF EXISTS Prescription")
initial_connection.commit()
initial_cursor.execute("DROP TABLE IF EXISTS Appointments")
initial_connection.commit()

# creating patient table only if it doesn't exist
initial_cursor.execute("""CREATE TABLE IF NOT EXISTS Patient(
                Patient_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name varchar (255),
                last_name varchar (255),
                address varchar(255),
                phone int                
                )""")

# commit changes to database
initial_connection.commit()

# creating transaction table only if it doesn't exist
initial_cursor.execute("""CREATE TABLE IF NOT EXISTS Healthcare_professional (
                Professional_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                First_name varchar (255),
                Last_name varchar (255)
                )""")

# commit changes to database
initial_connection.commit()


# creating transaction table only if it doesn't exist
initial_cursor.execute("""CREATE TABLE IF NOT EXISTS Doctor (
                Doctor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                FOREIGN KEY (Doctor_ID) REFERENCES Healthcare_professional (Professional_ID)
                )""")

# commit changes to database
initial_connection.commit()

initial_cursor.execute("""CREATE TABLE IF NOT EXISTS Nurse (
                Nurse_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                FOREIGN KEY (Nurse_ID) REFERENCES Healthcare_professional (Professional_ID)
                )""")

# commit changes to database
initial_connection.commit()

# creating transaction table only if it doesn't exist
initial_cursor.execute("""CREATE TABLE IF NOT EXISTS Receptionist (
                Receptionist_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                First_name varchar (255),
                Last_name varchar (255)                
                )""")
# FOREIGN KEY (Receptionist_ID) REFERENCES Healthcare_professional (Professional_ID)

# commit changes to database
initial_connection.commit()

# creating transaction table only if it doesn't exist
initial_cursor.execute("""CREATE TABLE IF NOT EXISTS Prescription (
                Prescription_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                type varchar (255),
                patient int,
                doctor int,
                quantity int,
                dosage float,
                FOREIGN KEY (patient) REFERENCES Patient (Patient_ID)
                FOREIGN KEY (doctor) REFERENCES Doctor (Doctor_ID)
                )""")

# commit changes to database
initial_connection.commit()

# creating transaction table only if it doesn't exist
initial_cursor.execute("""CREATE TABLE IF NOT EXISTS Appointments (
                Appointment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Patient INTEGER,
                HLTCARE_PROF INTEGER,
                Type_of_appointment varchar (255),
                Date_of_appointment varchar (255),
                FOREIGN KEY (Patient) REFERENCES Patient (Patient_ID)
                FOREIGN KEY (HLTCARE_PROF) REFERENCES Healthcare_professional (Professional_ID)
                )""")

# commit changes to database
initial_connection.commit()
# close the initial cursor
initial_cursor.close()
# then close the initial connection to the database
initial_connection.close()

# create dummy data
dummy_data_connection = sqlite3.connect("booking_system.db")
# create a cursor
dummy_data_cur = dummy_data_connection.cursor()

# another way to insert data
sql_health2 = """ INSERT INTO Healthcare_professional (First_name, Last_name) VALUES (?, ?) """
values_health2 = [
    ('Mister', 'Doctor'),
    ('Kaiser', 'Clara'),
    ('Marie', 'Curie')
]
# creating cursor to execute dummy data
dummy_data_cur.executemany(sql_health2, values_health2)

# inserting more dummy data
another_dummy = ["David", "Flash"]
dummy_data_cur.execute('INSERT INTO Healthcare_professional (First_name, Last_name) '
                       'VALUES (?, ?)', another_dummy)
# inserting doctor data
sql_doctor = "INSERT INTO Doctor (Doctor_ID) " \
             "VALUES ((SELECT Professional_ID " \
             "FROM Healthcare_professional " \
             "WHERE first_name = 'Marie'))"
dummy_data_cur.execute(sql_doctor)

sql_doctor2 = "INSERT INTO Doctor (Doctor_ID) " \
              "VALUES ((SELECT Professional_ID " \
              "FROM Healthcare_professional " \
              "WHERE first_name = 'Mister'))"
dummy_data_cur.execute(sql_doctor2)

sql_nurse = "INSERT INTO Nurse (Nurse_ID) " \
            "VALUES ((SELECT Professional_ID " \
            "FROM Healthcare_professional " \
            "WHERE first_name = 'David'))"
dummy_data_cur.execute(sql_nurse)

# inserting dummy patient data into patient table
sql_patient = "INSERT INTO Patient (first_name, last_name, address, phone) VALUES (?, ?, ?, ?)"
values_patient = [
    ('Herman', 'Larsen', 'address 1', 147),
    ('Skulpt', 'Anderson', 'address 2', 258),
    ('Mikael', 'Pirate', 'address 3', 369),
    ('Mikael', 'Rally driver', 'address 4', 123),
    ('Soda', 'Stream', 'address 5', 741),
    ('Herr', 'Gaardman', 'address 6', 852),
    ('MA', 'Monk', 'address 7', 963)
]
dummy_data_cur.executemany(sql_patient, values_patient)

# inserting dummy data prescriptions into Prescription table
sql_prescriptions = "INSERT INTO Prescription (type, patient, doctor, quantity, dosage) VALUES (?, ?, ?, ?, ?)"
values_prescriptions = [
    ("Sedative", 3, 1, 25, 250),
    ("Sedative", 4, 1, 25, 250),
    ("Sleeping pill", 1, 3, 10, 100),
    ("carbonic acid", 5, 1, 1, 60)
]
dummy_data_cur.executemany(sql_prescriptions, values_prescriptions)

# inserting dummy data appointments into Appointments table
sql_appointments = "INSERT INTO Appointments (patient, hltcare_prof, type_of_appointment, date_of_appointment) " \
                   "VALUES (?, ?, ?, ?)"
values_appointments = [
    (2, 3, "Headache", datetime(2022, 5, 30)),
    (6, 3, "Hernia", datetime(2022, 12, 16)),
    (7, 3, "Back ache", datetime(2022, 4, 23)),
    (1, 4, "Blood test", datetime(2022, 8, 2)),
    (2, 2, "Broken arm", datetime(2022, 1, 1)),
    (3, 1, "Angry dog", datetime(2022, 11, 1))
]
dummy_data_cur.executemany(sql_appointments, values_appointments)

# inserting dummy data receptionists into Receptionist table
sql_receptionist = "INSERT INTO receptionist (first_name, last_name) VALUES (?,?)"
values_receptionist = [
    ("Nr1", "Receptionist"),
    ("Nr2", "Receptionist")
]
dummy_data_cur.executemany(sql_receptionist, values_receptionist)

# all dummy data has been created and inserted, commit and close the connection to database
dummy_data_connection.commit()
dummy_data_cur.close()
dummy_data_connection.close()


# Create all the classes that are needed in the program
class HealthcareProfessional:
    def __init__(self, HPnr: int, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_number = HPnr

    def Consultation(self, patient):
        patient_name = patient.first_name + patient.last_name
        datum = datetime.now()
        print(f"I have consulted {patient_name} on the {datum}.")
        return f"I have consulted {patient_name} on the {datum}."

    def i_am_health_prof(self):
        print("I am a healthcare professional")


class Doctor(HealthcareProfessional):
    def __init__(self, empnr: int, first_name, last_name):
        super().__init__(empnr, first_name, last_name)

    def issue_prescription(self, patient: int, quantity: int, dosage: float, type_of_prescription: str):
        # open a connection to the database
        kalle_anka = sqlite3.connect("booking_system.db")
        # create a cursor
        cur = kalle_anka.cursor()
        # Insert entries into table
        cur.execute("INSERT INTO prescription (Type, Patient, Doctor, Quantity, Dosage) VALUES (?, ?, ?, ?, ?)",
                    [type_of_prescription,
                     patient,
                     self.employee_number,
                     quantity,
                     dosage])

        # commit changes to database
        kalle_anka.commit()
        # close the cursor
        cur.close()
        # Close connection to database when function is not running
        kalle_anka.close()

    def i_am_doctor(self):
        print("I am doctor")


# creating nurse class, establishing inheritance
class Nurse(HealthcareProfessional):
    def __init__(self, empnr: int, first_name, last_name):
        super().__init__(empnr, first_name, last_name)

    def i_am_nurse(self):
        print("I am nurse")

    def shout_NURSE(self):
        another_number = self.employee_number
        print("NURSE!")


# creating Patient class
class Patient:
    # instantiating class
    def __init__(self, pnr: int, first_name: str, last_name: str, address: str, phone: int):
        self.ID = pnr
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone

    # create function for patient to request repeat prescription
    def Request_repeat(self, repeat_doc: Doctor):
        # connect to database
        patient_connection = sqlite3.connect("booking_system.db")
        # create a cursor
        prescription_cursor = patient_connection.cursor()

        prescription_cursor.execute(
            " SELECT * FROM Prescription WHERE prescription.patient = (?)"
            , [self.ID])

        prescription_tuple = prescription_cursor.fetchmany()

        prescription_cursor.close()
        patient_connection.close()

        if not prescription_tuple:
            try:
                raise NameError('prescription not found')
            except NameError:
                print("Couldn't find prescription")
        else:
            repeat_doc.issue_prescription(self.ID, prescription_tuple[0][4], prescription_tuple[0][5],
                                          f"{prescription_tuple[0][1]} repeat")

    # creating function for receptionist to book appointment for patient
    def Request_appointment(self, receptionist, appointment_type: str, healthcare_professional):
        # def makeAppointment(type_of_appointment: str, staff: int, patient: int, date):
        receptionist.makeAppointment(appointment_type, healthcare_professional.employee_number, self.ID, datetime.now())


# creating Prescription class and defining class variables
class Prescription:
    Type: str
    Patient: Patient
    Doctor: Doctor
    Quantity: int
    Dosage: float

    # instantiating class prescriptions
    def __init__(self, pres_id, type_of_pres, patient, doctor, quantity, dosage):
        self.pres_id = pres_id
        self.type = type_of_pres
        self.Patient = patient
        self.Doctor = doctor
        self.Quantity = quantity
        self.Dosage = dosage


# creating class prescription
class Receptionist:
    name = ''

    # instantiating class
    def __init__(self, rec_nr: int, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.Employee_Number = rec_nr

    # creating function to make Appointment
    def makeAppointment(self, type_of_appointment: str, staff: int, patient: int, some_date):
        # open a connection to the database
        connection = sqlite3.connect("booking_system.db")
        # create a cursor
        cur = connection.cursor()

        # format our date, because of some trouble with SQL?
        # first the format of the date
        format_code = '%Y-%m-%d %H:%M:%S'
        # then the conversion
        string_of_date = some_date.strftime(format_code)

        # Insert values into the Appointment tables, insert values as of and when
        cur.execute(
            "INSERT INTO Appointments (Patient, HLTCARE_PROF, type_of_appointment, date_of_appointment) "
            "VALUES (?, ? ,? ,?)",
            [patient, staff, type_of_appointment, string_of_date])

        # commit changes to database
        connection.commit()
        # close the cursor
        cur.close()
        # then close the connection to the database
        connection.close()


# creating class Appointment
class Appointment:

    # instantiating class
    def __init__(self, app_id, patient, staff, type_of_appointment, date_sent_in):
        self.ID = app_id
        self.typ_av_mote = type_of_appointment
        self.date = date_sent_in
        self.staff = staff
        self.patient = patient


# creating Appointment schedule class
class AppointmentSchedule:
    # creating (empty) list to be populated by appointments
    appointments_in_schedule = []

    # instantiating class
    def __init__(self):
        # populate our list of appointments with the actual appointments from the database.
        # open a connection to the database
        connection = sqlite3.connect("booking_system.db")
        # create a cursor
        cur = connection.cursor()

        # query the database, and get all appointments
        cur.execute("SELECT * FROM appointments")
        elements = cur.fetchall()

        if not elements:
            # if there are no records in the database
            print('No records found')

        else:
            # Loop through results and add them to our list
            for element in elements:
                self.appointments_in_schedule.append(element)

        # no commit necessary after a SELECT statement, so just close cursor and the connection
        cur.close()
        connection.close()

    # This method is an example of using my data objects as parameters. This could be done with
    # just string and datetime, but using the data objects we ensure that we are working with the correct data types.
    def add_appointment(self, working_appointment: Appointment, patient_id: int, nhs_prof: HealthcareProfessional):
        # open a connection to the database
        connection = sqlite3.connect("booking_system.db")
        # create a cursor
        cur = connection.cursor()
        cur.execute("INSERT INTO Appointments (Patient, HLTCARE_PROF, Type_of_appointment, Date_of_appointment) "
                    "VALUES (?,?,?,?)",
                    [
                        patient_id,
                        nhs_prof.employee_number,
                        working_appointment.typ_av_mote,
                        working_appointment.date,
                    ])
        # commit changes to database
        connection.commit()
        # close the cursor
        cur.close()
        # Close connection to database when function is not running
        connection.close()

    # method to cancel an appointment
    def cancel_appointment(self, appointment: Appointment):
        # open a connection to the database
        connection = sqlite3.connect("booking_system.db")
        # create a cursor
        cur = connection.cursor()

        # delete row from the database based on the ID that gets sent in. Obviously we need to know the ID, so the /
        # easiest is to require a known appointment
        cur.execute("DELETE FROM Appointments WHERE Appointment_id = (?)", [appointment.ID])

        # should clear appointments and reload from database?
        # self.appointments_in_schedule.clear()
        # self.reload_appointments()

        # close cursor and connection
        cur.close()
        connection.close()

    def find_next(self, date_to_test_against: datetime):
        # creating an empty list to be filled with dates
        appointments_list_only_dates = []

        # we always get a string from the database, and need to convert it to datetime
        for datum in self.appointments_in_schedule:
            # the string with the date is always in position 4 in the tuple, that is extracted to date_string variable
            date_string = datum[4]
            # converting the string to datetime
            datetime_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
            # add the date to our list that we're going to calculate
            appointments_list_only_dates.append(datetime_obj)

        # get today's date,
        # this should be changed to whatever date we need to check is closest against
        if date_to_test_against:
            test_date = date_to_test_against
        else:
            # if we don't get a datetime, just use today's date
            test_date = datetime.now()

        # get all differences with date as values
        dates_dict = {
            abs(test_date.timestamp() - something.timestamp()): something
            for something in appointments_list_only_dates}

        # extracting minimum key using min()
        test_dates = dates_dict[min(dates_dict.keys())]

        # printing result
        print("Nearest date from list : " + str(test_dates))

#
# # TEST SECTION OF CODE
# # open connection to the database to get all relevant data and convert it to objects
# get_data_connection = sqlite3.connect("booking_system.db")
# # create a cursor
# get_data_cursor = get_data_connection.cursor()
#
# # get patient data from table in database
# get_sql_patient = "SELECT * FROM Patient"
# get_data_cursor.execute(get_sql_patient)
# patient_elements = get_data_cursor.fetchall()
# list_of_patient_objects = []
# if not patient_elements:
#     # if there are no records in the database
#     print('No records found')
#
# else:
#     # Loop through results and add them to our list
#     for element in patient_elements:
#         new_patient = Patient(element[0], element[1], element[2], element[3], element[4])
#         list_of_patient_objects.append(new_patient)
#
# # get receptionists
# get_sql_Receptionist = "SELECT * FROM Receptionist"
# get_data_cursor.execute(get_sql_Receptionist)
# # DON'T GET FROM THIS LIST
# Receptionist_elements = get_data_cursor.fetchall()
# # ONLY GET OBJECTS FROM THIS KINDS OF LIST
# list_of_Receptionist_objects = []
# if not Receptionist_elements:
#     # if there are no records in the database
#     print('No records found')
#
# else:
#     # Loop through results and add them to our list
#     for element in Receptionist_elements:
#         new_Receptionist: Receptionist
#         new_Receptionist = Receptionist(element[0], element[1], element[2])
#         list_of_Receptionist_objects.append(new_Receptionist)
#
# # get Healthcare professionals
# get_sql_Healthcare_professional = "SELECT * FROM Healthcare_professional"
# get_data_cursor.execute(get_sql_Healthcare_professional)
# # DON'T GET FROM THIS LIST
# Healthcare_professional_elements = get_data_cursor.fetchall()
# # ONLY GET OBJECTS FROM THESE KINDS OF LIST
# list_of_HealthcareProfessionals_objects = []
# if not Healthcare_professional_elements:
#     # if there are no records in the database
#     print('No records found')
#
# else:
#     # Loop through results and add them to our list
#     for element in Healthcare_professional_elements:
#         new_HealthcareProfessional: HealthcareProfessional
#         new_HealthcareProfessional = HealthcareProfessional(element[0], element[1], element[2])
#         list_of_HealthcareProfessionals_objects.append(new_HealthcareProfessional)
#
# # get Appointment
# get_sql_Appointment = "SELECT * FROM Appointments"
# get_data_cursor.execute(get_sql_Appointment)
# # DON'T GET FROM THIS LIST
# Appointment_elements = get_data_cursor.fetchall()
# # ONLY GET OBJECTS FROM THESE KINDS OF LIST
# list_of_Appointment_objects = []
# if not Appointment_elements:
#     # if there are no records in the database
#     print('No records found')
#
# else:
#     # Loop through results and add them to our list
#     for element in Appointment_elements:
#         new_Appointment: Appointment
#         new_Appointment = Appointment(element[0], element[1], element[2], element[3], element[4])
#         list_of_Appointment_objects.append(new_Appointment)
#
# # get Prescription
# get_sql_Prescription = "SELECT * FROM Prescription"
# get_data_cursor.execute(get_sql_Prescription)
# # DON'T GET FROM THIS LIST
# Prescription_elements = get_data_cursor.fetchall()
# # ONLY GET OBJECTS FROM THESE KINDS OF LIST
# list_of_Prescription_objects = []
# if not Prescription_elements:
#     # if there are no records in the database
#     print('No records found')
#
# else:
#     # Loop through results and add them to our list
#     for element in Prescription_elements:
#         new_Prescription: Prescription
#         new_Prescription = Prescription(element[0], element[1], element[2], element[3], element[4], element[5])
#         list_of_Prescription_objects.append(new_Prescription)
#
# # Each function is tested below by me creating objects that executes functions.
#
#
# # get doctors
# # get the doctors in the correct order for the doctor object.
# # there are other ways to do this, this just seemed like the simplest
# get_sql_Doctor = "SELECT Doctor_ID, first_name, last_name FROM Healthcare_professional " \
#                  "JOIN Doctor on Healthcare_professional.Professional_ID = Doctor.Doctor_ID "
# get_data_cursor.execute(get_sql_Doctor)
# # DON'T GET FROM THIS LIST
# Doctor_elements = get_data_cursor.fetchall()
# # ONLY GET OBJECTS FROM THIS KINDS OF LIST
# list_of_Doctor_objects = []
# if not Doctor_elements:
#     # if there are no records in the database
#     print('No records found')
#
# else:
#     # Loop through results and add them to our list
#     for element in Doctor_elements:
#         new_Doctor = Doctor(element[0], element[1], element[2])
#         list_of_Doctor_objects.append(new_Doctor)
#
# # no commit necessary after a SELECT statement, so just close cursor and the connection
# get_data_cursor.close()
# get_data_connection.close()
#
# # choosing one patient from the list to act as test subject
# p = list_of_patient_objects[0]
#
# # choosing first receptionist from the list to act as test subject
# r = list_of_Receptionist_objects[0]
#
# # choosing first Doctor from the list to act as test subject
# doc = list_of_Doctor_objects[0]
#
# # choosing first healthcare professional in list to act as test subject
# new_nhs_prof = list_of_HealthcareProfessionals_objects[0]
#
# # creating first appointment. Numbers are unique identifiers of appointmentID, patientID, healthcare staff, type of
# # appointment and date.
# new_Appointment_1 = Appointment(5, 3, 3, "headache", datetime.now())
#
# # patient requests an appointment. receptionist appoints a test appointment with first doctor
# p.Request_appointment(r, "test appointment", doc)
#
# # patient requests repeat prescription by first doctor in our list
# p.Request_repeat(doc)
#
# # first doctor in the lust issues patient with a prescription
# doc.issue_prescription(p.ID, 123, 123, "test prescription")
#
# # first doctor in our list consults the first patient in patient list
# doc.Consultation(p)
#
# # appointment schedule
# app_sched = AppointmentSchedule()
#
# # calling on function in appointment schedule class to add appointment
# app_sched.add_appointment(new_Appointment_1, 6, new_nhs_prof)
#
# # canceling the appointment just booked
# app_sched.cancel_appointment(new_Appointment_1)
#
# # finding next available appointment from specified list
# app_sched.find_next(datetime.now())


