from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from pathlib import * #importing path !!ถ้าไม่มีให้ pip install pathlib
import json #importing json file !!ถ้าไม่มีให้ pip install json

path = Path.cwd()
subjects = ['Calculus', 'Python Fundamental', 'Digital Fundamental', 'Foundation English', 'System Platform Administrative']
student_summary = {}

root = Tk()
root.option_add("*Font", "Bahnschrif 20 bold")
root.title("Grade Student Table")

#EN : try and catch for error that may occur in the program that cannot found the file if not found the file will create a new file
#TH : เพื่อดักจับว่าไฟล์ที่เราต้องการเปิดมีอยู่จริงหรือไม่ ถ้าไม่มีให้สร้างไฟล์ใหม่
try :
    with open(path / "student_summary.json", "r") as file:
        student_summary = json.load(file)
except FileNotFoundError:
    with open(path / "student_summary.json", "w") as file:
        json.dump(student_summary, file)

def open_student_summary():
    summary_tv.option_add("*Font", "Bahnschrif 15 bold")
    with open(path / "student_summary.json", "r") as file:
        student_summary = json.load(file)

    #looping dict to list
    count=1
    for studentid, value in student_summary.items():
        Label(summary_tv, text=studentid).grid(row=count, column=0, padx=20)
        
        for subject, value in value.items():
            Label(summary_tv, text=subject).grid(row=count, column=1, padx=20)
            Label(summary_tv, text=value[0]).grid(row=count, column=2, padx=20)
            Label(summary_tv, text=value[1]).grid(row=count, column=3, padx=20)
            count+=1
            
def grade_submit():
    std_id_sum = studentid.get()
    subj_sum = subjectname.get()
    credit_sum = credit.get()
    gpa_sum = gpa.get()

    with open(path / "student_summary.json", "r") as file:
        student_summary = json.load(file)
    if std_id_sum == "" or credit_sum == "":
            showerror("Error", "Please enter a valid Data")
    else:
        if std_id_sum not in student_summary:
            student_summary[std_id_sum] = dict()
            student_summary[std_id_sum][subj_sum] = [credit_sum, gpa_sum]
            with open(path / "student_summary.json", "w") as file:
                json.dump(student_summary, file)
        else:
            student_summary[std_id_sum][subj_sum] = [credit_sum, gpa_sum]
            with open(path / "student_summary.json", "w") as file:
                json.dump(student_summary, file)
        showinfo("Success", "Data has been saved")
    
studentid = StringVar()
subjectname = StringVar()
subjectname.set('Calculus')
credit = IntVar()
gpa = DoubleVar()

#Grid
header = Frame(root)
header.grid(row=0, column=0, columnspan=2)

menu = Frame(root)
menu.grid(row=1, column=0)

input_menu = Frame(root)
input_menu.grid(row=1, column=1)

submit_fm = Frame(root)
submit_fm.grid(row=2, column=0, columnspan=2)

#show summary frame
summary_tv = Frame(root)
summary_tv.grid(row=3, column=0, columnspan=2)
Label(summary_tv, text="StudentID").grid(row=0, column=0, padx=20)
Label(summary_tv, text="Subject").grid(row=0, column=1, padx=20)
Label(summary_tv, text="Credit").grid(row=0, column=2, padx=20)
Label(summary_tv, text="Grade").grid(row=0, column=3, padx=20)

#header zone
Label(header, text="Grade Student Table").pack()

#menu zone
Label(menu, text="StudentID : ").pack(padx=10, pady=10)
Label(menu, text="Subject : ").pack(padx=10, pady=10)
Label(menu, text="Credit : ").pack(padx=10, pady=10)
Label(menu, text="Grade : ").pack(padx=10, pady=10)

#inputmenu zone
studentid = Entry(input_menu, width=28, textvariable=studentid)
studentid.focus()
studentid.grid(column=1, row=0, padx=10, pady=10)

subjectnameLi = OptionMenu(input_menu, subjectname, *subjects)
subjectnameLi.grid(column=1, row=1, padx=10, pady=10)

credit = Entry(input_menu, textvariable=credit, width=28, justify="center")
credit.grid(column=1, row=2, padx=10, pady=10)

gpa = ttk.Combobox(input_menu, values=list(range(0, 5)), width=5)
gpa.current(0)
gpa.grid(column=1, row=3, padx=10, pady=10)

#button zone
submit_btn = ttk.Button(submit_fm, text="คำนวณ", command=grade_submit, width=20, cursor="hand2")
submit_btn.grid(padx=10, pady=10, column=0, row=0)

open_student_summary_btn = ttk.Button(submit_fm, text="เรียกดูไฟล์", command=open_student_summary, width=20, cursor="hand2")
open_student_summary_btn.grid(padx=10, pady=10, column=1, row=0)

#__main__ init
open_student_summary()
root.mainloop()

