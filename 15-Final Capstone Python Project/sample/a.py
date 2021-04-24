from tkinter import *


def raise_frame(frame):
	frame.tkraise()
	
    
def click():
	a=e1.get()
	l1=Label(f2, text='Hello'+a)
	l1.grid(row=0,column=0)



root = Tk()
f1 = Frame(root)
f2 = Frame(root)

f1.grid(row=0, column=0, sticky='news')
f2.grid(row=0, column=0, sticky='news')


Label(f1, text='Name').grid(row=0,column=0)
e1=Entry(f1, width=10)
e1.grid(row=0,column=1)

b1=Button(f1, text='get_value', command=click)
b1.grid(row=0,column=2)

b2=Button(f1, text='Submit', command=lambda:raise_frame(f2))
b2.grid(row=0,column=3)


b2=Button(f2, text='Back', command=lambda:raise_frame(f1))
b2.grid(row=1,column=1)


raise_frame(f1)
root.mainloop()