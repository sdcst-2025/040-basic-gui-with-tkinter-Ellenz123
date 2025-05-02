import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title("Example")
window.geometry("350x170")
window.configure(bg="white")

photo = PhotoImage(file="dog.png")
l1 = tk.Label(window, image=photo,bg="white")
l1.place(x=130, y=10)
l2 = tk.Label(window, text="Pochacco!",bg="white")
l2.place(x=200, y=60)
bottomframe=tk.Frame(window,bg="lightblue", width=350, height=70)
bottomframe.place(x=0, y=120)

l3=tk.Label(
    bottomframe, 
    text="A cuddly little puppy! This is from the same \n creators who brought you keropi and Kero Kero",
    font=("Arial",10, "bold"),
    bg="lightblue", 
    justify="center"
    )
l3.place(x=15, y=8)
window.mainloop()