from tkinter import *
from tkinter import ttk

## Main Screen Setup
root = Tk()
root.configure(background='red')
root.title("Calculator")
mainframe = ttk.Frame(root, padding='50').grid()

equation = StringVar()
expression = ''
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def evaluate():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = []

def clear():
    global expression
    expression = ''
    equation.set('')

## BUTTONS
button1 = ttk.Button(mainframe, command=lambda: press(1), text='1').grid(column=1, row=1)
button2 = ttk.Button(mainframe, command=lambda: press(2), text='2').grid(column=2, row=1)
button3 = ttk.Button(mainframe, command=lambda: press(3), text='3').grid(column=3, row=1)
button4 = ttk.Button(mainframe, command=lambda: press(4), text='4').grid(column=4, row=1)
button5 = ttk.Button(mainframe, command=lambda: press(5), text='5').grid(column=1, row=2)
button6 = ttk.Button(mainframe, command=lambda: press(6), text='6').grid(column=2, row=2)
button7 = ttk.Button(mainframe, command=lambda: press(7), text='7').grid(column=3, row=2)
button8 = ttk.Button(mainframe, command=lambda: press(8), text='8').grid(column=4, row=2)
button9 = ttk.Button(mainframe, command=lambda: press(9), text='9').grid(column=1, row=3)
button0 = ttk.Button(mainframe, command=lambda: press(0), text='0').grid(column=2, row=3)
button_plus = ttk.Button(mainframe, command=lambda: press('+'), text='+').grid(column=3, row=3)
button_sub = ttk.Button(mainframe, command=lambda: press('-'), text='-').grid(column=4, row=3)
button_mulitply = ttk.Button(mainframe, command=lambda: press('*'), text='*').grid(column=1, row=4)
button_divide = ttk.Button(mainframe, command=lambda: press('/'), text='/').grid(column=2, row=4)
button_equals = ttk.Button(mainframe, command=lambda: evaluate(), text='=').grid(column=4, row=4)
button_clear = ttk.Button(mainframe, command=lambda: clear(), text='Clear').grid(column=4, row=5)

## Shows the written equation in screen
box = Entry(mainframe, textvariable=equation).grid(columnspan=4, ipadx=100)
root.mainloop()
