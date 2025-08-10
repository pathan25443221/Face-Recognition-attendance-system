from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import psycopg2
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np

class Face_recognition:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="black",fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_left = Image.open(r"college_images\face_detector1.JPG")
        img_left = img_left.resize((650, 700))
        self.photo_img_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(self.root, image=self.photo_img_left)
        f_lbl.place(x=0, y=45, width=650, height=700)

        img_right = Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.JPG")
        img_right = img_right.resize((950, 700))
        self.photo_img_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(self.root, image=self.photo_img_right)
        f_lbl.place(x=650, y=45, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl,command=self.face_recog, text="DETECT FACE", cursor="hand2",font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=370, y=615, width=200, height=30)


#===============================Attendance=================================#
    def mark_attendance(self,i,r,n,c,):
        with open("Pathan.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list =[]
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{c},{dtString},{d1}, Present")







#===============================face recognition============================#

    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features =classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence =int((100*(1-predict/300)))

                conn = psycopg2.connect(
                        host="localhost",
                        port="5432",
                        database="face_recognizer",
                        user="postgres",
                        password="1234"
                    )
                my_cursor = conn.cursor()

                my_cursor.execute('SELECT "Name" FROM student WHERE "Student_ID" = %s', (str(id),))
                n = my_cursor.fetchone()
                print("DEBUG: Face ID returned:", id)
                print("DEBUG: Name fetched:", n)
                n = n[0] if n else "Unknown"

                my_cursor.execute('select "Roll" from student where "Student_ID" = %s', (str(id),))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute('select "course" from student where "Student_ID" = %s', (str(id),))
                c = my_cursor.fetchone()
                c = c[0] if c else "Unknown"

                my_cursor.execute('select "Student_ID" from student where "Student_ID" = %s', (str(id),))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                if confidence > 75:
                    cv2.putText(img,f"ID: {i}",(x,y-75),cv2.FONT_HERSHEY_DUPLEX,0.9,(128,230,255),3)
                    cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_DUPLEX,0.9,(128,230,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_DUPLEX,0.9,(128,230,255),3)
                    cv2.putText(img,f"Course: {c}",(x,y-5),cv2.FONT_HERSHEY_DUPLEX,0.9,(128,230,255),3)
                    self.mark_attendance(i,r,n,c)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord = [x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap =cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to grab frame from webcam.")
                break  # Or continue, or retry logic

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
        root = Tk()
        obj = Face_recognition(root)
        root.mainloop()