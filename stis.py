import os
import tkinter as tk 
from tkinter import ttk
#from ttk import label
import psutil
#function to get memory usage
def getMem():
    memory_usage = psutil.virtual_memory().used
    memory_usage_mb = "{:.1f}".format(memory_usage / (1024*1024*1024))
    return memory_usage_mb
    

def mainWindow():
    memUse = getMem()
    #window = tk.Tk()
    #text_box = tk.Text(window, height = 10, width = 100)
    #text_box.pack()
    #window.geometry('200x100')
    #window.resizable(False, False)
    window.title("The sharpest tool in the shed")
    text_box.delete(1.0, tk.END)

    text_box.insert(tk.END, f"{memUse} Gb")

    #memory_display_btn = tk.Button(window, text="Memory Usage", command=getMem)
    #memory_display_btn.pack()
    #window.mainloop()

#text_box = tk.Text(window, heigth=10, width=100, spacing=1)

window = tk.Tk()
window.geometry('200x100')
text_box = tk.Text(window, height = 2, width = 25)
text_box.pack()

label = ttk.Label(window, text="Memory being used")
label.pack(ipadx=10, ipady=10)
memory_display_btn = tk.Button(window, text="Memory Usage", command=mainWindow)
memory_display_btn.pack()
window.mainloop()
#mainWindow()


