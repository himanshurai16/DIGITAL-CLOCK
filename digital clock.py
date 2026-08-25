import tkinter as tk
from time import strftime

window = tk.Tk()
window.title("Digital Clock")
window.geometry("500x200")

clock = tk.Label(
    window,
    font=("Arial", 50, "bold"),
    bg="black",
    fg="white"
)

clock.pack(expand=True)


def show_time():
    current = strftime("%H:%M:%S")
    clock.config(text=current)
    clock.after(1000, show_time)


show_time()

window.mainloop()