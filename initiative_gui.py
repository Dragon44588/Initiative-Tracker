import tkinter as tk

def gui():
    window = tk.Tk()
    window.minsize(400, 400)
    title = tk.Label(text="Initiative")
    entry = tk.Entry(
        width = 20
        )
    button = tk.Button(
        width = 25,
        text = "submit"
        )
    title.pack(side = tk.LEFT)
    entry.pack(side = tk.LEFT)
    button.pack(side = tk.LEFT)


gui()
