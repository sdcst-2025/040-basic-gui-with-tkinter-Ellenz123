import tkinter as tk 

window = tk.Tk()
window.title("tk")
window.geometry("400x100")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=15)
Label1 = tk.Label(window,text="x", width=2)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=15)
Label2 = tk.Label(window,text="=", width=2)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=15)

Label1.grid(row=1, column=2)
Label2.grid(row=1, column=4)
entry1.grid(row=1,column=1, padx=5)
entry2.grid(row=1,column=3)
entry3.grid(row=1,column=5, padx=5)

window.mainloop()