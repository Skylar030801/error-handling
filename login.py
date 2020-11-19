from tkinter import *
from tkinter import messagebox


root =Tk()
root.title("Login verify")
root.geometry("300x300")


label_user=Label(root, text="Username")
label_user.pack()
user_entry=Entry(root, textvariable="username")
user_entry.pack()
pass_label=Label(root, text="Password")
pass_label.pack()
pass_entry=Entry(root, textvariable="password", show="*")
pass_entry.pack()
def check():
    all_logs={"sky":"03","green":"tea", "orange":"black", "red": "devil","dora":"boots"}
    myuser=user_entry.get()
    password=pass_entry.get()
    if (myuser, password)in all_logs.items():
        messagebox.showinfo("login", "Correct Login")
        root.withdraw()
        import def_money
        def_money()



    else:
        messagebox.showinfo("login", "Incorrect Login")
        user_entry.delete(0, END)
        pass_entry.delete(0, END)





mybutton= Button(root, text="Login ", bg="orange", command=check).pack()

root.mainloop()
