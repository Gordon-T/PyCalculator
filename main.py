import tkinter

window = tkinter.Tk() #beginning of gui loop

window.title('PyCalculator Demo')
window.geometry('400x500')

#frame where text would be inputted
textFrame = tkinter.Frame(window, height = 30, width = 300, borderwidth = 5, bg = 'blue')
textFrame.pack()

#simple buttons
button_1 = tkinter.Button(window, text = "1")
button_1.pack()

button_2 = tkinter.Button(window, text = "2")
button_2.pack()

button_3 = tkinter.Button(window, text = "3")
button_3.pack()

button_4 = tkinter.Button(window, text = "4")
button_4.pack()

button_5 = tkinter.Button(window, text = "5")
button_5.pack()

button_6 = tkinter.Button(window, text = "6")
button_6.pack()

button_7 = tkinter.Button(window, text = "7")
button_7.pack()

button_8 = tkinter.Button(window, text = "8")
button_8.pack()

button_9 = tkinter.Button(window, text = "9")
button_9.pack()

button_0 = tkinter.Button(window, text = "0")
button_0.pack()

window.mainloop() #end of loop