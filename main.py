from tkinter import *
import re


def check_triangle():
    x = int(entry1.get())
    y = int(entry2.get())
    z = int(entry3.get())

    if x + y <= z or (x == 0 and y == 0 and z == 0) or (x == 1 and y == 1 and z == 1):
        result_label.config(text="Введите значения существующего треугольника.")
    elif x > 1 and y > 1 and z > 1 and x == y and y == z and x + y > z:
        result_label.config(text="Это равносторонний треугольник.")
    elif x > 1 and y > 1 and z > 1 and x + y > z:
        result_label.config(text="Это разносторонний треугольник.")
    elif (x > 1 and y > 1 and z > 1) and (x == y and x != z or x == z and x != y or y == z and y != x):
        result_label.config(text="Это равнобедренный треугольник.")
    else:
        result_label.config(text="Введите значения существующего треугольника.")


def is_valid(newval):
    return re.match("^\d{0,4}$", newval) is not None


window = Tk()
window.title("triangleSokolov")
window.geometry('470x290')
window['bg'] = '#696969'

check = (window.register(is_valid), "%P")

label = Label(window, text="Введите длины сторон треугольника:", font="Times 18", bg='#696969', fg="White")
label.pack()

lab1 = Label(window, fg="#E6E6FA", bg="#696969")
lab1.pack()

entry1 = Entry(window, font="Times 15", fg="Black", bg="White", validate="key", validatecommand=check)
entry1.pack()
lab1 = Label(window, fg="#D8BFD8", bg="#696969")
lab1.pack()
entry2 = Entry(window, font="Times 15", fg="Black", bg="White", validate="key", validatecommand=check)
entry2.pack()
lab1 = Label(window, fg="#D8BFD8", bg="#696969")
lab1.pack()
entry3 = Entry(window, font="Times 15", fg="Black", bg="White", validate="key", validatecommand=check)
entry3.pack()
lab1 = Label(window, fg="#D8BFD8", bg="#696969")
lab1.pack()

check_button = Button(window, text="Вывести результат", fg="White", bg="Black", width=28, height=2,
                      command=check_triangle)
check_button.pack()
lab1 = Label(window, fg="#D8BFD8", bg="#696969")
lab1.pack()

result_label = Label(window, text="", font="Times 15", fg="White", bg="#696969")
result_label.pack()

window.mainloop()
