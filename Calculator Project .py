import tkinter as tk
from tkinter import scrolledtext as st
main = tk.Tk()
main.geometry("600x350")
main.title("Python Calculator")
# This creates the main window

historylabel = tk.Label(master=main, text="HISTORY", font=("Times New Roman", 15, "bold"))

scrollhistory = st.ScrolledText(master=main, width=20, height=15, font=("Ariel", 8))
scrollhistory.configure(state="disabled")
# These are used to create the history scrollbox

addentry1 = tk.Entry(master=main)
addentry2 = tk.Entry(master=main)
# These are the inputs for addition


def add_calculate():
    add1 = float(addentry1.get())
    add2 = float(addentry2.get())
    addsum = add1+add2
    scrollhistory.configure(state="normal")
    scrollhistory.insert(tk.INSERT, f"\n {add1} + {add2} = {addsum}\n")
    scrollhistory.configure(state="disabled")
    addresult.config(text=addsum)
# This is used for calculating the sum of the inputs and updating the history


addresult = tk.Label(master=main, text="0")
# This is a placeholder for the answer to addition

subtractentry1 = tk.Entry(master=main)
subtractentry2 = tk.Entry(master=main)
# These are the inputs for subtraction


def subtract_calculate():
    sub1 = float(subtractentry1.get())
    sub2 = float(subtractentry2.get())
    subresult = sub1-sub2
    scrollhistory.configure(state="normal")
    scrollhistory.insert(tk.INSERT, f"\n {sub1} - {sub2} = {subresult}\n")
    scrollhistory.configure(state="disabled")
    subresulttext.config(text=subresult)
# This is used for calculating the result of subtraction and updating the history


subresulttext = tk.Label(master=main, text="0")
# This is a placeholder for the answer to subtraction

multiplyentry1 = tk.Entry(master=main)
multiplyentry2 = tk.Entry(master=main)
# These are the inputs for multiplication


def multiply_calculation():
    mul1 = float(multiplyentry1.get())
    mul2 = float(multiplyentry2.get())
    mulproduct = mul1*mul2
    scrollhistory.configure(state="normal")
    scrollhistory.insert(tk.INSERT, f"\n {mul1} x {mul2} = {mulproduct}\n")
    scrollhistory.configure(state="disabled")
    mulresult.config(text=mulproduct)
# This is used for calculating the result of multiplication and updating the history


mulresult = tk.Label(master=main, text="0")
# This is a placeholder for the answer to multiplication

diventry1 = tk.Entry(master=main)
diventry2 = tk.Entry(master=main)
# These are the inputs for division


def div_calculation():
    div1 = float(diventry1.get())
    div2 = float(diventry2.get())
    divedend = div1/div2
    scrollhistory.configure(state="normal")
    scrollhistory.insert(tk.INSERT, f"\n {div1} / {div2} = {divedend}\n")
    scrollhistory.configure(state="disabled")
    divresult.config(text=divedend)
# This is used for calculating the result of division and updating history


divresult = tk.Label(master=main, text="0")
# This is a placeholder for the answer to division

add_Button = tk.Button(master=main, text="=", command=add_calculate)
subtract_button = tk.Button(master=main, text="=", command=subtract_calculate)
multiply_button = tk.Button(master=main, text="=", command=multiply_calculation)
divide_button = tk.Button(master=main, text="=", command=div_calculation)
# These are the lines for creating the buttons to do the calculations.

add_sign = tk.Label(master=main, text="+")
sub_sign = tk.Label(master=main, text="-")
mul_sign = tk.Label(master=main, text="x")
div_sign = tk.Label(master=main, text="/")
# These are the lines that create the signs for going between the inputs.

addentry1.place(relx=0.12, rely=0.2, anchor="center")
addentry2.place(relx=0.34, rely=0.2, anchor="center")
add_sign.place(relx=0.22, rely=0.2, anchor="center")
addresult.place(relx=0.6, rely=0.2, anchor="center")
add_Button.place(relx=0.48, rely=0.2, anchor="center")
# These place all of the components for addition.

subtractentry1.place(relx=0.12, rely=0.4, anchor="center")
subtractentry2.place(relx=0.34, rely=0.4, anchor="center")
sub_sign.place(relx=0.22, rely=0.4, anchor="center")
subresulttext.place(relx=0.6, rely=0.4, anchor="center")
subtract_button.place(relx=0.48, rely=0.4, anchor="center")
# These place all of the components for subtraction.

multiplyentry1.place(relx=0.12, rely=0.6, anchor="center")
multiplyentry2.place(relx=0.34, rely=0.6, anchor="center")
mul_sign.place(relx=0.22, rely=0.6, anchor="center")
mulresult.place(relx=0.6, rely=0.6, anchor="center")
multiply_button.place(relx=0.48, rely=0.6, anchor="center")
# These place all of the components for multiplication.

diventry1.place(relx=0.12, rely=0.8, anchor="center")
diventry2.place(relx=0.34, rely=0.8, anchor="center")
div_sign.place(relx=0.22, rely=0.8, anchor="center")
divresult.place(relx=0.6, rely=0.8, anchor="center")
divide_button.place(relx=0.48, rely=0.8, anchor="center")
# These place all of the components for division.

scrollhistory.place(relx=0.8, rely=0.4, anchor="center")
# This places the history scrollbox that is used for the calculator
historylabel.place(relx=0.78, rely=0.05, anchor="center")

main.mainloop()
# This is the command that is used to make the whole window stay open, it is necessary to function
