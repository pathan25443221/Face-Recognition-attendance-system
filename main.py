from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Student import Student
import os
from train import Train
from face_recoginition import Face_recognition
from attendance import Attendance


class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ----------- TITLE -----------
        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("Times New Roman", 30, "bold"), bg="#001F3F", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=60)

        # ----------- BACKGROUND IMAGE -----------
        bg_img = Image.open(r"college_images\ChatGPT Image Jul 10, 2025, 11_25_31 AM.png")
        bg_img = bg_img.resize((1530, 730))
        self.photo_bg = ImageTk.PhotoImage(bg_img)
        bg_lbl = Label(self.root, image=self.photo_bg)
        bg_lbl.place(x=0, y=60, width=1530, height=730)

        # ----------- Load All Icons -----------
        icons = {
            "student": "ChatGPT Image Jul 10, 2025, 05_10_27 PM.png",
            "face": "ChatGPT Image Jul 10, 2025, 12_10_10 PM.png",
            "attendance": "ChatGPT Image Jul 10, 2025, 12_03_57 PM.png",
            "train": "ChatGPT Image Jul 10, 2025, 12_05_28 PM.png",
            "photos": "ChatGPT Image Jul 10, 2025, 12_06_54 PM.png",
            "exit": "ChatGPT Image Jul 10, 2025, 12_08_24 PM.png"
        }

        self.icons = {}
        for key, filename in icons.items():
            img = Image.open(f"college_images/{filename}")
            img = img.resize((220, 220))
            self.icons[key] = ImageTk.PhotoImage(img)

        # ----------- Button Placement (3x2 Grid with Hover Effects) -----------

        self.buttons = {}

        def create_button(name, command, x, y):
            btn = Button(bg_lbl, image=self.icons[name], cursor="hand2", bd=0, highlightthickness=0, command=command, bg="black", activebackground="black")
            btn.place(x=x, y=y, width=220, height=220)

            # Add hover effect
            def on_enter(e): btn.config(bg="#00bfff")
            def on_leave(e): btn.config(bg="black")

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

            self.buttons[name] = btn

        # First row
        create_button("student", self.student_details, 300, 130)
        create_button("face", self.Face_recognition, 620, 130)
        create_button("attendance", self.Attendance, 940, 130)

        # Second row
        create_button("train", self.train_data, 300, 420)
        create_button("photos", self.open_img, 620, 420)
        create_button("exit", self.exit_app, 940, 420)

    # ----------- Functional Methods -----------
    def open_img(self):
        os.startfile("data")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def Face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def exit_app(self):
        self.root.quit()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()
