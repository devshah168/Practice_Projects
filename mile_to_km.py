from tkinter import *

window=Tk()
window.title("Mile to Km Converter")


def miles_to_km():
    miles=miles_input.get()
    kms=int(miles)*1.6
    kilometers_result.config(text=kms)
miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)
miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)
is_equal=Label(text="is equal to")
is_equal.grid(column=0,row=1)
kilometers_result=Label(text="0")
kilometers_result.grid(column=1,row=1)
km_label=Label(text="Km")
km_label.grid(column=2,row=1)
calculate_but=Button(text="Calculate",command=miles_to_km)
calculate_but.grid(column=1,row=2)
window.mainloop()