from tkinter import *

def fun1():
     x=c.get()
     y=x[::-1]
     d.delete(0,END)
     d.insert(1,y)
     print(x)


root = Tk()
root.title("Converter")
root.geometry('350x200')
 
a = Label(root, text="hello world")
a.grid(column=0, row=0)
 
c = Entry(root,width=10)
c.grid(column=1, row=0,padx=10)

d = Entry(root,width=10)
d.grid(column=1, row=2)
 
b = Button(root, text="Convert", command=fun1)
b.grid(column=1, row=1,pady=20)
 
root.mainloop()