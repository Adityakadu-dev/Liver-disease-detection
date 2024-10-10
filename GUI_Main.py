# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:26:07 2024

@author: admin
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
#from tkvideo import tkvideo

##############################################+=============================================================

root = tk.Tk()
#root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('face.db')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Liver Disease Detection System ")

image2 = Image.open('7.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)
lbl = tk.Label(root, text="Liver Disease Detection System", font=('times', 35,' bold '), width=60,height=1,bg="black",fg="white")
lbl.place(x=0, y=0)


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 =Image.open('6.jpg')
# image2 =image2.resize((w,h), Image.ANTIALIAS)

# background_image=ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0) #, relwidth=1, relheight=1)



  #################################################################################################################
def reg():
    print("Registration")
    from subprocess import call
    call(["python", "registration.py"]) 



def Log():
    print("Login")
    from subprocess import call
    call(["python", "log.py"])
 



def window():
    root.destroy()


button1 = tk.Button(root, text="Registration", command=reg,width=20, height=1, font=('times', 15, ' bold '),bg="black",fg="white")
button1.place(x=400, y=310)

button2 = tk.Button(root, text="Login", command=Log,width=20, height=1, font=('times', 15, ' bold '),bg="black",fg="white")
button2.place(x=600, y=410)


##
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=10, y=280)


exit = tk.Button(root, text="Exit", command=window, width=20, height=1, font=('times', 15, ' bold '),bg="green",fg="white")
exit.place(x=800, y=510)



root.mainloop()