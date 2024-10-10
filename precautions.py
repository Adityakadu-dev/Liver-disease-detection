import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModel 
from keras import optimizers
import sqlite3
from tensorflow.keras.optimizers import SGD
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Liver Disease Detection System")



bg = Image.open("l5.jpg")

# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

# frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=280, height=200, font=('times', 14, ' bold '),bg="pink")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=0, y=0)

# calling the function
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="#6AABD2")
canvas.pack()
canvas.place(x=0, y=0)
text_var="Liver Disease Detection System"
text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 50
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling
  
               
               
      
import webbrowser
# Create a function to retrieve the selected item from the drop-down list
def get_selected_item():
    selected_item = combobox.get()  # Get the selected item from the Combobox
    print(selected_item)
    #label.config(text=f"Selected Item: {selected_item}")  # Update the label text with the selected item
    if (selected_item=='Viral hepatitis'):
        label=tk.Label(root,text=''' Viral hepatitis   ''',width=40,font=('times',20,'bold'),bg="white",fg="black")
        label.place(x=700,y=100)
        label=tk.Label(root,text='''                       
        Symptoms:- fever, fatigue, loss of appetite, nausea, vomiting, abdominal pain, dark urine, \n light-colored stools, joint pain, and jaundice\n
        precautions:-entecavir (Baraclude), tenofovir (Viread), lamivudine (Epivir), adefovir (Hepsera) and telbivudine 
        ''',width=90,bg="#77BFC7",fg="black",height=33)
        label.place(x=700,y=200)
        def open_google():
            webbrowser.open("https://www.practo.com/pune/treatment-for-liver-disease")
        label = tk.Label(root, text="https://www.practo.com/pune/treatment-for-liver-disease", fg="blue", cursor="hand2")
        label.place(x=850,y=550)

# Bind the label to the function that opens Google when clicked
        label.bind("<Button-1>", lambda e: open_google())


        
    elif (selected_item=='Abnormal condition '):
        label=tk.Label(root,text='''Abnormal condition ''',width=40,font=('times',20,'bold'),bg="#6AABD2",fg="black")
        label.place(x=700,y=100)
        label=tk.Label(root,text='''
        Symptoms:- Skin and eyes that appear yellowish (jaundice),Abdominal pain and swelling,\nSwelling in the legs and ankles,Itchy skin,\nDark urine color,Pale stool color,Chronic fatigue,\nNausea or vomiting,Loss of appetite,Tendency to bruise easily.\n 
        precautions:- Avoiding alcohol or medications that can harm your liver''',bg="#77BFC7",fg="black",width=90,height=33)
        label.place(x=700,y=200)
        def open_google():
            webbrowser.open("https://www.practo.com/pune/treatment-for-liver-disease")
        label = tk.Label(root, text="https://www.practo.com/pune/treatment-for-liver-disease", fg="blue", cursor="hand2")
        label.place(x=850,y=550)

# Bind the label to the function that opens Google when clicked
        label.bind("<Button-1>", lambda e: open_google())
        
    elif (selected_item=='Acute hepatitis'):
         label=tk.Label(root,text=''' Acute hepatitis''',width=40,font=('times',20,'bold'),bg="white",fg="black")
         label.place(x=700,y=100)
         label=tk.Label(root,text='''
         symptoms:-fever, malaise, fatigue, loss of appetite, vomiting, diarrhea, and abdominal pain.\n
         precautions:-Lamivudine, adefovir dipivoxil
         
                        ''',bg="#77BFC7",fg="black",width=90,height=33) 
         label.place(x=700,y=200)
         def open_google():
             webbrowser.open("https://www.practo.com/pune/treatment-for-liver-disease")
         label = tk.Label(root, text="https://www.practo.com/pune/treatment-for-liver-disease", fg="blue", cursor="hand2")
         label.place(x=850,y=550)

 # Bind the label to the function that opens Google when clicked
         label.bind("<Button-1>", lambda e: open_google())
   
         
   
    



# Create a Label
label = tk.Label(root, text='''       Select an liver Disease:         ''',font=('times',15, ' bold '),bg="#6AABD2",fg="black",height=2,bd=5)
label.place(x=10,y=150)

# Create a Combobox (Drop-down list)
options = ['Viral hepatitis','Abnormal condition ','Acute hepatitis']  # List of options
selected_option = tk.StringVar()  # Variable to hold selected item
combobox = ttk.Combobox(root, textvariable=selected_option, values=options, state="readonly",font=('times',15, ' bold '))
combobox.place(x=30,y=250)

# Create a Button to get the selected item
button = tk.Button(root, text=" Get Info", command=get_selected_item,width=15, height=2, font=('times', 15, ' bold '),bg="#6AABD2",fg="black")
button.place(x=30,y=400)




#################################################################################################################
def window():
    root.destroy()



# button2 = tk.Button(frame_alpr, text="Amla", command=Amla, width=20, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button2.place(x=10, y=70)




exit = tk.Button(root, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="#6AABD2",fg="white")
exit.place(x=30, y=600)



root.mainloop()

