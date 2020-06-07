from tkinter import *
from tkinter import messagebox
import pyflames
root=Tk()
root.geometry('500x450')
root.configure(bg="#C4D8F8")
root.title('Flames calculator')
root.resizable(0,0)
frame=Frame(root)
frame.pack(side=TOP)
lbl_title = Label(frame, text="FLAMES", font="Arial 15 bold", bg="orange",  width = 300,fg="green")
lbl_title.pack(fill=X)
first=Label(root,text="First name     :-",font="Arial 15 bold",bg="#C4D8F8",fg="#F81740")
first.place(x=50,y=120)
e1=Entry(root,width=30)
e1.place(x=210,y=120)
first=Label(root,text="second name :-",font="Arial 15 bold",bg="#C4D8F8",fg="#F81740")
first.place(x=50,y=170)
e2=Entry(root,width=30)
e2.place(x=210,y=170)
def relation():
    if(e1.get()=='' or e2.get()==''):
        messagebox.showinfo("required","please fill the details")
    else:
        word=pyflames.pyflames()
        stat=word.flames(e1.get(),e2.get())
        messagebox.showinfo("relation",stat) 
b1=Button(root,text="status",bg="pink",font="Arial 15 bold",activebackground="#13BFCA",command=relation)
b1.place(x=250,y=250)
root.mainloop()
