#Shravan Surve

import tkinter as tk
import webbrowser

def navigate():
    s=entry1.get()
    print("Navigating to: ",(f"https://www.amazon.in/s?k={s}"))
    webbrowser.open(f"https://www.amazon.in/s?k={s}")
    
    
root=tk.Tk()
root.title("Website")

lable1=tk.Label(root,text="Enter the product you wanna search :",font=("Times New Roman",25),width=50)   
lable1.grid()

entry1=tk.Entry(root,font=("Times New Roman",25),bg="yellow",width=30)
entry1.grid()

button=tk.Button(root,text="Navigate", bg="yellow",
            activebackground="black",command=navigate)
button.grid()

root.mainloop()
