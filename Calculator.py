import tkinter
from tkinter import *
window = Tk()
window.title("CALCULATOR")
label_result = tkinter.Label(window,text="",width=25,height=5,bg="white")
label_result.grid(row=0,column=0,columnspan=5)
expression = ""

#funcations
def click_button_1(value):
    global expression
    expression += value
    label_result.config(text=expression)
def clear():
    global expression
    expression = ""
    label_result.config(text=expression) #display module
def calculate():
    global expression
    result=""
    if expression !="":  # when nothing error ia avoided
      try:
        result = eval(expression)

      except :
        result="Error"
        expression = ""
    label_result.config(text=result)

button_1 = Button(window,text="1",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("1"))
button_1.grid(row=1,column=0)
button_2 = Button(window,text="2",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("2"))
button_2.grid(row=1,column=1)
button_3 = Button(window,text="3",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("3"))
button_3.grid(row=1,column=2)
button_div = Button(text="/",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("/"))
button_div.grid(row=1,column=3)
button_4 = Button(window,text="4",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("4"))
button_4.grid(row=2,column=0)
button_5 = Button(window,text="5",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("5"))
button_5.grid(row=2,column=1)
button_6 = Button(window,text="6",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("6"))
button_6.grid(row=2,column=2)
button_7 = Button(window,text="7",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("7"))
button_7.grid(row=3,column=0)
button_8 = Button(window,text="8",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("8"))
button_8.grid(row=3,column=1)
button_mul = Button(window,text="*",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("*"))
button_mul.grid(row=2,column=3)
button_9 = Button(window,text="9",width=5,height=2,bg="white",fg="blue",command=lambda:click_button_1("9"))
button_9.grid(row=3,column=2)
button_sub = Button(text="-",width=5,height=2,bg="white",fg="blue",command= lambda: click_button_1("-"))
button_sub.grid(row=3,column=3)
button_c = Button(window,text="C",width=5,height=2,bg="white",fg="blue",command=lambda: clear())
button_c.grid(row=4,column=0)
button_0 = Button(window,text="0",width=5,height=2,bg="white",fg="blue",command=lambda :click_button_1("0"))
button_0.grid(row=4,column=1)
button_dot = Button(window,text=".",width=5,height=2,bg="white",fg="blue",command=lambda : click_button_1("."))
button_dot.grid(row=4,column=2)
button_add = Button(window,text="+",width=5,height=2,bg="white",fg="blue",command=lambda : click_button_1("+"))
button_add.grid(row=4,column=3)
button_eq = Button(window,text="=",width=24,height=2,bg="white",fg="blue",command=lambda : calculate())
button_eq.grid(row=5,column=0,columnspan=8)


window.mainloop()
