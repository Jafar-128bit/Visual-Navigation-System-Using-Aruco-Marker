import tkinter as tk

window = tk.Tk()

# Creating main label
display_text = tk.StringVar()
display = tk.Label(window, textvariable=display_text)
display.grid(row=0, columnspan=3)


def add_one():
    s = display_text.get()
    s += '1'
    display_text.set(s)


one = tk.Button(window, text="1", height=10, width=10, command=add_one)
one.grid(row=1, column=0)

window.mainloop()
