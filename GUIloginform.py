import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username =="admin" and password =="1234":
        messagebox.showinfo("login status","login successful")
    else:
        messagebox.showinfo("login status","logion invaild")
#create window
window = tk.Tk()
window.title("Login form")
window.geometry("300x200")
#labels
tk.Label(window,text="username").pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

tk.Label(window,text="password").pack(pady=5)
entry_password = tk.Entry(window)
entry_password.pack(pady=5)

#Login button
btn_login=tk.Button(window,text="Login",command=login)
btn_login.pack(pady=20)

window.mainloop()