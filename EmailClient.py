import re
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import os

import smtplib
from email.mime.text import MIMEText

from tkinter import *
root = Tk()


myContainer1= Frame(root)
myContainer1.grid()

my_filetypes = [('text files', '.txt')]
def Save ():
    Jmeno_souboru = filedialog.asksaveasfilename(parent=root,
                                          initialdir=os.getcwd(),
                                          title="Please select a file name for saving:",
                                          filetypes=my_filetypes)
    Otevirany_soubor = open(Jmeno_souboru, "w")
    Otevirany_soubor.write(Text.get("0.0", END))


def Open ():
    Jmeno_souboru = filedialog.askopenfilename(parent=root,
                                        initialdir=os.getcwd(),
                                        title="Please select a file:",
                                        filetypes=my_filetypes)
    Otevirany_soubor = open(Jmeno_souboru, "r")
    obsah=Otevirany_soubor.read()
    Text.delete("0.0", END)
    Text.insert("0.0", obsah)

m=Menu(root)
root.config(menu=m)

filemenu=Menu(m)
filemenu.add_command(label="Save", command=Save)
filemenu.add_command(label="Open", command=Open)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
m.add_cascade(label="File", menu=filemenu)

helpmenu=Menu(m)
helpmenu.add_command(label="SOS", command=lambda: print("Jedeme Vam na pomoc"))
m.add_cascade(label="Help", menu=helpmenu)

NapisProAdresata=Label(myContainer1)
NapisProAdresata["text"] = "TO"
NapisProAdresata["fg"] = "white"
NapisProAdresata["bg"] = "green"
NapisProAdresata["padx"] = 10
NapisProAdresata["pady"] = 10
NapisProAdresata.grid(row=0, column=0, sticky="W")

Adresat=Text(myContainer1, height=1, width=50)
Adresat.grid(row=0, column=1)

NapisProSubject=Label(myContainer1)
NapisProSubject["text"] = "SUBJECT"
NapisProSubject["fg"] = "white"
NapisProSubject["bg"] = "green"
NapisProSubject["padx"] = 10
NapisProSubject["pady"] = 10
NapisProSubject.grid(row=1, column=0, sticky="W")

Subject=Text(myContainer1, height=1, width=50)
Subject.grid(row=1, column=1)

NapisProText=Label(myContainer1)
NapisProText["text"] = "TEXT"
NapisProText["fg"] = "white"
NapisProText["bg"] = "green"
NapisProText["padx"] = 10
NapisProText["pady"] = 10
NapisProText.grid(row=2, column=0, sticky="NW")

Text=Text(myContainer1, height=20, width=50)
Text.grid(row=2, column=1)

def button1Click(event):
    answer=messagebox.askyesno("CLEAR CLEAR CLEAR","Are you ready to clear it?", parent=root)
    if answer:
        Text.delete("0.0", END)

def button2Click(event):
    zadany_email=Adresat.get("0.0", END).strip()
    if zadany_email== "":
        messagebox.showinfo("POZOR POZOR", "Please, insert an address.", parent=root)
        return

    if not re.match(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-.]+[.][a-zA-Z]{2,3}$", zadany_email):
        messagebox.showinfo("POZOR POZOR", "Your e-mail address is not valid.", parent=root)
        return

    if Subject.get("0.0", END).strip()== "":
        answer = messagebox.askyesno("A CO PREDMET?", "Are you sure to send e-mail without subject?", parent=root)
        if answer==False:
            return


    TextZpravy = Text.get("0.0", END)
    msg=MIMEText(TextZpravy)
    msg['Subject']= Subject.get("0.0", END).strip()
    msg["From"]="dada.013@seznam.cz"
    msg['To']= Adresat.get("0.0", END).strip()
    passwd=simpledialog.askstring("HESLO HESLO HESLO", "Please, insert your password", parent=root, show="*")
    if passwd==None:
        messagebox.showinfo("NIC NEPOSILAM", "Odesilani nebude", parent=root)
        return
    print(passwd)
    # s = smtplib.SMTP('smtp.seznam.cz')
    # s.starttls()
    # s.login("dada.013@seznam.cz", passwd)
    # s.send_message(msg)
    # s.quit()
    print("posilam")


tlacitka=LabelFrame(myContainer1)
tlacitka.grid(row=3, column=1)

button1=Button(tlacitka)
button1["text"]="CLEAR"
button1["background"] = "yellow"
button1["fg"] = "red"
button1["padx"] = 10
button1["pady"] = 10
button1.bind("<Button-1>", button1Click)
button1.grid(row=0, column=0)

button2=Button(tlacitka)
button2["text"]="SEND"
button2["background"] = "blue"
button2["fg"] = "white"
button2["padx"] = 20
button2["pady"] = 10
button2.bind("<Button-1>", button2Click)
button2.grid(row=0, column=1)




root.mainloop()