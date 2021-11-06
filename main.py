import tkinter

window = tkinter.Tk() #beginning of gui loop

window.title('PyCalculator Demo')
window.geometry('295x455')

#frame where text would be inputted
textFrame = tkinter.Frame(window, height = 50, width = 250, borderwidth = 5, bg = 'gray').place(x = 23, y = 10)

buttonFrames = tkinter.Frame(window, )

#Number Keypad
button_1 = tkinter.Button(window, text = "1", height = 4, width = 8).place(x = 10, y = 300)

button_2 = tkinter.Button(window, text = "2", height = 4, width = 8).place(x = 80, y = 300)

button_3 = tkinter.Button(window, text = "3", height = 4, width = 8).place(x = 150, y = 300)

button_4 = tkinter.Button(window, text = "4", height = 4, width = 8).place(x = 10, y = 225)

button_5 = tkinter.Button(window, text = "5", height = 4, width = 8).place(x = 80, y = 225)

button_6 = tkinter.Button(window, text = "6", height = 4, width = 8).place(x = 150, y = 225)

button_7 = tkinter.Button(window, text = "7", height = 4, width = 8).place(x = 10, y = 150)

button_8 = tkinter.Button(window, text = "8", height = 4, width = 8).place(x = 80, y = 150)

button_9 = tkinter.Button(window, text = "9", height = 4, width = 8).place(x = 150, y = 150)

button_0 = tkinter.Button(window, text = "0", height = 4, width = 8).place(x = 80, y = 375)

button_period = tkinter.Button(window, text = ".", height = 4, width = 8).place(x = 150, y = 375)

#Operation buttons

buttonAdd = tkinter.Button(window, text = "+", height = 4, width = 8).place(x = 220, y = 300)

buttonSubtract = tkinter.Button(window, text = "-", height = 4, width = 8).place(x = 220, y = 225)

buttonMultiply = tkinter.Button(window, text = "*", height = 4, width = 8).place(x = 220, y = 150)

buttonDivide = tkinter.Button(window, text = "/", height = 4, width = 8).place(x = 220, y = 75)

buttonEqual = tkinter.Button(window, text = "=", height = 4, width = 8).place(x = 220, y = 375)

buttonClear = tkinter.Button(window, text = "Clear", height = 4, width = 8).place(x = 10, y = 375)

buttonDivide = tkinter.Button(window, text = "/", height = 4, width = 8).place(x = 220, y = 75)

buttonSqrt = tkinter.Button(window, text = "√", height = 4, width = 8).place(x = 150, y = 75)

buttonExp = tkinter.Button(window, text = "^", height = 4, width = 8).place(x = 80, y = 75)

buttonGraph = tkinter.Button(window, text = "Graph", height = 4, width = 8).place(x = 10, y = 75)


window.mainloop() #end of loop