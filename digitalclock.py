import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    # Call this function again after 1000ms (1 second)
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.configure(bg="black")

# Create and place the label
label = tk.Label(root, font=("Arial", 40), bg="black", fg="cyan")
label.pack(anchor="center")

# Start the clock
update_time()

# Run the app
root.mainloop()
