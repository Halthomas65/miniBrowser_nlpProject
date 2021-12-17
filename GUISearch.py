from tkinter import *
from tkinter import messagebox

W=Tk()
W.geometry('1000x700')
W.title('Project')

L1=Label(master=W,text='Input',font=('arial',20))
L1.grid(row = 0, column= 0, padx =20,pady= 0,sticky='W')
L1.place(x = 50, y = 30, height = 30, width=200)

L2=Label(master=W,text='Output',font=('arial',20))
L2.grid(row = 0, column= 1, padx =20,pady= 0,sticky='W')
L2.place(x = 500, y = 30, height = 30, width=200)


E1 = Text(master=W, height = 5, width = 52, font=('arial',15))
E1.grid(row = 1,column = 0,padx = 20,pady = 5,stick = 'w')
E1.place(x = 50, y = 70, height = 500, width= 300)


def B1_click():
    print(E1.get("1.0", "end-1c"))

def B2_click():
    E1.delete('1.0', END)

def B3_click():
     E1.delete('1.0', END)
     

def B4_click():
    W.destroy()

B1 = Button(master = W,text = 'TEST',font=('arial',13),bg = 'blue', fg = 'white',width = 12,command=B1_click)
B1.grid(row = 3,column = 3,padx = 30,pady = 20,stick = 'w')
B1.place(x = 850, y =100)

B2 = Button(master = W,text = 'DELETE INPUT',font=('arial',13),bg = 'blue', fg = 'white',width = 12,command=B2_click)
B2.grid(row = 6,column = 3,padx = 30,pady = 20,stick = 'w')
B2.place(x = 850, y =200)

B3 = Button(master = W,text = 'DELETE ALL',font=('arial',13),bg = 'blue', fg = 'white',width = 12,command=B3_click)
B3.grid(row = 9,column = 3,padx = 30,pady = 20,stick = 'w')
B3.place(x = 850, y =300)

B4 = Button(master = W,text = 'EXIT',font=('arial',13),bg = 'red', fg = 'black',width = 12,command=B4_click)
B4.grid(row = 9,column = 3,padx = 30,pady = 20,stick = 'w')
B4.place(x = 850, y =650)

W.mainloop()