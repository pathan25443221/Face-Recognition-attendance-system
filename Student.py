import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import psycopg2
import cv2
from dotenv import load_dotenv


class Student:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
#======================================variables======================================================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()
        # # first img
        # img = Image.open(r"C:\Users\JIYA\Desktop\face_recognition_system\college_images\face-recognition.png")
        # img = img.resize((500, 130))
        # self.photo_img = ImageTk.PhotoImage(img)
        # f_lbl = Label(self.root, image=self.photo_img)
        # f_lbl.place(x=0, y=0, width=500, height=130)
        #
        # # second img
        # img1 = Image.open(r"C:\Users\JIYA\Desktop\face_recognition_system\college_images\smart-attendance.jpg")
        # img1 = img1.resize((500, 130))
        # self.photo_img1 = ImageTk.PhotoImage(img1)
        # f_lbl = Label(self.root, image=self.photo_img1)
        # f_lbl.place(x=500, y=0, width=500, height=130)
        #
        # # third img
        # img2 = Image.open(r"C:\Users\JIYA\Desktop\face_recognition_system\college_images\iStock-182059956_18390_t12.jpg")
        # img2 = img2.resize((550, 130))
        # self.photo_img2 = ImageTk.PhotoImage(img2)
        # f_lbl = Label(self.root, image=self.photo_img2)
        # f_lbl.place(x=1000, y=0, width=550, height=130)

        # background img
        img3 =Image.open(r"college_images\ChatGPT Image Jul 10, 2025, 11_25_31 AM.png")
        img3 = img3.resize((1530,790))
        self.photo_img3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photo_img3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="#001F3F",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
#_______________________MAIN FRAME___________________________________

        main_frame = Frame(bg_img,bd=2,bg="#0b0f2e")
        main_frame.place(x=10,y=100, width=1480,height=600)

#_______________________LEFT LABEL FRAME_____________________________

        left_frame= LabelFrame(main_frame,bd=2,bg="#0b0f2e",fg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130))
        self.photo_img_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.photo_img_left)
        f_lbl.place(x=5, y=0, width=718, height=130)
