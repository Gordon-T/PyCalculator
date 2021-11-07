import tkinter
import operator


window = tkinter.Tk() #beginning of gui loop

window.title('PyCalculator')
window.geometry('295x455')

#frame where text would be inputted
textFrame = tkinter.Frame(window, height = 50, width = 250, borderwidth = 5).place(x = 23, y = 10)

buttonFrames = tkinter.Frame(window)

#Input Button


button = tkinter.Entry(window)
button.pack(pady=30)
input = button.get()

count = 0

def input_button1():
    global count
    button.insert(count, 1)
    count = count + 1

def input_button2():
    global count
    button.insert(count, 2)
    count = count + 1

def input_button3():
    global count
    button.insert(count, 3)
    count = count + 1

def input_button4():
    global count
    button.insert(count, 4)
    count = count + 1

def input_button5():
    global count
    button.insert(count, 5)
    count = count + 1

def input_button6():
    global count
    button.insert(count, 6)
    count = count + 1

def input_button7():
    global count
    button.insert(count, 7)
    count = count + 1

def input_button8():
    global count
    button.insert(count, 8)
    count = count + 1

def input_button9():
    global count
    button.insert(count, 9)
    count = count + 1

def input_button0():
    global count
    button.insert(count, 0)
    count = count + 1

def input_button_add():
    global count
    button.insert(count, '+')
    count = count + 1

def input_button_subtract():
    global count
    button.insert(count, '-')
    count = count + 1

def input_button_multiply():
    global count
    button.insert(count, '*')
    count = count + 1

def input_button_divide():
    global count
    button.insert(count, '/')
    count = count + 1

def input_buttonClear():
    button.delete("0", "end")

def calculate():
    operator_dict = {"+": operator.add, "-": operator.sub, '*': operator.mul, '/': operator.truediv}
    button.get()
    list = []
    for loopvar in button.get():
       if loopvar != '+' or '-' or '*' or '/':
           list.append(loopvar)
       else:
           




#Number Keypad
button_1 = tkinter.Button(window, text = "1", height = 4, width = 8, command = input_button1).place(x = 10, y = 300)

button_2 = tkinter.Button(window, text = "2", height = 4, width = 8, command = input_button2).place(x = 80, y = 300)

button_3 = tkinter.Button(window, text = "3", height = 4, width = 8, command = input_button3).place(x = 150, y = 300)

button_4 = tkinter.Button(window, text = "4", height = 4, width = 8, command = input_button4).place(x = 10, y = 225)

button_5 = tkinter.Button(window, text = "5", height = 4, width = 8, command = input_button5).place(x = 80, y = 225)

button_6 = tkinter.Button(window, text = "6", height = 4, width = 8, command = input_button6).place(x = 150, y = 225)

button_7 = tkinter.Button(window, text = "7", height = 4, width = 8, command = input_button7).place(x = 10, y = 150)

button_8 = tkinter.Button(window, text = "8", height = 4, width = 8, command = input_button8).place(x = 80, y = 150)

button_9 = tkinter.Button(window, text = "9", height = 4, width = 8, command = input_button9).place(x = 150, y = 150)

button_0 = tkinter.Button(window, text = "0", height = 4, width = 8, command = input_button0).place(x = 80, y = 375)

button_period = tkinter.Button(window, text = ".", height = 4, width = 8).place(x = 150, y = 375)

#Operation buttons

buttonAdd = tkinter.Button(window, text = "+", height = 4, width = 8, command = input_button_add).place(x = 220, y = 300)

buttonSubtract = tkinter.Button(window, text = "-", height = 4, width = 8, command = input_button_subtract).place(x = 220, y = 225)

buttonMultiply = tkinter.Button(window, text = "*", height = 4, width = 8, command = input_button_multiply).place(x = 220, y = 150)

buttonDivide = tkinter.Button(window, text = "/", height = 4, width = 8, command = input_button_divide).place(x = 220, y = 75)

buttonEqual = tkinter.Button(window, text = "=", height = 4, width = 8, command = calculate).place(x = 220, y = 375)

buttonClear = tkinter.Button(window, text = "Clear", height = 4, width = 8, command = input_buttonClear).place(x = 10, y = 375)

buttonSqrt = tkinter.Button(window, text = "√", height = 4, width = 8).place(x = 150, y = 75)

buttonExp = tkinter.Button(window, text = "^", height = 4, width = 8).place(x = 80, y = 75)

buttonGraph = tkinter.Button(window, text = "Graph", height = 4, width = 8).place(x = 10, y = 75)


window.mainloop() #end of loop
