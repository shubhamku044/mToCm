from tkinter import *
def converter():
    m = float(meters.get())
    cm = m*100
    result.config(text=cm)

window = Tk()
window.title("meter to centimeter converter")
window.config(padx=20, pady=20, bg="#ffddd2")

meters = Entry(width=6,font = ("Roboto", 16, "bold"))
meters.grid(row=0, column=1)

meter_label = Label(text = "meter",font = ("Roboto", 16),bg="#ffddd2", fg="#d62828")
meter_label.grid(row=0, column=2)

myLabel = Label(text = "m to cm",font=("Ubuntu",20,"bold"),bg="#ffddd2",fg="#1d3557")
myLabel.grid(row=0, column=0)

result = Label(text = " ",font = ("Roboto", 16, "bold"),bg="white", width=6)
result.grid(row=1, column=1)

cm_label = Label(text = "centimeter",font=("Roboto",18),bg="#ffddd2", fg="#d62828")
cm_label.grid(row=1, column=2)

calc = Button(text="Calculate", command= converter, bg="#edf6f9")
calc.grid(row=2, column=1)

window.mainloop()
