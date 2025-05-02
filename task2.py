import tkinter as tk 
from tkinter import PhotoImage

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("630x200")
photo1 = PhotoImage(file="dog.png")
l1 = tk.Label(window, image=photo1)
l1.place(x=0,y=0)

l2 = tk.Label(window, text="Client Database")
l2.place(x=240,y=50)

l3 = tk.Label(window, text="Search by Name")
l3.place(x=400,y=10)
e1=tk.Entry(window)
e1.place(x=500,y=10)

l4 = tk.Label(window, text="Name")
l4.place(x=30,y=100)
e2=tk.Entry(window,width=15)
e2.place(x=0,y=120)

l5 = tk.Label(window, text="Type")
l5.place(x=140,y=100)
e3=tk.Entry(window,width=15)
e3.place(x=120,y=120)

l5 = tk.Label(window, text="Breed")
l5.place(x=260,y=100)
e3=tk.Entry(window,width=15)
e3.place(x=240,y=120)

l5 = tk.Label(window, text="Owner")
l5.place(x=380,y=100)
e3=tk.Entry(window,width=15)
e3.place(x=360,y=120)

l5 = tk.Label(window, text="Birthdate")
l5.place(x=500,y=100)
e3=tk.Entry(window,width=15)
e3.place(x=480,y=120)


b1=tk.Button(window, text="< Previous")
b2=tk.Button(window, text="Save Entry")
b3=tk.Button(window, text="Next >")
b1.place(x=0, y=160)
b2.place(x=250, y=160)
b3.place(x=580, y=160)
window.mainloop()