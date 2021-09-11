#create student information form using TKinter.

import tkinter as tk
from tkinter import *
win=tk.Tk(className="StudentInfoForm......")

#-name,address,email,schoolname,stding in,year,dob,gender,schooltype- Marathi medium,english,convent,semi

win.geometry("1000x1000")
label=tk.Label(win,text="***** STUDENT INFORMATION FORM *****").place(x=380,y=10)
Name=tk.Label(win,text="NAME").place(x=35,y=60)
e1=tk.Entry(win).place(x=170,y=60)
Address=tk.Label(win,text="ADDRESS").place(x=35,y=90)
e2=tk.Entry(win).place(x=170,y=90)
Email=tk.Label(win,text="EMAIL").place(x=35,y=120)
e3=tk.Entry(win).place(x=170,y=120)
Schoolname=tk.Label(win,text="SCHOOL NAME ").place(x=35,y=150)
e4=tk.Entry(win).place(x=170,y=150)
Stding_in_year=tk.Label(win,text="STUDING IN YEAR ").place(x=35,y=180)
e5=tk.Entry(win).place(x=170,y=180)
dob=tk.Label(win,text="DATE OF BIRTH ").place(x=35,y=210)
e6=tk.Entry(win).place(x=170,y=210)

Gender=tk.Label(win,text="  1]  SELECT GENDER ").place(x=35,y=280)
radio1=tk.Radiobutton(win,text="Male",value=0).place(x=120,y=310)
radio2=tk.Radiobutton(win,text="Female",value=1).place(x=320,y=310)

schooltype=tk.Label(win,text="  2]  SCHOOL TYPE ").place(x=35,y=360)
radio3=tk.Radiobutton(win,text="Marathi Medium",value=0).place(x=120,y=390)
radio4=tk.Radiobutton(win,text="English Medium",value=0).place(x=320,y=390)
radio5=tk.Radiobutton(win,text="Convent Medium",value=0).place(x=520,y=390)
radio6=tk.Radiobutton(win,text="Semi-English Medium",value=1).place(x=720,y=390)

submit=tk.Button(win,text="SUBMIT",activebackground="pink",activeforeground="purple").place(x=420,y=500)
win.mainloop()