# Paint_Python
Версия Paint написанная на языке программирования Python
Этот проект был написанн PVkolos. 
Проект кроссплатформенный, он работает как на Windows, так и на Linux и MacOS.
В данном коде я предоставляю вам мою версию Paint, написанную на языке программирования Python.
Чтобы вам воспользоваться этим проектом, вам необходимо установить некоторые зависимости:

pip install tkcap

Так же у вас должен быть установленный на компьтере Python и рабочий pip.

Логика работы кода:
Мы отслеживаем мышь, нажата она или нет, и если она нажата, то рисуем круги, от текущего положения мыши - 20 пикселей (чтобы мышь была приблизительно в центре круга) до положения мыши + размер круга выбранный пользователем.
Есть функция заливки всего фона, реализованная при помощи изменения цвета фона объекта класса Canvas. 
Есть функция отчистки всего фона, реализованная при помощи метода отчистки объекта класса Canvas: object.delete("all"). 
Есть функция изменения резмера кисти.
Есть функция изменения цвета кисти.
Есть функция сохранения вашего рисунка в формате jpg, реализованная при помощи скриншота вашей программы на tkinter.

Если есть предложения по дороботке этого проетка, пишите на почту: pythonitpa@gmail.com

Если хотите поддержать меня: https://www.donationalerts.com/r/pvkolos
