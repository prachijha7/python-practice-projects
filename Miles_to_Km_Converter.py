from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=50)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)

#Entries
input_entry = Entry(width=10)
#Add some text to begin with
input_entry.insert(END, string="0")
#Gets text in entry
input_entry.grid(column=1, row=0)

#Buttons
def convert():
    miles = float(input_entry.get())
    km = round(miles * 1.609)
    answer_label.config(text=km)

#calls action() when pressed
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()

