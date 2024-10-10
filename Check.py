from tkinter import *

import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

root = tk.Tk()

root.geometry("800x850+250+5")
root.title("LOAN PREDICTION")
root.configure(background="pink")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
        #####For background Image
# image2 = Image.open('p3.png')
# image2 = image2.resize((w, h), Image.ANTIALIAS)
    
# background_image = ImageTk.PhotoImage(image2)
    
# background_label = tk.Label(root, image=background_image)
    
# background_label.image = background_image
    
# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
        
        
    
    
Age = tk.IntVar()
Gender = tk.StringVar()
Total_Bilirubin = tk.IntVar()
Direct_Bilirubin= tk.IntVar()
Alkaline_Phosphotase = tk.IntVar()
Alamine_Aminotransferase = tk.IntVar()
Aspartate_Aminotransferase = tk.IntVar()
Total_Protiens= tk.IntVar()
Albumin= tk.IntVar()
Albumin_and_Globulin_Ratio = tk.IntVar()

    
   
    
    #===================================================================================================================
def Detect():
        e1= Age.get()
        print(e1)
       
        
        e2=Gender.get()
        print(e2)
        if e2=="Male":
           e2=0
        else:
           e2=1
        
        e3= Total_Bilirubin.get()
        print(e3)
       
        e4=Direct_Bilirubin.get()
        print(e4)
        
        e5=Alkaline_Phosphotase.get()
        print(e5)
       
        e6=Alamine_Aminotransferase.get()
        print(e6)
        e7=Aspartate_Aminotransferase.get()
        print(e7)
        e8=Total_Protiens.get()
        print(e8)
        e9=Albumin.get()
        print(e9)
        e10=Albumin_and_Globulin_Ratio.get()
        print(e10)
        
        
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('model2.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]])
        print(v)
        if v[0]==1:
            print("Yes")
            yes = tk.Label(root,text="liver Disease detected",background="red",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=550,y=680)
                     
        
            
        else:
            print("No")
            no = tk.Label(root, text="Disease not detected", background="green", foreground="black",font=('times', 20, ' bold '),width=20)
            no.place(x=550, y=680)
            


l1=tk.Label(root,text="Age",background="pink",font=('times', 20,' bold '),width=3,fg="black")
l1.place(x=400,y=50)
Age=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Age)
Age.place(x=800,y=50)



l2=tk.Label(root,text="Gender",background="pink",font=('times', 20, ' bold '),width=5)
l2.place(x=400,y=100)
   

monthchoosen = ttk.Combobox(root, width = 27, textvariable = Gender)

    # Adding combobox drop down list
monthchoosen['values'] = ('Female','Male')
monthchoosen.place(x=800,y=100)
    #monthchoosen.grid(column = 1, row = 2)
monthchoosen.current()






l3=tk.Label(root,text="Total_Bilirubin",background="pink",font=('times', 20, ' bold '),width=11,fg="black")
l3.place(x=400,y=150)
Total_Bilirubin=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Total_Bilirubin)
Total_Bilirubin.place(x=800,y=150)
    
l4=tk.Label(root,text="Direct_Bilirubin",background="pink",font=('times', 20, ' bold '),width=12)
l4.place(x=400,y=200)
Direct_Bilirubin=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Direct_Bilirubin)
Direct_Bilirubin.place(x=800,y=200)



l5=tk.Label(root,text="Alkaline_Phosphotase",background="pink",font=('times', 20, ' bold '),width=16,fg="black")
l5.place(x=400,y=250)
Alkaline_Phosphotase=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Alkaline_Phosphotase)
Alkaline_Phosphotase.place(x=800,y=250)



l6=tk.Label(root,text="Alamine_Aminotransferase",background="pink",font=('times', 20, ' bold '),width=20)
l6.place(x=400,y=300)
Alamine_Aminotransferase=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Alamine_Aminotransferase)
Alamine_Aminotransferase.place(x=800,y=300)

l7=tk.Label(root,text="Aspartate_Aminotransferase",background="pink",font=('times', 20, ' bold '),width=21,fg="black")
l7.place(x=400,y=350)
Aspartate_Aminotransferase=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Aspartate_Aminotransferase)
Aspartate_Aminotransferase.place(x=800,y=350)

l8=tk.Label(root,text="Total_Protiens",background="pink",font=('times', 20, ' bold '),width=11)
l8.place(x=400,y=400)
Total_Protiens=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Total_Protiens)
Total_Protiens.place(x=800,y=400)

l9=tk.Label(root,text="Albumin",background="pink",font=('times', 20, ' bold '),width=6,fg="black")
l9.place(x=400,y=450)
Albumin=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Albumin)
Albumin.place(x=800,y=450)

l10=tk.Label(root,text="Albumin_and_Globulin_Ratio",background="pink",font=('times', 20, ' bold '),width=22)
l10.place(x=400,y=500)
Albumin_and_Globulin_Ratio=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Albumin_and_Globulin_Ratio)
Albumin_and_Globulin_Ratio.place(x=800,y=500)

   




    
    
button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
button1.place(x=600,y=600)

root.mainloop()

