
from tkinter import *
import tkinter
import tkcap

root = Tk()
root.geometry("1200x800")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas = Canvas(root, bg='white', height=screen_height, width=screen_width)
root.title('Paint')


def draw(event):
    value = variable.get()
    value_color = variable_2.get()
    if value:
        canvas.create_oval((event.x - 20, event.y - 20), (event.x + int(value), event.y + int(value)), fill=value_color, outline=value_color)


def dalate():
    canvas.config(bg='white')
    canvas.delete("all")


def zal():
    if variable_2.get():
        canvas.config(bg=variable_2.get())


def save():
    cap = tkcap.CAP(root)
    cap.capture(f'{text.get()}.jpg')


variable = StringVar(root)
shr = OptionMenu(root, variable, 1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100)
variable_2 = StringVar(root)
color = OptionMenu(root, variable_2, 'red', 'green', 'blue', 'pink', 'black', 'white', 'grey', 'brown', 'orange', 'violet')

btn = tkinter.Button(root, text='Очистить всё', command=dalate)
btno = tkinter.Button(root, text='Заливка', command=zal)
lable = tkinter.Label(root, text='Размер кисти:')
lable_2 = tkinter.Label(root, text='Цвет кисти (заливки):')
lable_3 = tkinter.Label(root, text='Название файла:')
btn2 = tkinter.Button(root, text='Save', command=save)
text = tkinter.Entry()
root.bind("<B1-Motion>", draw)

lable_3.grid(column=1, row=0)
text.grid(column=3, row=0)
btn2.grid(column=9, row=0)
btn.grid(column=19, row=0, padx=100)
btno.grid(column=29, row=0, padx=50)
lable.grid(column=39, row=0, padx=50)
shr.grid(column=39, row=1, padx=50)
lable_2.grid(column=59, row=0, padx=50)
color.grid(column=59, row=1, padx=50)
canvas.place(x=0, y=50)

root.mainloop()
