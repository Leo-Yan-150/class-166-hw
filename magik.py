from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Drawing even crazier stuff with code that I totally know")
root.geometry("1000x1000")

labelsx=Label(root,text="Start X")
labelsy=Label(root,text="Start Y")
labelex=Label(root,text="End X")
labeley=Label(root,text="End Y")
labelcolor=Label(root,text="Choose a color")

labelcolors=["red","lightblue","lime","yellow"]
combocolor=ttk.Combobox(root, state="r", values=labelcolors, width=10)
inputsx=Entry(root)
inputsy=Entry(root)
inputex=Entry(root)
inputey=Entry(root)

canva = Canvas(root,width=900,height=800,bg="aliceblue",highlightbackground="black")
canva.pack()
labelsx.place(relx=0.1,rely=0.85,anchor=CENTER)
labelsy.place(relx=0.3,rely=0.85,anchor=CENTER)
labelex.place(relx=0.5,rely=0.85,anchor=CENTER)
labeley.place(relx=0.7,rely=0.85,anchor=CENTER)
labelcolor.place(relx=0.9,rely=0.85,anchor=CENTER)
combocolor.place(relx=0.9,rely=0.9,anchor=CENTER)
inputsx.place(relx=0.1,rely=0.9,anchor=CENTER)
inputex.place(relx=0.5,rely=0.9,anchor=CENTER)
inputsy.place(relx=0.3,rely=0.9,anchor=CENTER)
inputey.place(relx=0.7,rely=0.9,anchor=CENTER)

root.mainloop()