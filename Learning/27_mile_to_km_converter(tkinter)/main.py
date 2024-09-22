from tkinter import *

window = Tk()
window.title("Mile to km converter")
window.config(padx=20, pady=20)

# text input
entry = Entry(width=5)
entry.grid(column=1, row=0)

# is equal to {x} km
# Label0
label0 = Label(text="miles")
label0.grid(column=2, row=0)
# Label1
text="is\nequal to"
label1 = Label(text=text)
label1.grid(column=0, row=1)
# Label2
label2 = Label(text="0")
label2.grid(column=1, row=1)
# Label3
label3 = Label(text="km")
label3.grid(column=2, row=1)


# calculate function
def calc():
    if entry.get():
        miles = round(int(entry.get()) * 1.609)
        label2.config(text=miles)
    else:
        print("r u mad bro")


# calculate button
button = Button(text="calculate", command=calc)
button.grid(column=1, row=2)

window.mainloop()
