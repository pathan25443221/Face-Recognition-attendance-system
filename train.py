from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import psycopg2
import cv2
import os
import numpy as np

class Train:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Times New Roman", 30, "bold"), bg="#001F3F", fg="white")
        # title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_images\train_data_no_button_1920x1080.png")
        img_top = img_top.resize((1530, 800))
        self.photo_img_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photo_img_top)
        f_lbl.place(x=0, y=0, width=1530, height=800)

        # Button
        b1_1 = Button(self.root,command=self.train_classifier, text="TRAIN DATA", cursor="hand2",font=("times new roman", 24, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=570, y=562, width=390, height=60)


        # img_bottom = Image.open(r"college_images\train_data_no_button_1920x1080.png")
        # img_bottom = img_bottom.resize((1530, 340))
        # self.photo_img_bottom = ImageTk.PhotoImage(img_bottom)
        # f_lbl = Label(self.root, image=self.photo_img_bottom)
        # f_lbl.place(x=0, y=430, width=1530, height=340)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces =[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

#=================================Train the classifier and save==============================#
        clf =cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!",parent =self.root)



































if __name__ == "__main__":
        root = Tk()
        obj = Train(root)
        root.mainloop()