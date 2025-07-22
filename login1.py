import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")
        password_entry.delete(0, tk.END)

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text='Show')
    else:
        password_entry.config(show='')
        toggle_btn.config(text='Hide')

# Root window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="#ecf0f1")
root.resizable(False, False)

# Frame for content
frame = tk.Frame(root, bg="white", padx=20, pady=20, bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title = tk.Label(frame, text="Login", font=("Helvetica", 18, "bold"), bg="white", fg="#2c3e50")
title.pack(pady=(0, 10))

# Username
tk.Label(frame, text="Username", font=("Arial", 12), bg="white", anchor="w").pack(fill="x")
username_entry = tk.Entry(frame, font=("Arial", 12), relief="groove", bd=2)
username_entry.pack(fill="x", pady=(0, 10))

# Password
tk.Label(frame, text="Password", font=("Arial", 12), bg="white", anchor="w").pack(fill="x")
pw_frame = tk.Frame(frame, bg="white")
pw_frame.pack(fill="x", pady=(0, 10))

password_entry = tk.Entry(pw_frame, font=("Arial", 12), relief="groove", bd=2, show="*")
password_entry.pack(side="left", fill="x", expand=True)

toggle_btn = tk.Button(pw_frame, text="Show", command=toggle_password, bg="#bdc3c7", relief="flat", padx=5)
toggle_btn.pack(side="right", padx=5)

# Login button
login_btn = tk.Button(frame, text="Login", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", padx=10, pady=5, command=login)
login_btn.pack(pady=10, fill="x")

# Run the app
root.mainloop()
