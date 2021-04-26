from tkinter import *
import tkinter
from tkinter import messagebox as mbox
import tkcap
import os
from tkinter import colorchooser
from tkinter.ttk import *

root = Tk()
root.geometry("1200x800")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
cn = Canvas(root, bg='white', height=30, width=30)
canvas = Canvas(root, bg='white', height=screen_height, width=screen_width)
root.title('Paint')
hx = None
value_color = None


def draw(event):
    global value_color
    value = variable.get()
    value_color = hx

    if value and value_color:
        canvas.create_oval((event.x - int(value) // 2, event.y - int(value) // 2), (event.x + int(value) // 2, event.y + int(value) // 2), fill=value_color, outline=value_color)
    elif not value and value_color:
        mbox.showerror("Ошибка", "Выберите размер кисти для рисования!")


def dalate():
    canvas.config(bg='white')
    canvas.delete("all")


def zal():
    if value_color:
        canvas.config(bg=value_color)
    else:
        mbox.showerror("Ошибка", "Выберите цвет заливки!")


def save():
    if not os.path.exists(f'{text.get()}.jpg'):
        cap = tkcap.CAP(root)
        cap.capture(f'{text.get()}.jpg')
    else:
        mbox.showerror("Ошибка", "Файл с таким именем существует!")


def color_sam():
    global hx, value_color
    (rgb, hx) = colorchooser.askcolor()
    cn.config(bg=hx)


variable = StringVar(root)
shr = OptionMenu(root, variable, 1, 1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100)

bytton = tkinter.ttk.Button(root, text='Выбрать цвет', command=color_sam)
btn = tkinter.ttk.Button(root, text='Очистить всё', command=dalate)
btno = tkinter.ttk.Button(root, text='Заливка', command=zal)
lable = tkinter.ttk.Label(root, text='Размер кисти:')
lable_2 = tkinter.ttk.Label(root, text='Цвет кисти (заливки):')
lable_3 = tkinter.ttk.Label(root, text='Название файла:')
btn2 = tkinter.ttk.Button(root, text='Save', command=save)
text = tkinter.ttk.Entry()
root.bind("<B1-Motion>", draw)
root.bind('<Button-1>', draw)

bytton.grid(column=59, row=1)
lable_3.grid(column=1, row=0, pady=7)
text.grid(column=3, row=0)
btn2.grid(column=9, row=0)
btn.grid(column=19, row=0, padx=100)
btno.grid(column=29, row=0, padx=50)
lable.grid(column=39, row=0, padx=50)
shr.grid(column=39, row=1, padx=50)
lable_2.grid(column=59, row=0, padx=25)
canvas.place(x=0, y=65)
cn.grid(column=69, row=1)

root.mainloop()
