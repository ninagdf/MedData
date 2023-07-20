from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
from tkinter import messagebox
import subprocess

#this should have CREATE, UPDATE, DELETE functionality button
#additional SEARCH 

class MedData:
    def __init__(self, root):
        self.root = root
        self.root.title("MedData")
        self.root.geometry("1540x800+0+0")
        self.root.resizable(width=False, height=False)  # Disable window resizing
        icon = PhotoImage(file='materials/Icon.png')
        self.root.iconphoto(True, icon)

        def to_home():
            root.destroy()
            subprocess.run(['python', 'Home.py'])
                
        def on_enter_AboutUsBack(event):
            button4.config(image=button4.resized_hover_image)

        def on_leave_AboutUsBack(event):
            button4.config(image=button4.resized_image)


        # Create transparent image
        transparent_image = PhotoImage(width=1, height=1)

        # Load the button image
        AboutUsBackButton = PhotoImage(file='D:/ninaf/MedData/MedData/materials/AboutUsBack.png')

        # Resize the button image
        resized_image4 = AboutUsBackButton.subsample(int(AboutUsBackButton.width() / 90), int(AboutUsBackButton.height() / 55))

        # Create button widget
        button4 = Button(root, command=to_home, image=resized_image4, bd=0, relief="flat", highlightthickness=0, compound="center",
                    fg="white", bg="white", activebackground="white", activeforeground="white")

        # Set the width and height of the button
        desired_width4 = 90
        desired_height4 = 55
        button4.config(width=desired_width4, height=desired_height4)

        # Hovered button image
        AboutUsBackButtonHover = PhotoImage(file='materials/AboutUsBackHover.png')

        # Store resized images as attributes of button widgets
        button4.resized_image = resized_image4
        button4.resized_hover_image = AboutUsBackButtonHover.subsample(57, 66)

        # Add the AboutUs image to the canvas as a button
        button4_window = canvas.create_window(1400, 50, anchor="nw", window=button4)

        # Event bindings for hovering effect
        button4.bind('<Enter>', on_enter_AboutUsBack)
        button4.bind('<Leave>', on_leave_AboutUsBack)

        self.patientid = StringVar()  # Should match the column name in Patient table: PatientID
        self.name = StringVar()  # Should match the column name in Patient table: Name
        self.contactnumber = StringVar()  # Should match the column name in Patient table: ContactNumber
        self.age = StringVar()  # Should match the column name in Patient table: Age
        self.sex = StringVar()  # Should match the column name in Patient table: Sex
        self.currentphysician = StringVar()  # Should match the column name in Patient table: CurrentPhysician
        self.dateoflastupdate = StringVar()  # Should match the column name in Patient table: DateofLastUpdate
        self.physicianlicenceno = StringVar()  # Should match the column name in Physician table: PhysicianLicenseNumber
        self.physician = StringVar()  # Should match the column name in PhysicianInfo table: Physician
        self.contactnum2 = StringVar()  # Should match the column name in PhysicianInfo table: ContactNumber
        self.illnesscode = StringVar()  # Should match the column name in diagnosisandmeds table: IllnessCode
        self.illness = StringVar()  # This line is not used in the code you provided, make sure it's intended to be used elsewhere
        self.medicinereferencenumber = StringVar()  # Should match the column name in diagnosisandmeds table: MedicineReferenceNumber
        self.medicationname = StringVar()  # Should match the column name in diagnosisandmeds table: Medicationname
        self.dosage = StringVar()  # Should match the column name in diagnosisandmeds table: Dosage
        self.freq = StringVar()  # Should match the column name in diagnosisandmeds table: Freq
        self.medstartdate = StringVar()  # Should match the column name in diagnosisandmeds table: MedStartDate
        self.medenddate = StringVar()  # Should match the column name in diagnosisandmeds table: MedEndDate
        self.purpose = StringVar()  # Should match the column name in diagnosisandmeds table: Purpose
        self.treatmentnotes = StringVar()  # Should match the column name in diagnosisandmeds table: TreatmentNotes
        self.illnessstartdate = StringVar()  # Should match the column name in diagnosisandmeds table: IllnessStartDate
        self.illnessenddate = StringVar()  # Should match the column name in diagnosisandmeds table: IllnessEndDate

        # ==========================DataFrame======================
        background_color = "#FFFFFF"
        
        Dataframe1 = Frame(self.root)
        Dataframe1.place(x=195, y=150, width=312, height=308)

        Dataframe2 = Frame(self.root)
        Dataframe2.place(x=675, y=150, width=300, height=308)

        DataframeShow = Frame(self.root)
        DataframeShow.place(x=1018, y=147, width=500, height=316)

        DataframeLeft = LabelFrame(Dataframe1,
                                   text="", fg="#05066D", bg = background_color)
        DataframeLeft.place(x=0, y=5, width=1000, height=320)

        DataframeLeft2 = LabelFrame(Dataframe2,
                                   text="", fg="#05066D", bg = background_color)
        DataframeLeft2.place(x=0, y=5, width=300, height=320)

        DataframeRight = LabelFrame(DataframeShow,
                                    text="", fg="#05066D", bg = background_color)
        DataframeRight.place(x=0, y=0, width=500, height=323)

        # =============================== buttons frame =======================
        Buttonframe = Frame(self.root)
        Buttonframe.place(x=20, y=482, width=1495, height=70)

        # =============================== Details frame ===========================
        Detailsframe = Frame(self.root)
        Detailsframe.place(x=19, y=568, width=1499, height=211)

        # ================================ Dataframeleft =========================================
        self.txtpatientid = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.patientid, fg="black", bg=background_color)
        self.txtpatientid.grid(row=0, column=1)


        self.txtpatientname = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.name, fg="black", bg=background_color)
        self.txtpatientname.grid(row=1, column=1)


        self.txtcontactnumber = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.contactnumber, fg="black", bg=background_color)
        self.txtcontactnumber.grid(row=2, column=1)


        self.txtage = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.age, fg="black", bg=background_color)
        self.txtage.grid(row=3, column=1)


        self.txtsex = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.sex, fg="black", bg=background_color)
        self.txtsex.grid(row=4, column=1)


        self.txtcurrentphysician = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.currentphysician, fg="black", bg=background_color)
        self.txtcurrentphysician.grid(row=5, column=1)


        self.txtdateoflastupdate = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.dateoflastupdate, fg="black", bg=background_color)
        self.txtdateoflastupdate.grid(row=6, column=1)


        self.txtphysicianlicenceno = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.physicianlicenceno, fg="black", bg=background_color)
        self.txtphysicianlicenceno.grid(row=7, column=1)


        self.txtphysician = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.physician, fg="black", bg=background_color)
        self.txtphysician.grid(row=8, column=1)


        self.txtcontactnum2 = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.contactnum2, fg="black", bg=background_color)
        self.txtcontactnum2.grid(row=9, column=1)


        self.txtillnesscode = Entry(DataframeLeft, font=("Poppins SemiBold", 10), width=38, textvariable=self.illnesscode, fg="black", bg=background_color)
        self.txtillnesscode.grid(row=10, column=1)


        self.txtillness = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.illness, fg="black", bg=background_color)
        self.txtillness.grid(row=0, column=1)


        self.txtmedicinerefnumber = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.medicinereferencenumber, fg="black", bg=background_color)
        self.txtmedicinerefnumber.grid(row=1, column=1)


        self.txtmedicationname = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.medicationname, fg="black", bg=background_color)
        self.txtmedicationname.grid(row=2, column=1)


        self.txtdosage = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.dosage, fg="black", bg=background_color)
        self.txtdosage.grid(row=3, column=1)


        self.txtfreq = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.freq, fg="black", bg=background_color)
        self.txtfreq.grid(row=4, column=1, sticky=W)


        self.txtmedstartdate = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.medstartdate, fg="black", bg=background_color)
        self.txtmedstartdate.grid(row=5, column=1)

        self.txtmedenddate = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.medenddate, fg="black", bg=background_color)
        self.txtmedenddate.grid(row=6, column=1)


        self.txtpurpose = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.purpose, fg="black", bg=background_color)
        self.txtpurpose.grid(row=7, column=1)


        self.txttreatmentnotes = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.treatmentnotes, fg="black", bg=background_color)
        self.txttreatmentnotes.grid(row=8, column=1)


        self.txtillnessstartdate = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.illnessstartdate, fg="black", bg=background_color)
        self.txtillnessstartdate.grid(row=9, column=1)

        self.txtillnessenddate = Entry(DataframeLeft2, font=("Poppins SemiBold", 10), width=38, textvariable=self.illnessenddate, fg="black", bg=background_color)
        self.txtillnessenddate.grid(row=10, column=1)

        #=========================== DataframeRight=======================================
        self.txtOutput = Text(DataframeRight, font = ("Poppins SemiBold", 12, "bold"), width=45, height = 16, padx = 2, pady = 6)
        self.txtOutput.grid (row = 0, column = 0)

        #============================ Button ====================================
        self.btnCreate = Button(Buttonframe, command=self.iCreate ,text="Add New Data", bg="#05066D", fg="white", font=("Poppins", 12, "bold"),
                        width=23, height=2, padx=2, pady=6)
        self.btnCreate.grid(row=0, column=0)

        self.btnRead = Button(Buttonframe, command=self.iRead, text="Show", bg="#05066D", fg="white",
                             font=("Poppins", 12, "bold"), width=23, height=2, padx=2, pady=6)
        self.btnRead.grid(row=0, column=1)
        
        
        self.btnUpdate = Button(Buttonframe, command=self.iUpdate, text="Update", bg="#05066D", fg="white", font=("Poppins", 12, "bold"),
                   width=23, height=2, padx=12, pady=6)
        self.btnUpdate.grid(row=0, column=2)

        self.btnDelete = Button(Buttonframe, command= self.iDelete, text="Delete", bg="#05066D", fg="white", font=("Poppins", 12, "bold"),
                   width=23, height=2, padx=12, pady=6)
        self.btnDelete.grid(row=0, column=3)

        self.btnClear = Button(Buttonframe,command =self.Clear, text="Clear", bg="#05066D", fg="white", font=("Poppins", 12, "bold"),
                  width=23, height=2, padx=12, pady=6)
        self.btnClear.grid(row=0, column=4)

        self.btnExit = Button(Buttonframe,command=self.iExit, text="Exit", bg="#05066D", fg="white", font=("Poppins", 12, "bold"),
                 width=20, height=2, padx=12, pady=6)
        self.btnExit.grid(row=0, column=5)

       # =================================Table======================================
       # ================================ Scrollbar for Details Frame (Nasa ibaba)=====================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe, column=("patientid", "name", "contactnumber", "age", "sex", "currentphysician", "dateoflastupdate", "physicianlicenceno", "physician", "contactnum2", "illnesscode", "illness", "medicinereferencenumber", "medicationname", "dosage", "freq", "medstartdate", "medenddate", "purpose", "treatmentnotes", "illnessstartdate", "illnessenddate"),
                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        #==================================================================
                
        # Create a horizontal scrollbar
        scroll_x = Scrollbar(DataframeRight, orient=HORIZONTAL)
        scroll_x.grid(row=1, column=0, sticky="ew")

        # Create a vertical scrollbar
        scroll_y = Scrollbar(DataframeRight, orient=VERTICAL)
        scroll_y.grid(row=0, column=1, sticky="ns")

        # Create the Text widget and configure it to work with the scrollbars
        self.txtOutput = Text(DataframeRight, font=("Poppins SemiBold", 12, "bold"), width=45, height=16,
                            padx=2, pady=6, wrap=NONE, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.txtOutput.grid(row=0, column=0, sticky="nsew")

        # Configure the scrollbars to work with the Text widget
        scroll_x.config(command=self.txtOutput.xview)
        scroll_y.config(command=self.txtOutput.yview)

        # Configure grid weights to allow the Text widget to expand
        DataframeRight.grid_rowconfigure(0, weight=1)
        DataframeRight.grid_columnconfigure(0, weight=1)

        #=================================================================================
        
        self.hospital_table.heading("patientid", text="Patient ID")
        self.hospital_table.heading("name", text="Name")
        self.hospital_table.heading("contactnumber", text="Contact Number")
        self.hospital_table.heading("age", text="Age")
        self.hospital_table.heading("sex", text="Sex")
        self.hospital_table.heading("currentphysician", text="Current Physician")
        self.hospital_table.heading("dateoflastupdate", text="Date of Last Update")
        self.hospital_table.heading("physicianlicenceno", text="Physician License Number")
        self.hospital_table.heading("physician", text="Physician")
        self.hospital_table.heading("contactnum2", text="Contact Number")
        self.hospital_table.heading("illnesscode", text="Illness Code")
        self.hospital_table.heading("illness", text="Illness")
        self.hospital_table.heading("medicinereferencenumber", text="Medicine Reference Number")
        self.hospital_table.heading("medicationname", text="Medication Name")
        self.hospital_table.heading("dosage", text="Dosage")
        self.hospital_table.heading("freq", text="Frequency")
        self.hospital_table.heading("medstartdate", text="Medication Start Date")
        self.hospital_table.heading("medenddate", text="Medication End Date")
        self.hospital_table.heading("purpose", text="Purpose")
        self.hospital_table.heading("treatmentnotes", text="Treatment Notes")
        self.hospital_table.heading("illnessstartdate", text="Illness Start Date")
        self.hospital_table.heading("illnessenddate", text="Illness End Date")

        
        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)
        
        self.hospital_table.column("patientid", width=80)
        self.hospital_table.column("name", width=100)
        self.hospital_table.column("contactnumber", width=100)
        self.hospital_table.column("age", width=50)
        self.hospital_table.column("sex", width=50)
        self.hospital_table.column("currentphysician", width=120)
        self.hospital_table.column("dateoflastupdate", width=120)
        self.hospital_table.column("physicianlicenceno", width=120)
        self.hospital_table.column("physician", width=100)
        self.hospital_table.column("contactnum2", width=100)
        self.hospital_table.column("illnesscode", width=100)
        self.hospital_table.column("illness", width=120)
        self.hospital_table.column("medicinereferencenumber", width=120)
        self.hospital_table.column("medicationname", width=120)
        self.hospital_table.column("dosage", width=80)
        self.hospital_table.column("freq", width=80)
        self.hospital_table.column("medstartdate", width=120)
        self.hospital_table.column("medenddate", width=120)
        self.hospital_table.column("purpose", width=120)
        self.hospital_table.column("treatmentnotes", width=120)
        self.hospital_table.column("illnessstartdate", width=120)
        self.hospital_table.column("illnessenddate", width=120)





        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)



        self.fetch_data()


        #=============================functionalities==================================
    def iRead(self):
        self.txtOutput.insert(END, "Patient ID:\t\t\t" + self.patientid.get() + "\n")
        self.txtOutput.insert(END, "Patient Name:\t\t\t" + self.name.get() + "\n")
        self.txtOutput.insert(END, "Contact No.:\t\t\t" + self.contactnumber.get() + "\n")
        self.txtOutput.insert(END, "Age:\t\t\t" + self.age.get() + "\n")
        self.txtOutput.insert(END, "Sex:\t\t\t" + self.sex.get() + "\n")
        self.txtOutput.insert(END, "Current Physician:\t\t\t" + self.currentphysician.get() + "\n")
        self.txtOutput.insert(END, "Date of Last Update:\t\t\t" + self.dateoflastupdate.get() + "\n")
        self.txtOutput.insert(END, "Physician License No:\t\t\t" + self.physicianlicenceno.get() + "\n")
        self.txtOutput.insert(END, "Physician:\t\t\t" + self.physician.get() + "\n")
        self.txtOutput.insert(END, "Contact Number:\t\t\t" + self.contactnum2.get() + "\n")
        self.txtOutput.insert(END, "Illness Code:\t\t\t" + self.illnesscode.get() + "\n")
        self.txtOutput.insert(END, "Illness:\t\t\t" + self.illness.get() + "\n")
        self.txtOutput.insert(END, "Medicine Ref No.:\t\t\t" + self.medicinereferencenumber.get() + "\n")
        self.txtOutput.insert(END, "Medication Name:\t\t\t" + self.medicationname.get() + "\n")
        self.txtOutput.insert(END, "Dosage:\t\t\t" + self.dosage.get() + "\n")
        self.txtOutput.insert(END, "Frequency:\t\t\t" + self.freq.get() + "\n")
        self.txtOutput.insert(END, "Medication Start Date:\t\t\t" + self.medstartdate.get() + "\n")
        self.txtOutput.insert(END, "Medication End Date:\t\t\t" + self.medenddate.get() + "\n")
        self.txtOutput.insert(END, "Purpose:\t\t\t" + self.purpose.get() + "\n")
        self.txtOutput.insert(END, "Treatment Notes:\t\t\t" + self.treatmentnotes.get() + "\n")
        self.txtOutput.insert(END, "Illness Start Date:\t\t\t" + self.illnessstartdate.get() + "\n")
        self.txtOutput.insert(END, "Illness End Date:\t\t\t" + self.illnessenddate.get() + "\n")

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nina1232580",
            database="patient_db"
        )
        my_cursor = conn.cursor()

        query = """
        SELECT p.PatientID, p.Name, p.ContactNumber, p.Age, p.Sex, p.CurrentPhysician, p.DateofLastUpdate,
                ph.PhysicianLicenseNumber,
                pi.Physician, pi.ContactNumber,
                f.illnesscode, f.illness,
                d.MedicineReferenceNumber, d.Medicationname, d.Dosage, 
                d.Freq, d.MedStartDate, d.MedEndDate, d.Purpose, d.TreatmentNotes, d.IllnessStartDate, d.IllnessEndDate
        FROM Patient p
        JOIN Physician ph ON p.PatientID = ph.PatientCode
        JOIN PhysicianInfo pi ON ph.PhysicianLicenseNumber = pi.PhysicianLicenseNumber
        JOIN findings f ON p.PatientID = f.Patientreference
        JOIN diagnosisandmeds d ON p.PatientID = d.PatientNumber
        """

        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in rows:
                # Modify the column names according to your table schema
                modified_row = (
                    row[0],  # PatientID
                    row[1],  # Name
                    row[2],  # ContactNumber
                    row[3],  # Age
                    row[4],  # Sex
                    row[5],  # CurrentPhysician
                    row[6],  # DateofLastUpdate
                    row[7],  # PhysicianLicenseNumber
                    row[8],  # Physician
                    row[9],  # ContactNumber
                    row[10],  # illnesscode
                    row[11],  # illness
                    row[12],  # MedicineReferenceNumber
                    row[13],  # Medicationname
                    row[14],  # Dosage
                    row[15],  # Freq
                    row[16],  # MedStartDate
                    row[17],  # MedEndDate
                    row[18],  # Purpose
                    row[19],  # TreatmentNotes
                    row[20],  # IllnessStartDate
                    row[21]   # IllnessEndDate
                )
                self.hospital_table.insert("", END, values=modified_row)

        conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.patientid.set(row[0])  # Set the value of patientid variable
        self.name.set(row[1])  # Set the value of patientname variable
        self.contactnumber.set(row[2])  # Set the value of contactnumber variable
        self.age.set(row[3])  # Set the value of age variable
        self.sex.set(row[4])  # Set the value of sex variable
        self.currentphysician.set(row[5])  # Set the value of currentphysician variable
        self.dateoflastupdate.set(row[6])  # Set the value of dateoflastupdate variable
        self.physicianlicenceno.set(row[7])  # Set the value of physicianlicenceno variable
        self.physician.set(row[8])  # Set the value of physician variable
        self.contactnum2.set(row[9])  # Set the value of contactnum2 variable
        self.illnesscode.set(row[10])  # Set the value of illnesscode variable
        self.illness.set(row[11])  # Set the value of illness variable
        self.medicinereferencenumber.set(row[12])  # Set the value of medicinerefnumber variable
        self.medicationname.set(row[13])  # Set the value of medicationname variable
        self.dosage.set(row[14])  # Set the value of dosage variable
        self.freq.set(row[15])  # Set the value of freq variable
        self.medstartdate.set(row[16])  # Set the value of medstartdate variable
        self.medenddate.set(row[17])  # Set the value of medenddate variable
        self.purpose.set(row[18])  # Set the value of purpose variable
        self.treatmentnotes.set(row[19])  # Set the value of treatmentnotes variable
        self.illnessstartdate.set(row[20])  # Set the value of illnessstartdate variable
        self.illnessenddate.set(row[21])  # Set the value of illnessenddate variable

    def iCreate(self):
        # Retrieve values from GUI inputs
        patient_id = self.patientid.get()
        patient_name = self.name.get()
        contact_number = self.contactnumber.get()
        age = self.age.get()
        sex = self.sex.get()
        current_physician = self.currentphysician.get()
        date_of_last_update = self.dateoflastupdate.get()
        physician_license_number = self.physicianlicenceno.get()
        physician = self.physician.get()
        contact_number_2 = self.contactnum2.get()
        illness_code = self.illnesscode.get()
        illness = self.illness.get()
        medicine_reference_number = self.medicinereferencenumber.get()
        medication_name = self.medicationname.get()
        dosage = self.dosage.get()
        freq = self.freq.get()
        med_start_date = self.medstartdate.get()
        med_end_date = self.medenddate.get()
        purpose = self.purpose.get()
        treatment_notes = self.treatmentnotes.get()
        illness_start_date = self.illnessstartdate.get()
        illness_end_date = self.illnessenddate.get()
        findings_illness_code = self.illnesscode.get()
        findings_illness = self.illness.get()
        findings_patient_reference = self.patientid.get()

        # Check if all fields are filled
        if (
            patient_id == ""
            or patient_name == ""
            or contact_number == ""
            or age == ""
            or sex == ""
            or current_physician == ""
            or date_of_last_update == ""
            or physician_license_number == ""
            or physician == ""
            or contact_number_2 == ""
            or illness_code == ""
            or illness == ""
            or medicine_reference_number == ""
            or medication_name == ""
            or dosage == ""
            or freq == ""
            or med_start_date == ""
            or med_end_date == ""
            or purpose == ""
            or treatment_notes == ""
            or illness_start_date == ""
            or illness_end_date == ""
            or findings_illness_code == ""
            or findings_illness == ""
            or findings_patient_reference == ""
        ):
            messagebox.showinfo("ALERT", "Please enter all fields")
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Nina1232580",
                    database="patient_db",
                )
                cursor = con.cursor()

                # Insert data into the Patient table
                patient_query = "INSERT INTO Patient (PatientID, Name, ContactNumber, Age, Sex, CurrentPhysician, DateofLastUpdate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                patient_values = (
                    patient_id,
                    patient_name,
                    contact_number,
                    age,
                    sex,
                    current_physician,
                    date_of_last_update,
                )
                cursor.execute(patient_query, patient_values)

                # Insert data into the Physician table
                physician_query = "INSERT INTO Physician (PatientCode, PhysicianLicenseNumber) VALUES (%s, %s)"
                physician_values = (patient_id, physician_license_number)
                cursor.execute(physician_query, physician_values)

                # Insert data into the PhysicianInfo table
                physician_info_query = "INSERT INTO PhysicianInfo (PhysicianLicenseNumber, Physician, ContactNumber) VALUES (%s, %s, %s)"
                physician_info_values = (physician_license_number, physician, contact_number_2)
                cursor.execute(physician_info_query, physician_info_values)

                # Insert data into the diagnosisandmeds table
                diagnosis_meds_query = "INSERT INTO diagnosisandmeds (PatientNumber, IllnessCode, MedicineReferenceNumber, Medicationname, Dosage, Freq, MedStartDate, MedEndDate, Purpose, TreatmentNotes, IllnessStartDate, IllnessEndDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                diagnosis_meds_values = (
                    patient_id,
                    illness_code,
                    medicine_reference_number,
                    medication_name,
                    dosage,
                    freq,
                    med_start_date,
                    med_end_date,
                    purpose,
                    treatment_notes,
                    illness_start_date,
                    illness_end_date,
                )
                cursor.execute(diagnosis_meds_query, diagnosis_meds_values)

                # Insert data into the findings table
                findings_query = "INSERT INTO findings (PatientReference, IllnessCode, Illness) VALUES (%s, %s, %s)"
                findings_values = (findings_patient_reference, findings_illness_code, findings_illness)
                cursor.execute(findings_query, findings_values)

                con.commit()
                con.close()

                messagebox.showinfo("Status", "Successfully Inserted")

                # Fetch and display the updated data
                self.fetch_data()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", str(e))

    def iUpdate(self):
        # Retrieve values from GUI inputs
        patient_id = self.patientid.get()
        patient_name = self.name.get()
        contact_number = self.contactnumber.get()
        age = self.age.get()
        sex = self.sex.get()
        current_physician = self.currentphysician.get()
        date_of_last_update = self.dateoflastupdate.get()
        physician_license_number = self.physicianlicenceno.get()
        physician = self.physician.get()
        contact_number_2 = self.contactnum2.get()
        illness_code = self.illnesscode.get()
        illness = self.illness.get()
        medicine_reference_number = self.medicinereferencenumber.get()
        medication_name = self.medicationname.get()
        dosage = self.dosage.get()
        freq = self.freq.get()
        med_start_date = self.medstartdate.get()
        med_end_date = self.medenddate.get()
        purpose = self.purpose.get()
        treatment_notes = self.treatmentnotes.get()
        illness_start_date = self.illnessstartdate.get()
        illness_end_date = self.illnessenddate.get()
        findings_illness_code = self.illnesscode.get()
        findings_illness = self.illness.get()
        findings_patient_reference = self.patientid.get()

        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Nina1232580",
                database="patient_db",
            )
            cursor = con.cursor()

            # Update data in the Patient table
            patient_query = "UPDATE Patient SET Name = %s, ContactNumber = %s, Age = %s, Sex = %s, CurrentPhysician = %s, DateofLastUpdate = %s WHERE PatientID = %s"
            patient_values = (
                patient_name,
                contact_number,
                age,
                sex,
                current_physician,
                date_of_last_update,
                patient_id,
            )
            cursor.execute(patient_query, patient_values)

            # Update data in the Physician table
            physician_query = "UPDATE Physician SET PhysicianLicenseNumber = %s WHERE PatientCode = %s"
            physician_values = (physician_license_number, patient_id)
            cursor.execute(physician_query, physician_values)

            # Update data in the PhysicianInfo table
            physician_info_query = "UPDATE PhysicianInfo SET Physician = %s, ContactNumber = %s WHERE PhysicianLicenseNumber = %s"
            physician_info_values = (physician, contact_number_2, physician_license_number)
            cursor.execute(physician_info_query, physician_info_values)

            # Update data in the diagnosisandmeds table
            diagnosis_meds_query = "UPDATE diagnosisandmeds SET MedicineReferenceNumber = %s, Medicationname = %s, Dosage = %s, Freq = %s, MedStartDate = %s, MedEndDate = %s, Purpose = %s, TreatmentNotes = %s, IllnessStartDate = %s, IllnessEndDate = %s WHERE PatientNumber = %s AND IllnessCode = %s"
            diagnosis_meds_values = (
                medicine_reference_number,
                medication_name,
                dosage,
                freq,
                med_start_date,
                med_end_date,
                purpose,
                treatment_notes,
                illness_start_date,
                illness_end_date,
                patient_id,
                illness_code,
            )
            cursor.execute(diagnosis_meds_query, diagnosis_meds_values)

            # Update data in the findings table
            findings_query = "UPDATE findings SET Illness = %s WHERE PatientReference = %s AND IllnessCode = %s"
            findings_values = (findings_illness, findings_patient_reference, findings_illness_code)
            cursor.execute(findings_query, findings_values)

            con.commit()
            con.close()

            messagebox.showinfo("Status", "Successfully Updated")

            # Fetch and display the updated data
            self.fetch_data()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))

    def iDelete(self):
        # Retrieve the selected patient ID from the GUI
        patient_id = self.patientid.get()

        if patient_id == "":
            messagebox.showinfo("ALERT", "Please select a patient to delete")
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Nina1232580",
                    database="patient_db"
                )
                cursor = con.cursor()

                # Delete records from the diagnosisandmeds table
                diagnosis_meds_query = "DELETE FROM diagnosisandmeds WHERE PatientNumber = %s"
                diagnosis_meds_values = (patient_id,)
                cursor.execute(diagnosis_meds_query, diagnosis_meds_values)
                con.commit()

                # Delete records from the findings table
                findings_query = "DELETE FROM findings WHERE Patientreference = %s"
                findings_values = (patient_id,)
                cursor.execute(findings_query, findings_values)
                con.commit()

                # Delete records from the PhysicianInfo table
                physician_info_query = "DELETE FROM PhysicianInfo WHERE PhysicianLicenseNumber IN (SELECT PhysicianLicenseNumber FROM Physician WHERE PatientCode = %s)"
                physician_info_values = (patient_id,)
                cursor.execute(physician_info_query, physician_info_values)
                con.commit()

                # Delete records from the Physician table
                physician_query = "DELETE FROM Physician WHERE PatientCode = %s"
                physician_values = (patient_id,)
                cursor.execute(physician_query, physician_values)
                con.commit()

                # Delete records from the Patient table
                patient_query = "DELETE FROM Patient WHERE PatientID = %s"
                patient_values = (patient_id,)
                cursor.execute(patient_query, patient_values)
                con.commit()

                con.close()

                messagebox.showinfo("Status", "Successfully Deleted")

                # Fetch and display the updated data
                self.fetch_data()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", str(e))

    def Clear(self):
        self.patientid.set("")
        self.name.set("")
        self.contactnumber.set("")
        self.age.set("")
        self.sex.set("")
        self.currentphysician.set("")
        self.dateoflastupdate.set("")
        self.physicianlicenceno.set("")
        self.physician.set("")
        self.contactnum2.set("")
        self.illnesscode.set("")
        self.illness.set("")
        self.medicinereferencenumber.set("")
        self.medicationname.set("")
        self.dosage.set("")
        self.freq.set("")
        self.medstartdate.set("")
        self.medenddate.set("")
        self.purpose.set("")
        self.treatmentnotes.set("")
        self.dosage.set("")
        self.illnessstartdate.set("")
        self.illnessenddate.set("")
        self.txtOutput.delete("1.0", END)

    def iExit(self):
            iExit =messagebox.askyesno("Medical History Application", "Confirm you want to exit")
            if iExit>0:
             root.destroy()
            return
  

root = Tk()

canvas = Canvas(root, width=1540, height=800)
canvas.pack()

# Set the path to the background image
background_image_path6 = "materials/ManageBG.png"

# Create a PhotoImage object for the background image
background_image6 = PhotoImage(file=background_image_path6)

# Add the background image to the canvas
canvas.create_image(0, 0, anchor="nw", image=background_image6)

my_label = Label(root, text='')
my_label.pack(padx=10, pady=10)

ob = MedData(root)
root.mainloop()


