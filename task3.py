import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title("Example")
window.geometry("350x150")
window.resizable(False,False)
window.configure(bg="white")

photo = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=photo,bg="white")
label1.grid(row=0, column=0, columnspan=2, pady=(10,5))

label2 = tk.Label(window, text="Pochacco!",bg="white")
label2.grid(row=1, column=0, columnspan=2)

bottomframe=tk.Frame(window,bg="lightblue")
bottomframe.grid(row=2, column=0, columnspan=2, sticky="we", padx=0, pady=(5,10))

label3=tk.Label(
    bottomframe, 
    text="A cuddly little puppy! This is from the same \n creators who brought you keropi and Kero Kero",
    font=("Arial",10, "bold"),
    bg="lightblue", 
    justify="center"
    )
label3.grid(row=0, colomn=0, padx=10, pady=5)


window.mainloop()