from tkinter import *
import tkinter
import tkcap


root = Tk()
root.geometry("1200x800")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas = Canvas(root, bg='white', height=screen_height, width=screen_width)


def draw(event):
    value = variable.get()
    value_color = variable_2.get()
    if value:
        canvas.create_line((event.x, event.y), (event.x + 10, event.y + 10), fill=value_color, width=value)


def dalate():
    canvas.delete("all")


def zal():
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
lable_3.place(x=10, y=5)
text.place(x=115, y=5)
btn2.place(x=245, y=2)
btn.place(x=400, y=2)                                                    
btno.place(x=600, y=2)
lable.place(x=800, y=5)
shr.place(x=890, y=2)
lable_2.place(x=990, y=5)
color.place(x=1120, y=2)
canvas.pack()


root.mainloop()
