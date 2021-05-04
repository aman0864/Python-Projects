import tkinter as tk
from tkinter import PhotoImage

# setting root window:
root = tk.Tk()
root.title("Cool Tkinter Buttons")
root.config(bg="#100e17")
root.geometry("800x400")

# load round corner button image:
img = PhotoImage(file=r"btn.png")

# Button widgets:
tk.Button(root, text=" Button 1 ", font="Bahnschrift 20", bg="red", fg="white", activebackground="red",
          activeforeground="black", borderwidth=2, relief=tk.RAISED, cursor="hand2").place(x=200, y=100)

tk.Button(root, text="Button 2", font="System 20", bg="green", fg="black", activebackground="black", activeforeground="darkgreen",
          borderwidth=1, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black").place(x=350, y=102)

tk.Button(root, text="Button 3", bg="#00bfff", fg="white", activebackground="#87ceeb", activeforeground="black",
          borderwidth=2, relief=tk.RIDGE, font="Bahnschrift 20", cursor="hand2").place(x=510, y=100)

tk.Button(root, text="Button 4", bg="grey", fg="red", activebackground="red", activeforeground="black", borderwidth=3,
          font="Bahnschrift 20", cursor="hand2", highlightbackground="red", relief=tk.SUNKEN).place(x=200, y=180)

tk.Button(root, image=img, bg="#100e17", activebackground="#100e17", relief=tk.FLAT,
          borderwidth=0, padx=40, pady=40, cursor="hand2", width=120).place(x=350, y=195)

tk.Button(root, text="Button 6", bg="orange", fg="black", activebackground="orange", activeforeground="black",
          borderwidth=2, relief=tk.SOLID, font="Bahnschrift 20", cursor="hand2", highlightbackground="red").place(x=510, y=182)

# window in mainloop:
root.mainloop()
