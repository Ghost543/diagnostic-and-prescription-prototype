import os
import sqlite3

from tkinter import *
from tkinter import  filedialog
from tkinter import messagebox
from PIL import Image,ImageTk

# from Model.main import predict
from Control.control import look

##########################################
import tensorflow as tf
import os
import caer
import canaro
import numpy as np
import cv2 as cv
import gc

###################################################
conn = sqlite3.connect('citzeen_data.db')

model = tf.keras.models.load_model('C:\\Users\\hp\\Desktop\\Peter\\gui\\Model\\model__.h5')
characters=['JOSE', 'PAUL', 'PETER']
IMG_SIZE = (100,100)
channels = 1

def __prepare(img_test):
    img = cv.imread(img_test)
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img = cv.resize(img,IMG_SIZE)
    img = caer.reshape(img,IMG_SIZE,channels)
    return img




root = Tk()
root.title("INTEGRATION OF IMAGE RECOGNITION ALGORITHM IN SURVIALANCE SYSTEM (IIRASS)")
root.configure(bg="#16c79a")
width_val = root.winfo_screenwidth()
height_val = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width_val, height_val))



def show():
    global move
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",filetypes=(("JPG File","*.jpg"),("PNG file","*.png"),("All Files","*.*")))
    move = fln
    img = Image.open(fln)
    # print(fln)
    img = img.resize((350, 200))
    img = ImageTk.PhotoImage(img)
    labe_img.configure(image=img)
    labe_img.image=img
# print(move)
def scan():
    print(move)
    global citzeen
    predictions = model.predict(__prepare(move))
    citzeen = characters[np.argmax(predictions[0])]
    print(citzeen)

    # if len(move) == 0:
    #     messagebox.showerror("Scan error","Upload Image to scan")
    # citzeen = predict(fln)

    messagebox.showinfo("Scan Complete", "Scanning Image is Complete")
    print(citzeen)

def open_citzeen_profile():
    # Toplevel object which will
    # be treated as a new window
    citzeen_win = Toplevel(root)
    print(citzeen)
    disp = "Citzeen"
    if len(citzeen) != 0:
        disp = citzeen
    disp = disp.capitalize()
    print(disp)

    cursor = conn.execute("SELECT * FROM citzeen WHERE lastname=?", (disp,))
    details = cursor.fetchone()
    conn.close()
    details = list(details)
    # sets the title of the
    # Toplevel widget
    citzeen_win.title(f"{disp} Profile")
    nin_l = Label(citzeen_win, text="NIN: ", font=("Arial Bold", 14))
    nin = Label(citzeen_win, text={details[0]}, font=("Arial Bold", 14))
    fname_l = Label(citzeen_win,text="First Name: ", font=("Arial Bold",14))
    fname = Label(citzeen_win,text={details[1]}, font=("Arial Bold",14))
    lname_l = Label(citzeen_win, text="Last Name: ", font=("Arial Bold", 14))
    lname = Label(citzeen_win, text={details[2]}, font=("Arial Bold", 14))
    address_l = Label(citzeen_win, text="Address: ", font=("Arial Bold", 14))
    adrress = Label(citzeen_win, text={details[4]}, font=("Arial Bold", 14))
    age_l = Label(citzeen_win, text="Age", font=("Arial Bold", 14))
    age = Label(citzeen_win, text={details[3]}, font=("Arial Bold", 14))
    tel_l = Label(citzeen_win, text="Telephone Number: ", font=("Arial Bold", 14))
    tel = Label(citzeen_win, text={details[5]}, font=("Arial Bold", 14))
    # sets the geometry of toplevel
    citzeen_win.geometry("%dx%d+0+0" % (width_val/2, height_val/2))

    nin_l.grid(row=0, column=0)
    nin.grid(row=0, column=1)

    fname_l.grid(row=1,column=0)
    fname.grid(row=1,column=1)
    lname_l.grid(row=2, column=0)
    lname.grid(row=2, column=1)
    address_l.grid(row=3, column=0)
    adrress.grid(row=3, column=1)
    age_l.grid(row=4, column=0)
    age.grid(row=4, column=1)
    tel_l.grid(row=5, column=0)
    tel.grid(row=5, column=1)

    # A Label widget to show in toplevel



title = Label(root,text="INTEGRATION OF IMAGE RECOGNITION ALGORITHM IN SURVIALANCE SYSTEM (IIRASS)",bg="#16c79a",fg="#11698e",font=("ALGERIAN",18))
title.place(x=0.25*width_val,y=0.01*height_val)
labe_img = Label(root)
labe_img.place(x=3.9*width_val/8,y=height_val/14)

upload_btn = Button(root,text="UPLOAD", command=show, width=25,height=3,bg="#114e60",fg="#f4eee8",font=("Arial Bold", 11)).place(x=width_val/2, y=height_val/3)


scan_btn = Button(text="SCAN", width=25,height=3, bg="#114e60",command=scan,fg="#f4eee8",font=("Arial Bold", 11)).place(x=width_val/4, y=2*height_val/4)
view_btn = Button(text="VIEW", width=25,height=3,command=open_citzeen_profile,bg="#114e60",fg="#f4eee8",font=("Arial Bold", 11)).place(x=3*width_val/4, y=2*height_val/4)

root.mainloop()