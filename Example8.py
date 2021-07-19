# Пример похож на предыдущий, но здесь используются классы, поэтому
# каждое окно имеет собственную информацию состояния.

from tkinter import *
import random

import self as self


class MyGui:
    """
    Графический пользовательский интерфейс с кнопками,
    которые изменяют цвет и увеличивают размеры меток
    """
    colors = ['green', 'blue', 'orange', 'red', 'brown', 'yellow']

    def __init__(self, parent, title='popup'):
        parent.title(title)
        self.growing = False
        self.fontsize = 10
        self.lab = Label(parent, text='Gui1', fg='white', bg='navy')
        self.lab.pack(expand=YES, fill=BOTH)
        Button(parent, text='Spam', command=self.reply).pack(side=LEFT)
        Button(parent, text='Grow', command=self.grow).pack(side=LEFT)
        Button(parent, text='Stop', command=self.stop).pack(side=LEFT)

    def reply(self):
        """change the button's color at random on Spam presses"""
        self.fontsize += 5
        color = random.choice(self.colors)
        self.lab.config(bg=color,
                        font=('courier', self.fontsize, 'bold italic'))

    def grow(self):
        """start making the label grow on Grow presses"""
        self.growing = True
        self.grower()

    def grower(self):
        if self.growing:
            self.fontsize += 5
            self.lab.config(font=('courier', self.fontsize, 'bold'))
            self.lab.after(500, self.grower)

    def stop(self):
        """stop the button growing on Stop presses"""
        self.growing = False

class MySubGui(MyGui):
    colors = ['black', 'purple']   # Настройка для изменения вариантов цвета

MyGui(Tk(), 'main')
MyGui(Toplevel())
MySubGui(Toplevel())
mainloop()

