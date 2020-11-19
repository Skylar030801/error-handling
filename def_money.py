from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Qualify")
root.geometry("300x300")

e_amount=Entry(root)
e_amount.grid(row=2,column=1)
label_main=Label(root,text="Please Enter Your Amount.")
label_main.grid(row=1,column=1)



def check():
    amount=int(e_amount.get())
    try:
        if amount < 3000:
            raise ValueError(messagebox.showinfo('Message',"Please deposit more funds"))

    except ValueError:
        print(ValueError)
        e_amount.delete(0,END)

    else:
        (messagebox.showinfo('Message',"CONGRADULATIONS!!! YOU qualify for a trip to Malasia"))




b_verify=Button(root,text="Check", command=check)
b_verify.grid(row=3,column=1)

root.mainloop()
