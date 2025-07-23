import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(padx=10, pady=10, fill="x")


# Button click event
def click_button(value):
    entry.insert(tk.END, value)


def clear_entry():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create button frame
btn_frame = tk.Frame(root)
btn_frame.pack()

# Place buttons in grid
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == 'C':
            action = clear_entry
        elif btn_text == '=':
            action = calculate
        else:
            action = lambda x=btn_text: click_button(x)

        btn = tk.Button(btn_frame, text=btn_text, width=5, height=2, font=("Arial", 14), command=action)
        btn.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
