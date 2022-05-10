import errno
import tkinter as tk
from tkinter import *

import cx_Oracle
import cx_Oracle as o
from cx_Oracle import *


from cx_Oracle import *

# create connection

con = o.connect('C##pradeep/idevelop123@localhost:1521/pandu')

print(con.version)


# create cursor
# cur = con.cursor()


# cur.execute("create table orac(incidentnumber varchar(20) NOT NULL UNIQUE, username varchar(20) NOT NULL UNIQUE, updatedby varchar(200) NOT NULL UNIQUE)")
def clear():
    first = textbox1.get()
    second = textbox2.get()
    third = textbox3.get()
    var4.set("")
    if (first and second and third != " ") or first != "" or second != "" or third != "":
        incidentnumber.set("")
        username.set("")
        createdby.set("")
        textbox1.focus()
def submit():
    cur = con.cursor()
    first = textbox1.get()
    second = textbox2.get()
    third = textbox3.get()


    if ((first=="") or (second=="") or (third=="")) or ((first==" ") or (second=="")and (third==" ")):
        var4.set("mandatory to fill up the fields")
    else:
        try:
            if (first and second and third != " ") and (first or second or third != " "):
              var4.set(first + " " + second + "   " + third)
              cur.execute("INSERT INTO qwerty VALUES ('first','second','third')")
            con.commit()
            #var4.set("database updated")

        except o.Error as err1:
            s = str(err1)
            var4.set(s)
            return True



import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry('800x600')
root.title("Degreed Utility")
root.resizable(False,False)

frame = tk.Frame(root,highlightbackground="grey", highlightthickness=0.5, pady=10, padx=10)
#frame.place( relwidth=25, relheight=10)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)



var1 = StringVar()
incidentnumber = StringVar()
var2 = StringVar()
username = StringVar()
var3 = StringVar()
createdby = StringVar()
var4 = StringVar()

label_0 = Label(frame, text="Redbadge Exception Access", width=30, font=("bold", 25))
label_0.place(x=23, y=53)

label_1 = Label(frame, text="Incident Number Ref.", width=20, font=("bold", 10))
label_1.place(x=93, y=130)
var1.set("incident number")

textbox1 = tk.Entry(frame, textvariable=incidentnumber, width=30)
textbox1.place(x=280, y=130)
textbox1.focus()
incidentnumber.set("")

label_2 = Label(frame, text="User's CEC ID", width=20, font=("bold", 10))
label_2.place(x=73, y=180)
var2.set("username")

textbox2 = tk.Entry(frame, textvariable=username, width=30)
textbox2.place(x=280, y=180)
username.set("")

label_3 = Label(frame, text="Your CEC ID", width=20, font=("bold", 10))
label_3.place(x=71, y=230)
var3.set("created by")

textbox3 = tk.Entry(frame, textvariable=createdby, width=30)
textbox3.place(x=280, y=230)
createdby.set("")

label4 = Label(root, textvariable=var4, width=60, font=("Helvetica", 9))
label4.place(x=200, y=530)


Button(root, text='Submit', highlightbackground="black", highlightthickness=3,  width=30, height=1,bd=5,relief='raised', overrelief='sunken', fg='black', command=submit).place(x=450, y=450)

Button2 = Button(root, text='Clear', highlightbackground="black", highlightthickness=3, width=30, height=1, bd=5,relief='raised', overrelief='sunken', fg='black', command=clear).place(x=120, y=450)

root.mainloop()
