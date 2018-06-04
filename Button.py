from tkinter import *
root = Tk()


myContainer1= Frame(root)
myContainer1.grid()

m=Menu(root)
root.config(menu=m)

filemenu=Menu(m)
filemenu.add_command(label="New", command=lambda: print("Novy soubor"))
filemenu.add_command(label="Open", command=lambda: print("Oteviraaaaam"))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
m.add_cascade(label="File", menu=filemenu)

helpmenu=Menu(m)
helpmenu.add_command(label="SOS", command=lambda: print("Jedeme Vam na pomoc"))
m.add_cascade(label="Help", menu=helpmenu)


napis=Label(myContainer1)
napis["text"] = "Uz umim tlacitka"
napis["fg"] = "white"
napis["bg"] = "green"
napis["padx"] = 10
napis["pady"] = 10
napis.grid(row=0, column=0, sticky="E")
# vzdycky musim objekt zabalit - ukoncit jej "grid"

oramovani=LabelFrame(myContainer1)
oramovani["padx"] = 20
oramovani["pady"] = 20
oramovani["text"] = "Ramujeme pribeh"
oramovani["labelanchor"] = "nw"
oramovani["bg"] = "violet"
oramovani["fg"] = "blue"
oramovani["relief"] = SUNKEN
oramovani.grid(row=1, column=0)

text=Text(oramovani)
text["background"]= "pink"
text.insert(END, "Vlozte text:")
text.focus_set()
text.grid(row=2, column=0)

def button1Click(event):
    text.insert(END, "Zmacknuto")

tlacitka=LabelFrame(myContainer1)
tlacitka.grid(row=2, column=0)

button1=Button(tlacitka)
button1["text"]="Hello World"
button1["background"] = "yellow"
button1["fg"] = "red"
button1["padx"] = 10
button1["pady"] = 10
button1.bind("<Button-1>", button1Click)
button1.grid(row=0, column=0)

button2=Button(tlacitka)
button2["text"]="Look"
button2["background"] = "blue"
button2["fg"] = "white"
button2["padx"] = 20
button2["pady"] = 10
button2.bind("<Button-1>", button1Click)
button2.grid(row=0, column=1)


button3=Button(tlacitka)
button3["text"]="Bye"
button3["background"] = "black"
button3["fg"] = "white"
button3["padx"] = 20
button3["pady"] = 10
button3.bind("<Button-1>", button1Click)
button3.grid(row=0, column=3)



root.mainloop()
# vzdycky az na konci programu