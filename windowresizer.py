from tkinter import *
root = Tk()
root.title("My Window Resizer")
root.geometry("200x200")


frame = Frame(root,background="black")
frame.pack(fill="both",expand=True)


label_head =Label(frame,text="Welcome to Window Resizer",font=("Times New Roman",10,"bold"),bg="black",fg="white")
label_head.grid(row=0,column=2)


width = StringVar()
height = StringVar()


label_width = Label(frame,text="Width:",bg="black",fg="white",pady=10,padx=5)
label_width.grid(row=1,column=1)
label_height = Label(frame,text="Height",bg="black",fg="white",pady=10,padx=5)
label_height.grid(row=2,column=1)


width_entry =Entry(frame,textvariable=width)
width_entry.grid(row=1,column=2)


height_entry =Entry(frame,textvariable=height)
height_entry.grid(row=2,column=2)
def updateWindow():
    print("Updating your window")
    root.geometry(f"{width.get()}x{height.get()}")

button = Button(frame,text="Apply",command=updateWindow)
button.grid(row=3,column=2)

root.mainloop()
