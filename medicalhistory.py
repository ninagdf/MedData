from tkinter import *
import tkinter.ttk as ttk
import random
import time 
import datetime
from tkinter import messagebox
from tkinter import Scrollbar

import mysql.connector

#this should have CREATE, UPDATE, DELETE functionality button
#additional SEARCH 


class MedData:
    def __init__(self, root):
        self.root = root
        self.root.title("MedData")
        self.root.geometry("1540x800+0+0")
      

        self.patientid=StringVar()
        self.patientname=StringVar()
        self.contactnumber=StringVar()
        self.age=StringVar()
        self.sex=StringVar()
        self.currentphysician=StringVar()
        self.physicianlicenceno=StringVar()
        self.physician=StringVar()
        self.contactnum2=StringVar()
        self.illnesscode=StringVar()
        self.illness=StringVar()
        self.medicinerefnumber=StringVar()
        self.medicationname=StringVar()
        self.dosage=StringVar()
        self.freq=StringVar()
        self.medstartdate=StringVar()
        self.medenddate=StringVar()
        self.purpose=StringVar()
        self.treatmentnotes=StringVar()
        self.illnessstartdate=StringVar()
        self.illnessenddate=StringVar()
        



        lbtitle = Label(self.root, bd=20, relief=RIDGE, text="MEDICAL HISTORY APPLICATION", fg="blue", bg="#cadce6",
                        font=("times new roman", 50, "bold"))
        lbtitle.pack(side=TOP, fill=X)

        # ==========================DataFrame======================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE,
                                   font=("arial", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=700)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("times new roman", 12, "bold"), text="Output")
        DataframeRight.place(x=990, y=5, width=460, height=370)

        # =============================== buttons frame =======================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # =============================== Details frame ===========================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=200)

        # ================================ Dataframeleft =========================================
     
        lblpatientid = Label(DataframeLeft, font=("arial", 10, "bold"), text="Patient ID:", padx=2)
        lblpatientid.grid(row=0, column=0, sticky=W)
        txtpatientid = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.patientid)
        txtpatientid.grid(row=0, column=1)

        lblpatientname = Label(DataframeLeft, font=("arial", 10, "bold"), text="Patient Name:", padx=2)
        lblpatientname.grid(row=1, column=0, sticky=W)
        txtpatientname = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.patientname)
        txtpatientname.grid(row=1, column=1)

        lblcontactnumber = Label(DataframeLeft, font=("arial", 10, "bold"), text="Contact Number:", padx=2, pady=2)
        lblcontactnumber.grid(row=2, column=0, sticky=W)
        txtcontactnumber = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.contactnumber)
        txtcontactnumber.grid(row=2, column=1)

        lblage = Label(DataframeLeft, font=("arial", 10, "bold"), text="Age:", padx=2, pady=4)
        lblage.grid(row=3, column=0, sticky=W)
        txtage = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.age)
        txtage.grid(row=3, column=1)

        lblsex = Label(DataframeLeft, font=("arial", 10, "bold"), text="Sex:", padx=2, pady=4)
        lblsex.grid(row=4, column=0, sticky=W)
        txtsex = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.sex)
        txtsex.grid(row=4, column=1)

        lblcurrentphysician = Label(DataframeLeft, font=("arial", 10, "bold"), text="Current Physician:", padx=2, pady=4)
        lblcurrentphysician.grid(row=5, column=0, sticky=W)
        txtcurrentphysician = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.currentphysician)
        txtcurrentphysician.grid(row=5, column=1)

        lblphysicianlicenceno = Label(DataframeLeft, font=("arial", 10, "bold"), text="Physician Licence Number:", padx=2, pady=4)
        lblphysicianlicenceno.grid(row=6, column=0, sticky=W)
        txtphysicianlicenceno = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.physicianlicenceno)
        txtphysicianlicenceno.grid(row=6, column=1)

        lblphysician = Label(DataframeLeft, font=("arial", 10, "bold"), text="Physician:", padx=2, pady=2)
        lblphysician.grid(row=7, column=0, sticky=W)
        txtphysician = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.physician)
        txtphysician.grid(row=7, column=1)

        lblcontactnum2 = Label(DataframeLeft, font=("arial", 10, "bold"), text="Contact Number:", padx=2, pady=2)
        lblcontactnum2.grid(row=8, column=0, sticky=W)
        txtcontactnum2 = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.contactnum2)
        txtcontactnum2.grid(row=8, column=1)

        lblillnesscode = Label(DataframeLeft, font=("arial", 10, "bold"), text="Illness Code:", padx=2, pady=2)
        lblillnesscode.grid(row=9, column=0, sticky=W)
        txtillnesscode = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.illnesscode)
        txtillnesscode.grid(row=9, column=1)

        lblillness = Label(DataframeLeft, font=("arial", 10, "bold"), text="Illness:", padx=2, pady=2)
        lblillness.grid(row=10, column=0, sticky=W)
        txtillness = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.illness)
        txtillness.grid(row=10, column=1)

        lblmedicinerefnumber = Label(DataframeLeft, font=("arial", 10, "bold"), text="Medicine Reference Number:", padx=2)
        lblmedicinerefnumber.grid(row=0, column=2, sticky=W)
        txtmedicinerefnumber = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.medicinerefnumber)
        txtmedicinerefnumber.grid(row=0, column=3)

        lblmedicationname = Label(DataframeLeft, font=("arial", 10, "bold"), text="Medication Name:", padx=2, pady=2)
        lblmedicationname.grid(row=1, column=2, sticky=W)
        txtmedicationname = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.medicationname)
        txtmedicationname.grid(row=1, column=3)

        lbldosage = Label(DataframeLeft, font=("arial", 10, "bold"), text="Dosage:", padx=2, pady=2)
        lbldosage.grid(row=2, column=2, sticky=W)
        txtdosage = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.dosage)
        txtdosage.grid(row=2, column=3)

        lblfreq = Label(DataframeLeft, font=("arial", 10, "bold"), text="Frequency:", padx=2, pady=2)
        lblfreq.grid(row=3, column=2, sticky=W)
        txtfreq = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.freq)
        txtfreq.grid(row=3, column=3, sticky=W)

        lblmedstartdate = Label(DataframeLeft, font=("arial", 10, "bold"), text="Medication Start Date:", padx=2, pady=2)
        lblmedstartdate.grid(row=4, column=2, sticky=W)
        txtmedstartdate = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.medstartdate)
        txtmedstartdate.grid(row=4, column=3)

        lblmedenddate = Label(DataframeLeft, font=("arial", 10, "bold"), text="Medication End Date:", padx=2, pady=2)
        lblmedenddate.grid(row=5, column=2, sticky=W)
        txtmedenddate = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.medenddate)
        txtmedenddate.grid(row=5, column=3)

        lblPurpose = Label(DataframeLeft, font=("arial", 10, "bold"), text="Purpose:", padx=2, pady=2)
        lblPurpose.grid(row=6, column=2, sticky=W)
        txtPurpose = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.purpose)
        txtPurpose.grid(row=6, column=3)

        lbltreatmentnotes = Label(DataframeLeft, font=("arial", 10, "bold"), text="Treatment Notes:", padx=2, pady=2)
        lbltreatmentnotes.grid(row=7, column=2, sticky=W)
        txttreatmentnotes = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.treatmentnotes)
        txttreatmentnotes.grid(row=7, column=3)

        lblillnessstartdate = Label(DataframeLeft, font=("arial", 10, "bold"), text="Illness Start Date:", padx=2, pady=2)
        lblillnessstartdate.grid(row=8, column=2, sticky=W)
        txtillnessstartdate = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.illnessstartdate)
        txtillnessstartdate.grid(row=8, column=3)

        lblillnessenddate = Label(DataframeLeft, font=("arial", 10, "bold"), text="Illness End Date:", padx=2, pady=2)
        lblillnessenddate.grid(row=9, column=2, sticky=W)
        txtillnessenddate = Entry(DataframeLeft, font=("arial", 10), width=38, textvariable=self.illnessenddate)
        txtillnessenddate.grid(row=9, column=3)



        
     



        #=========================== DataframeRight=======================================
        self.txtOutput = Text(DataframeRight, font = ("arial", 12, "bold"), width=45, height = 16, padx = 2, pady = 6)
        self.txtOutput.grid (row = 0, column = 0)


        #============================ Button ====================================
        btnPrescription = Button(Buttonframe, command=self.output ,text="Add New Data", bg="#318eeb", fg="white", font=("arial", 12, "bold"),
                        width=23, height=2, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, command=self.output, text="Prescription Data", bg="#318eeb", fg="white",
                             font=("arial", 12, "bold"), width=23, height=2, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)
        
        
        btnUpdate = Button(Buttonframe, command=self.update, text="Update", bg="#318eeb", fg="white", font=("arial", 12, "bold"),
                   width=23, height=2, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, command= self.idelete, text="Delete", bg="#318eeb", fg="white", font=("arial", 12, "bold"),
                   width=23, height=2, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe,command =self.Clear, text="Clear", bg="#318eeb", fg="white", font=("arial", 12, "bold"),
                  width=23, height=2, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,command=self.iExit, text="Exit", bg="#318eeb", fg="white", font=("arial", 12, "bold"),
                 width=23, height=2, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # ==================================Table======================================
       # ================================ Table =======================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe, column=("patientid", "patientname", "contactnumber", "age", "sex", "currentphysician", "physicianlicenceno",
                                                "physician", "contactnum2", "illnesscode", "illness", "medicinerefnumber", "medicationname", "dosage", "freq", "medstartdate", "medenddate", "Purpose", "treatmentnotes", "illnessstartdate", "illnessenddate"),
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
        self.txtOutput = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16,
                            padx=2, pady=6, wrap=NONE, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.txtOutput.grid(row=0, column=0, sticky="nsew")

        # Configure the scrollbars to work with the Text widget
        scroll_x.config(command=self.txtOutput.xview)
        scroll_y.config(command=self.txtOutput.yview)

        # Configure grid weights to allow the Text widget to expand
        DataframeRight.grid_rowconfigure(0, weight=1)
        DataframeRight.grid_columnconfigure(0, weight=1)



        
        #=================================================================================
        
        self.hospital_table.heading("patientid", text="PatientID")
        self.hospital_table.heading("patientname", text="Patient Name")
        self.hospital_table.heading("contactnumber", text="ContactNo")
        self.hospital_table.heading("age", text="Age")
        self.hospital_table.heading("sex", text="Sex")
        self.hospital_table.heading("currentphysician", text="Current Physician")
        self.hospital_table.heading("physicianlicenceno", text="Physician Licence Number")
        self.hospital_table.heading("physician", text="Physician")
        self.hospital_table.heading("contactnum2", text="Contact Number")
        self.hospital_table.heading("illnesscode", text="Illness Code")
        self.hospital_table.heading("illness", text="Illness")
        self.hospital_table.heading("medicinerefnumber", text="Medicine Reference Number")
        self.hospital_table.heading("medicationname", text="Medication Name")
        self.hospital_table.heading("dosage", text="Dosage")
        self.hospital_table.heading("freq", text="Frequency")
        self.hospital_table.heading("medstartdate", text="Medication Start Date")
        self.hospital_table.heading("medenddate", text="Medication Start Date")
        self.hospital_table.heading("Purpose", text="Purpose")
        self.hospital_table.heading("treatmentnotes", text="Treatment Notes")
        self.hospital_table.heading("illnessstartdate", text="Illness Start Date")
        self.hospital_table.heading("illnessenddate", text="Illness End Date")

        
        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)
        
        self.hospital_table.column("patientid", width=100)
        self.hospital_table.column("patientname", width=100)
        self.hospital_table.column("contactnumber", width=100)
        self.hospital_table.column("age", width=100)
        self.hospital_table.column("sex", width=100)
        self.hospital_table.column("currentphysician", width=100)
        self.hospital_table.column("physicianlicenceno", width=100)
        self.hospital_table.column("physician", width=100)
        self.hospital_table.column("contactnum2", width=100)
        self.hospital_table.column("illnesscode", width=100)
        self.hospital_table.column("illness", width=100)
        self.hospital_table.column("medicinerefnumber", width=100)
        self.hospital_table.column("medicationname", width=100)
        self.hospital_table.column("dosage", width=100)
        self.hospital_table.column("freq", width=100)
        self.hospital_table.column("medstartdate", width=100)
        self.hospital_table.column("medenddate", width=100)
        self.hospital_table.column("Purpose", width=100)
        self.hospital_table.column("treatmentnotes", width=100)
        self.hospital_table.column("illnessstartdate", width=100)
        self.hospital_table.column("illnessenddate", width=100)




        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)



        self.fetch_data()


   
    
              #=====================================functionality declaration==========================================
    def IprescriptionData(self):
            if self.patientid.get()==""or self.ref.get()=="":
                messagebox.showerror("Error", "All fiels are required")
            else:
                conn=mysql.connector.connect(host="localhost", username="root", password = "database27", database ="patient_db")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                           
                                                                                                                                self.patientid.get(),
                                                                                                                                self.patientname.get(),
                                                                                                                                self.contactnumber.get(),
                                                                                                                                self.age.get(),
                                                                                                                                self.sex.get(),
                                                                                                                                self.currentphysician.get(),
                                                                                                                                self.physicianlicenceno.get(),
                                                                                                                                self.physician.get(),
                                                                                                                                self.contactnum2.get(),
                                                                                                                                self.illnesscode.get(),
                                                                                                                                self.illness.get(),
                                                                                                                                self.medicinerefnumber.get(),
                                                                                                                                self.medicationname.get(),
                                                                                                                                self.dosage.get(),
                                                                                                                                self.freq.get(),
                                                                                                                                self.medstartdate.get(),
                                                                                                                                self.medenddate.get(),
                                                                                                                                self.purpose.get(),
                                                                                                                                self.treatmentnotes.get(),
                                                                                                                                self.illnessstartdate.get(),
                                                                                                                                self.illnessenddate.get(),

                                                                            
                                                                                                        ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")

    def update(self):
            conn=mysql.connector.connect(host="localhost", username="root", password = "database27", database ="patient_db")
            my_cursor=conn.cursor()
            my_cursor.execute("update patient set patientid =%s,patientname=%s,contactnumber=%s,age=%s,sex=%s,currentphysician=%s,physicianlicenceno=%s,physician=%s,contactnum2=%s,illnesscode=%s,illness=%s,medicinerefnumber=%s,medicationname=%s,dosage=%s,freq=%s,medstartdate=%s,medenddate=%s,purpose=%s,treatmentnotes=%s,illnessstartdate=%s,illnessenddate=%s")
    
    """
    def fetch_data(self):
            # Establish a connection to the database
            conn = mysql.connector.connect(host="localhost", username="root", password="database27", database="patient_db")
            my_cursor = conn.cursor()

            # Fetch data from Table 1
            my_cursor.execute("SELECT * FROM patient")
            rows_table1 = my_cursor.fetchall()
            if len(rows_table1) != 0:
                # Iterate over the fetched rows and insert them into the hospital_table
                for i in rows_table1:
                    self.hospital_table.insert("", END, values=i)

            # Fetch data from Table 2
            my_cursor.execute("SELECT * FROM physician")
            rows_table2 = my_cursor.fetchall()
            if len(rows_table2) != 0:
                # Iterate over the fetched rows and insert them into the hospital_table
                for i in rows_table2:
                    self.hospital_table.insert("", END, values=i)

            # Fetch data from Table 3
            my_cursor.execute("SELECT * FROM physicianinfo")
            rows_table3 = my_cursor.fetchall()
            if len(rows_table3) != 0:
                # Iterate over the fetched rows and insert them into the hospital_table
                for i in rows_table3:
                    self.hospital_table.insert("", END, values=i)

            # Fetch data from Table 4
            my_cursor.execute("SELECT * FROM findings")
            rows_table4 = my_cursor.fetchall()
            if len(rows_table4) != 0:
                # Iterate over the fetched rows and insert them into the hospital_table
                for i in rows_table4:
                    self.hospital_table.insert("", END, values=i)

            # Fetch data from Table 5
            my_cursor.execute("SELECT * FROM diagnosisandmeds")
            rows_table5 = my_cursor.fetchall()
            if len(rows_table5) != 0:
                # Iterate over the fetched rows and insert them into the hospital_table
                for i in rows_table5:
                    self.hospital_table.insert("", END, values=i)

            # Close the database connection
            conn.close()
    """
    def fetch_data(self): 
        conn=mysql.connector.connect(host="localhost", username="root", password = "database27", database ="patient_db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from patient")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
         
    def get_cursor(self, event=""):
            cursor_row = self.hospital_table.focus()  # Correction: changed .found() to .focus()
            content = self.hospital_table.item(cursor_row)
            row = content["values"]
            self.patientid.set(row[0])
            self.patientname.set(row[1])
            self.contactnumber.set(row[2])
            self.age.set(row[3])
            self.sex.set(row[4])
            self.currentphysician.set(row[5])
            self.physicianlicenceno.set(row[6])
            self.physician.set(row[7])
            self.contactnum2.set(row[8])
            self.illnesscode.set(row[9])
            self.illness.set(row[10])
            self.medicinerefnumber.set(row[11])
            self.medicationname.set(row[12])
            self.dosage.set(row[13])
            self.freq.set(row[14])
            self.medstartdate.set(row[15])
            self.medenddate.set(row[16])
            self.purpose.set(row[17])
            self.treatmentnotes.set(row[18])
            self.illnessstartdate.set(row[19])
            self.illnessenddate.set(row[20])



    def output(self):
            self.txtOutput.insert(END,"Patient ID:\t\t\t"+self.patientid.get() + "\n")
            self.txtOutput.insert(END,"Patient Name:\t\t\t"+self.patientname.get() + "\n")
            self.txtOutput.insert(END,"Contact No.:\t\t\t"+self.contactnumber.get() + "\n")
            self.txtOutput.insert(END,"Age:\t\t\t"+self.age.get() + "\n")
            self.txtOutput.insert(END,"Sex:\t\t\t"+self.sex.get() + "\n")
            self.txtOutput.insert(END,"Current Physician:\t\t\t"+self.currentphysician.get() + "\n")
            self.txtOutput.insert(END,"Physician License No:\t\t\t"+self.physicianlicenceno.get() + "\n")
            self.txtOutput.insert(END,"Physician:\t\t\t"+self.physician.get() + "\n")
            self.txtOutput.insert(END,"Contact Number:\t\t\t"+self.contactnum2.get() + "\n")
            self.txtOutput.insert(END,"Illness Code:\t\t\t"+self.illnesscode.get() + "\n")
            self.txtOutput.insert(END,"Illness:\t\t\t"+self.illness.get() + "\n")
            self.txtOutput.insert(END,"Medicine Ref No.:\t\t\t"+self.medicinerefnumber.get() + "\n")
            self.txtOutput.insert(END,"Medication Name:\t\t\t"+self.medicationname.get() + "\n")
            self.txtOutput.insert(END,"Dosage:\t\t\t"+self.dosage.get() + "\n")
            self.txtOutput.insert(END,"Frequency:\t\t\t"+self.freq.get() + "\n")
            self.txtOutput.insert(END,"Medication Start Date:\t\t\t"+self.medstartdate.get() + "\n")
            self.txtOutput.insert(END,"Medication End Date:\t\t\t"+self.medenddate.get() + "\n")
            self.txtOutput.insert(END,"Purpose:\t\t\t"+self.purpose.get() + "\n")
            self.txtOutput.insert(END,"Treatment Notes:\t\t\t"+self.treatmentnotes.get() + "\n")
            self.txtOutput.insert(END,"Illness Start Date:\t\t\t"+self.illnessstartdate.get() + "\n")
            self.txtOutput.insert(END,"Illness End Date:\t\t\t"+self.illnessenddate.get() + "\n")

    def idelete(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="database27", database="patient_db")
            my_cursor = conn.cursor()
            query = "delete from hospital where Reference_No=%s"
            value = self.patientid.get()  # Replace self.ref.get() with the appropriate variable you want to use for deletion
            my_cursor.execute(query, (value,))  # Pass value as a parameter to the execute method

            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Delete", "Patient has been deleted successfully")

    def Clear(self):
            self.patientid.set("")
            self.patientname.set("")
            self.contactnumber.set("")
            self.age.set("")
            self.sex.set("")
            self.currentphysician.set("")
            self.physicianlicenceno.set("")
            self.physician.set("")
            self.contactnum2.set("")
            self.illnesscode.set("")
            self.illness.set("")
            self.medicinerefnumber.set("")
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
            self.txtOutput.delete("1.0",END)    

    def iExit(self):
            iExit =messagebox.askyesno("Medical History Application", "Confirm you want to exit")
            if iExit>0:
             root.destroy()
            return
                 
        

   

root = Tk()
ob = MedData(root)
root.mainloop()