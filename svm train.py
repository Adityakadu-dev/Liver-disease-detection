from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("Liver Disease Detection System")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++
image2 = Image.open('1.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)

 # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Liver Disease Detection System", font=('times', 35,' bold '), height=1, width=60,bg="#50C878",fg="Black")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv(r"indian_liver_patient.csv")



data = data.dropna()

le = LabelEncoder()



def Data_Preprocessing():
    data = pd.read_csv(r"indian_liver_patient.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['Age'] = le.fit_transform(data['Age'])
    data['Gender'] = le.fit_transform(data['Gender'])
    data['Total_Bilirubin'] = le.fit_transform(data['Total_Bilirubin'])
    data['Direct_Bilirubin'] = le.fit_transform(data['Direct_Bilirubin'])
    data['Alkaline_Phosphotase'] = le.fit_transform(data['Alkaline_Phosphotase'])
    data['Alamine_Aminotransferase'] = le.fit_transform(data['Alamine_Aminotransferase'])

    data['Aspartate_Aminotransferase'] = le.fit_transform(data['Aspartate_Aminotransferase'])
    data['Total_Protiens'] = le.fit_transform(data['Total_Protiens'])   
    data['Albumin'] = le.fit_transform(data['Albumin'])
    data['Albumin_and_Globulin_Ratio'] = le.fit_transform(data['Albumin_and_Globulin_Ratio'])   
  

    """Feature Selection => Manual"""
    x = data.drop(['prediction'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['prediction']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=213, y=85)


def Model_Training():
    data = pd.read_csv(r"indian_liver_patient.csv")
    data.head()

    data = data.dropna()


    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['Age'] = le.fit_transform(data['Age'])
    data['Gender'] = le.fit_transform(data['Gender'])
    data['Total_Bilirubin'] = le.fit_transform(data['Total_Bilirubin'])
    data['Direct_Bilirubin'] = le.fit_transform(data['Direct_Bilirubin'])
    data['Alkaline_Phosphotase'] = le.fit_transform(data['Alkaline_Phosphotase'])
    data['Alamine_Aminotransferase'] = le.fit_transform(data['Alamine_Aminotransferase'])

    data['Aspartate_Aminotransferase'] = le.fit_transform(data['Aspartate_Aminotransferase'])
    data['Total_Protiens'] = le.fit_transform(data['Total_Protiens'])   
    data['Albumin'] = le.fit_transform(data['Albumin'])
    data['Albumin_and_Globulin_Ratio'] = le.fit_transform(data['Albumin_and_Globulin_Ratio'])   
    

    """Feature Selection => Manual"""
    x = data.drop(['prediction'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['prediction']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=123)

    from sklearn.tree import DecisionTreeClassifier
    svcclassifier = DecisionTreeClassifier()
    svcclassifier.fit(x_train, y_train)
    y_pred = svcclassifier.predict(x_test)
    

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as model2.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"model2.joblib")
    print("Model saved as model2.joblib")



def call_file():
    from subprocess import call
    call(["python", "Check.py"])


def window():
    root.destroy()

button2 = tk.Button(root, foreground="black", background="#50C878", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
button2.place(x=20, y=150)

# button3 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Model Training", command=Model_Training, width=15, height=2)
# button3.place(x=20, y=170)

button4 = tk.Button(root, foreground="black", background="#50C878", font=("Tempus Sans ITC", 14, "bold"),
                    text=" Prediction", command=call_file, width=15, height=2)
button4.place(x=20, y=250)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=20, y=350)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''