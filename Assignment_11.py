import tkinter as tk
import webbrowser

def submit_form():
    name = entry1.get()
    course = entry2.get()
    Reference_site =entry3.get()
    f=open("backend2.txt","+w")
    f.writelines(["Name:",name,"\nCourse:",course,"\Reference site:",Reference_site])

    faq_url='https://community.upwork.com/t5/Frequently-Asked-Questions/tkb-p/Academy-FAQ'
    webbrowser.open(faq_url)


root = tk.Tk()
root.title('Course Enquiry Form')


label1 = tk.Label(root, text='Your Name:',font=("Times New Roman",25),width=50)
label1.grid()
entry1 = tk.Entry(root,font=("Times New Roman",25),bg="orange",width=30)
entry1.grid()

label2 = tk.Label(root, text='Enter course:',font=("Times New Roman",25),width=50)
label2.grid()
entry2 = tk.Entry(root,font=("Times New Roman",25),bg="orange",width=30)
entry2.grid()

label3 = tk.Label(root, text='From where did you hear about us ?:',font=("Times New Roman",25),width=50)
label3.grid()
entry3 = tk.Entry(root,font=("Times New Roman",25),bg="orange",width=30)
entry3.grid()


button= tk.Button(root, text='Submit', command=submit_form,bg="orange",
            activebackground="white")
button.grid()


root.mainloop()