#_______________________CURRENT COURSE_______________________________
        current_course_frame = LabelFrame(left_frame, bd=2, bg="#0b0f2e",fg="white", relief=RIDGE, text="Current course information",font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        dep_label = Label(current_course_frame,text="Department",font=("times new roman", 13, "bold"),bg="#0b0f2e",fg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 13, "bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science and IT","Business Administration",)
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # COURSE
        course_label = Label(current_course_frame,text="Course",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 13, "bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","MBA","MCA","BCA","BBA","MBA-HR","MBA-GN")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label = Label(current_course_frame,text="Year",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 13, "bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # SEMESTER
        semester_label = Label(current_course_frame,text="Semester",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 13, "bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","semester-1","semester-2","semester-3","semester-4","semester-5","semester-6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


#_______________________CLASS STUDENT INFORMATION LABEL FRAME_________________________________
        class_student_frame = LabelFrame(left_frame, bd=2, bg="#0b0f2e",fg="white", relief=RIDGE, text="Class Student Information",font=("times new roman", 13, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)
        # Student ID
        studentID_label =Label(class_student_frame,text="StudentID:",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        studentID_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman", 13, "bold"),)
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        # Student Name
        studentName_label =Label(class_student_frame,text="Student Name:",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman", 13, "bold"),)
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Class Division
        class_div_label =Label(class_student_frame,text="Class Division:",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, width=18,
                                    font=("times new roman", 13, "bold"), state="readonly", )
        class_div_combo["values"] = ("A", "B", "C","NA")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        # Roll No
        roll_no_label =Label(class_student_frame,text="Roll No:",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman", 13, "bold"),)
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label =Label(class_student_frame,text="Gender",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=18,font=("times new roman", 13, "bold"),state="readonly",)
        gender_combo["values"]=("Select Gender","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Date of Birth
        dob_label =Label(class_student_frame,text="DOB:",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman", 13, "bold"),)
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label =Label(class_student_frame,text="Email:",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman", 13, "bold"),)
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone No
        phone_no_label =Label(class_student_frame,text="Phone No:",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman", 13, "bold"),)
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label =Label(class_student_frame,text="Address:",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman", 13, "bold"),)
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # # Teacher name
        # teacher_label =Label(class_student_frame,text="Teacher Name:",font=("times new roman", 13, "bold"),bg="#001F3F",fg="white")
        # teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        #
        # teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman", 13, "bold"),)
        # teacher_entry.grid(row=4 ,column=3,padx=10,pady=5,sticky=W)
#_______________________________________Radio Buttons_______________________________________
        self.var_radio1=StringVar()
        radionbtn1 =ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2 =ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="no")
        radionbtn2.grid(row=6,column=1)
#_______________________________________Button frame________________________________________
        btn_frame = Frame(class_student_frame, bd=2, bg="#0b0f2e", relief=RIDGE)
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btn_frame,command=self.add_data,text="Save",width=17,font=("times new roman",13,"bold"),bg="#001F3F",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,command=self.update_data,text="Update",width=17,font=("times new roman",13,"bold"),bg="#001F3F",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,command=self.delete_data,text="Delete",width=17,font=("times new roman",13,"bold"),bg="#001F3F",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,command=self.reset_data,text="Reset",width=17,font=("times new roman",13,"bold"),bg="#001F3F",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, bg="#0b0f2e", relief=RIDGE)
        btn_frame1.place(x=0, y=235, width=715, height=35)
        take_photo_btn = Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="#001F3F",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="#001F3F",fg="white")
        update_btn.grid(row=0,column=1)
#_______________________RIGHT LABEL FRAME_____________________________________________________

        right_frame= LabelFrame(main_frame,bd=2,fg="white",bg="#0b0f2e",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        img_right = Image.open(r"college_images\smart-attendance.jpg")
        img_right = img_right.resize((715, 130))
        self.photo_img_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(right_frame, image=self.photo_img_right)
        f_lbl.place(x=5, y=0, width=708, height=130)

#==================================================SEARCHING SYSTEM=====================================================
        # ================== SEARCHING SYSTEM ==================
        search_frame = LabelFrame(right_frame, bd=2, bg="#0b0f2e", fg="white",
                                  relief=RIDGE, text="Search System",
                                  font=("times new roman", 13, "bold"))
        search_frame.place(x=5, y=135, width=708, height=70)

        search_label = Label(search_frame, text="Search By:",
                             font=("times new roman", 13, "bold"),
                             bg="#001F3F", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search_by,
                                    font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, textvariable=self.var_search_txt,
                                 width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", command=self.search_data,
                            width=12, font=("times new roman", 12, "bold"), bg="#001F3F", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All", command=self.fetch_data,
                             width=12, font=("times new roman", 12, "bold"), bg="#001F3F", fg="white")
        showAll_btn.grid(row=0, column=4, padx=5)

        # ==================================================TABLE FRAME==========================================================
        table_frame = Frame(right_frame, bd=2, bg="#0b0f2e", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_tabel = ttk.Treeview(
            table_frame,
            columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
                     "dob", "email", "Phone_no", "address", "photo"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)

        # Headings
        self.student_tabel.heading("dep", text="Department")
        self.student_tabel.heading("course", text="Course")
        self.student_tabel.heading("year", text="Year")
        self.student_tabel.heading("sem", text="Semester")
        self.student_tabel.heading("id", text="StudentID")
        self.student_tabel.heading("name", text="Name")
        self.student_tabel.heading("div", text="Division")
        self.student_tabel.heading("roll", text="Roll_No")
        self.student_tabel.heading("gender", text="Gender")
        self.student_tabel.heading("dob", text="DOB")
        self.student_tabel.heading("email", text="Email")
        self.student_tabel.heading("Phone_no", text="Phone_NO")
        self.student_tabel.heading("address", text="Address")
        self.student_tabel.heading("photo", text="PhotoSampleStatus")

        self.student_tabel["show"] = "headings"

        # Column widths
        for col in ("dep", "course", "year", "sem", "id", "name", "div", "roll",
                    "gender", "dob", "email", "Phone_no", "address"):
            self.student_tabel.column(col, width=100)
        self.student_tabel.column("photo", width=0, stretch=False)  # hidden but accessible

        self.student_tabel.pack(fill=BOTH, expand=1)
        self.student_tabel.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    #================================Function decoration==========================

    def add_data(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror(title="Error",message="All Fields are required.",parent=self.root)
        else:
            try:
                conn = psycopg2.connect(
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                    database=os.getenv("DB_NAME"),
                    user=os.getenv("db_user"),
                    password=os.getenv("DB_PASSWORD")
                )
                my_cursor = conn.cursor()

                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_dep.get(),
                                                                            self.var_course.get(),
                                                                            self.var_year.get(),
                                                                            self.var_semester.get(),
                                                                            self.var_std_id.get(),
                                                                            self.var_std_name.get(),
                                                                            self.var_div.get(),
                                                                            self.var_roll.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_dob.get(),
                                                                            self.var_email.get(),
                                                                            self.var_phone.get(),
                                                                            self.var_address.get(),
                                                                            self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student detail has been added successfully",parent = self.root)
            except Exception as es:
                print(es)
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root )

#=====================================Fetch Data================================#
    def fetch_data(self):
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("db_user"),
            password=os.getenv("DB_PASSWORD")
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!= 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in data:
                self.student_tabel.insert("",END,values=i)
            conn.commit()
        conn.close()

#======================Get Cursor=====================#
    def get_cursor(self, event=""):
        cursor_focus = self.student_tabel.focus()
        content = self.student_tabel.item(cursor_focus)
        data = content["values"]

        if not data or len(data) < 13:
            return

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(str(data[4]))
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(str(data[7]))
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(str(data[11]))
        self.var_address.set(data[12])
        self.var_radio1.set(data[13])  # PhotoSampleStatus (hidden column)

    #=========================Update Function======================
    def update_data(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror(title="Error",message="All Fields are required.",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update",message="Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = psycopg2.connect(
                        host=os.getenv("DB_HOST"),
                        port=os.getenv("DB_PORT"),
                        database=os.getenv("DB_NAME"),
                        user=os.getenv("db_user"),
                        password=os.getenv("DB_PASSWORD")
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        'UPDATE student SET "Dep"=%s, "course"=%s, "year"=%s, "semester"=%s, "Name"=%s, "Division"=%s, "Roll"=%s, "Gender"=%s, "Dob"=%s, "Email"=%s, "Phone"=%s, "Address"=%s, "PhotoSample"=%s WHERE "Student_ID"=%s',
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        )
                    )



                else:
                    if not Update:
                        return
                messagebox.showinfo("Success",message="Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                print(es)
                messagebox.showerror("Error",message=f"Due to :{es}",parent=self.root)

#=================================Delete Function==============================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent = self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page",message="Do you want to delete this student",parent=self.root)
                if delete > 0 :
                    conn = psycopg2.connect(
                        host=os.getenv("DB_HOST"),
                        port=os.getenv("DB_PORT"),
                        database=os.getenv("DB_NAME"),
                        user=os.getenv("db_user"),
                        password=os.getenv("DB_PASSWORD")
                    )
                    my_cursor = conn.cursor()
                    sql = 'delete from student where "Student_ID"=%s'
                    val =(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted the student details",parent=self.root)
            except Exception as es:
                print(es)
                messagebox.showerror("Error",message=f"Due to :{es}",parent=self.root)
#=============================================reset Function=====================================
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_course.set("select Course")
        self.var_year.set("select Year")
        self.var_semester.set("select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

#================================Generate data set Take Photo Samples=========================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror(title="Error",message="All Fields are required.",parent=self.root)
        else:
            try:

                conn = psycopg2.connect(
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                    database=os.getenv("DB_NAME"),
                    user=os.getenv("db_user"),
                    password=os.getenv("DB_PASSWORD")
                    )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result =my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id+=1
                my_cursor.execute(
                    'UPDATE student SET "Dep"=%s, "course"=%s, "year"=%s, "semester"=%s, "Name"=%s, "Division"=%s, "Roll"=%s, "Gender"=%s, "Dob"=%s, "Email"=%s, "Phone"=%s, "Address"=%s, "PhotoSample"=%s WHERE "Student_ID"=%s',
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
#===========================Load predifiend data on face Frontal from Open cv=======================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                cap =cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","generating data set completed successfully")
            except Exception as es:
                print(es)
                messagebox.showerror("Error", message=f"Due to :{es}", parent=self.root)

    # ===================================search function=======================================
    def search_data(self):
        if self.var_search_by.get() == "Select" or self.var_search_txt.get().strip() == "":
            messagebox.showerror("Error", "Please select a search type and enter search text", parent=self.root)
            return
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("db_user"),
                password=os.getenv("DB_PASSWORD")
            )
            my_cursor = conn.cursor()

            search_field_map = {
                "Roll_No": '"Roll"',
                "Phone_No": '"Phone"'
            }

            selected_field = self.var_search_by.get()
            if selected_field not in search_field_map:
                messagebox.showerror("Error", "Invalid search type selected", parent=self.root)
                conn.close()
                return

            query = f"SELECT * FROM student WHERE {search_field_map[selected_field]} = %s"
            my_cursor.execute(query, (self.var_search_txt.get(),))
            data = my_cursor.fetchall()

            self.student_tabel.delete(*self.student_tabel.get_children())
            if data:
                for row in data:
                    self.student_tabel.insert("", END, values=row)
            else:
                messagebox.showinfo("Result", "No record found", parent=self.root)

            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__== "__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()

