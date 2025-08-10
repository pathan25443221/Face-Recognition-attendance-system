from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import psycopg2
import cv2
import os
import csv
from tkinter import filedialog
MY_DATA =[]

class Attendance:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

#=================Variables================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_course=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # img = Image.open(r"college_images\iStock-182059956_18390_t12.jpg")
        # img = img.resize((800, 200))
        # self.photo_img = ImageTk.PhotoImage(img)
        # f_lbl = Label(self.root, image=self.photo_img)
        # f_lbl.place(x=0, y=0, width=800, height=200)
        #
        # # second img
        # img1 = Image.open(r"college_images\smart-attendance.jpg")
        # img1 = img1.resize((800, 200))
        # self.photo_img1 = ImageTk.PhotoImage(img1)
        # f_lbl = Label(self.root, image=self.photo_img1)
        # f_lbl.place(x=800, y=0, width=800, height=200)

        img3 = Image.open(r"college_images\ChatGPT Image Jul 10, 2025, 11_25_31 AM.png")
        img3 = img3.resize((1530, 790))
        self.photo_img3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photo_img3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="#001F3F",fg="white")
        title_lbl.place(x=0, y=0, width=1530,  height=45)

        main_frame = Frame(bg_img, bd=2, bg="#0b0f2e")
        main_frame.place(x=10, y=150, width=1480, height=520)

#_______________________LEFT LABEL FRAME_____________________________

        left_frame= LabelFrame(main_frame,bd=2,bg="#0b0f2e",fg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=505)

        img_left = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130))
        self.photo_img_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.photo_img_left)
        f_lbl.place(x=5, y=0, width=718, height=130)


        left_inside_frame = Frame(left_frame, bd=2,relief=RIDGE , bg="#0b0f2e")
        left_inside_frame.place(x=3, y=135,width=720, height=340)

#===========================================Labels and Entry====================================#

        # Student ID
        attendanceID_label = Label(left_inside_frame, text="AttendanceID:", font=("comicsansns", 13, "bold"),
                                bg="#001F3F",fg="white")
        attendanceID_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id,
                                    font=("comicsansns", 13, "bold"), )
        attendanceID_entry.grid(row=0, column=1,padx=10,pady=5, sticky=W)

        # Roll
        rolllabel = Label(left_inside_frame, text="Roll:", font=("comicsansns", 13, "bold"),
                                bg="#001F3F",fg="white")
        rolllabel.grid(row=0, column=2,pady=8)

        atten_roll     = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll, width=20,
                                    font=("comicsansns", 13, "bold"), )
        atten_roll.grid(row=0, column=3,pady=8)

        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("comicsansns", 13, "bold"),
                                   bg="#001F3F",fg="white")
        name_label.grid(row=1, column=0)

        name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name,
                                       font=("comicsansns", 13, "bold"), )
        name_entry.grid(row=1, column=1, pady=8)

        # Department
        deplabel = Label(left_inside_frame, text="Department:", font=("comicsansns", 13, "bold"),
                           bg="#001F3F",fg="white")
        deplabel.grid(row=1, column=2)

        atten_cou = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_course,
                               font=("comicsansns", 13, "bold"), )
        atten_cou.grid(row=1, column=3, pady=8)

        # Time
        timelabel = Label(left_inside_frame, text="Time:", font=("comicsansns", 13, "bold"),
                         bg="#001F3F",fg="white")
        timelabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time,
                              font=("comicsansns", 13, "bold"), )
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        datelabel = Label(left_inside_frame, text="Date:", font=("comicsansns", 13, "bold"),
                         bg="#001F3F",fg="white")
        datelabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date, width=20,
                              font=("comicsansns", 13, "bold"), )
        atten_date.grid(row=2, column=3, pady=8)

        # attendance
        attendance_label = Label(left_inside_frame, text="Search By:", font=("comicsansns", 13, "bold"), bg="#001F3F",fg="white")
        attendance_label.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, font=("times new roman", 13, "bold"),textvariable=self.var_atten_attendance, state="readonly", width=15)
        self.atten_status["values"] = ("Select ", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=8)

        # _______________________________________Button frame________________________________________
        btn_frame = Frame(left_inside_frame, bd=2, bg="#0b0f2e", relief=RIDGE)
        btn_frame.place(x=0, y=250, width=715, height=35)

        ex_btn = Button(btn_frame,command=self.exportCsv, text="Export csv", width=17, font=("times new roman", 13, "bold"),
                          bg="#001F3F", fg="white")
        ex_btn.grid(row=0, column=1)

        im_btn = Button(btn_frame, text="Import csv",command=self.importCsv, width=17,
                            font=("times new roman", 13, "bold"), bg="#001F3F", fg="white")
        im_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", width=17,
                            font=("times new roman", 13, "bold"), bg="#001F3F", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17,
                           font=("times new roman", 13, "bold"), bg="#001F3F", fg="white")
        reset_btn.grid(row=0, column=3)
        #_______________________RIGHT LABEL FRAME_____________________________________________________

        right_frame= LabelFrame(main_frame,bd=2,bg="#0b0f2e",fg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame = Frame(right_frame, bd=2, bg="#0b0f2e", relief=RIDGE)
        table_frame.place(x=5, y=5, width=700, height=435)

#============================Scroll Bar table=================================#
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.AttandanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","course","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttandanceReportTable.xview)
        scroll_y.config(command=self.AttandanceReportTable.yview)

        self.AttandanceReportTable.heading("id",text="Attendance ID")
        self.AttandanceReportTable.heading("roll",text="Roll")
        self.AttandanceReportTable.heading("name",text="Name")
        self.AttandanceReportTable.heading("course",text="Course")
        self.AttandanceReportTable.heading("time",text="Time")
        self.AttandanceReportTable.heading("date",text="Date")
        self.AttandanceReportTable.heading("attendance",text="Attendance")

        self.AttandanceReportTable["show"]="headings"
        self.AttandanceReportTable.column("id",width=100)
        self.AttandanceReportTable.column("roll",width=100)
        self.AttandanceReportTable.column("name",width=100)
        self.AttandanceReportTable.column("course",width=100)
        self.AttandanceReportTable.column("time",width=100)
        self.AttandanceReportTable.column("date",width=100)
        self.AttandanceReportTable.column("attendance",width=100)



        self.AttandanceReportTable.pack(fill=BOTH,expand=1)
        self.AttandanceReportTable.bind("<ButtonRelease>",self.get_cursor)
#==========================fetch data=======================
    def fetchData(self,rows):
        self.AttandanceReportTable.delete(*self.AttandanceReportTable.get_children())
        for i in rows:
            self.AttandanceReportTable.insert("",END,values=i)
    # Import csv
    def importCsv(self):
        global MY_DATA
        MY_DATA.clear()
        fln =filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as  myfile:
            csvread =csv.reader(myfile,delimiter=",")
            for i in csvread:
                MY_DATA.append(i)
            self.fetchData(MY_DATA)

    # Export csv
    def exportCsv(self):
        try:
            if len(MY_DATA)<1:
                messagebox.showerror(title="No Data!",message="No Data Found To export",parent=self.root)
                return False
            fln =filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln, mode="w", newline="")as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in MY_DATA:
                    exp_write.writerow(i)
                messagebox.showinfo(title="Data Export",message="Your Data Exported to "+ os.path.basename(fln)+" successfully")
        except Exception as es:
                print(es)
                messagebox.showerror("Error", message=f"Due to :{es}", parent=self.root)
    def get_cursor(self,event=""):
        cursor_row = self.AttandanceReportTable.focus()
        content =self.AttandanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_course.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_course.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Select")

if __name__== "__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()