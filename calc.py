# coding=utf8
from tkinter import *
from functools import partial
from math import sqrt


RED = "white"


class Calculadora(object):
    def __init__(self, instancia):
        self.font = ('Verdana', '50', 'bold')
        self.font2 = ('Verdana', '10', 'bold')
        self.t = 0
        self.y = 0

        # Frame que contem a entrada de texto
        self.frame2 = Canvas(instancia, height=3, width=18)
        self.frame2['bg'] = RED

        # Frame que contem os botões especificos
        self.frame5 = Frame(instancia)
        self.frame5['bg'] = RED

        # Empacotamos as nossas frames
        self.frame2.pack()
        self.frame5.pack()

        # Colocar a entrada de texto
        self.form = Text(self.frame2, height=3, width=18, font=self.font)
        self.form.pack()

        botões = (
        '7', '8', '9', 'delete', '4', '5',
        '6', '/', '1', '2', '3', '*', '0', '.',
        '-', '(', '(', ')', 'sqrt()', '+')

        for i in range(len(botões)):
            if i % 4 == 0:
                subframe = Frame(self.frame5)
                subframe.pack()
            a = Button(subframe, text=botões[i], bg='white', width=22, height=4,
                    command=partial(self.ColocaTexto, botões[i]), font=self.font2, borderwidth=0.5)
            a.pack(side=LEFT)
            self.y += 1
            if self.y == 14:
                self.pop = Button(subframe, text="=", bg="white", width=22, height=4,
                             command=partial(self.ColocaTexto, "="), font=self.font2, borderwidth=0.5)
                self.pop.focus_force()
                self.pop.pack(side=LEFT)
                self.pop.bind("<Return>", self.invoca)

    def ColocaTexto(self, texto):
        if self.t == 1:
            if texto.isnumeric() or texto in "sqrt()":
                self.form.delete(1.0, END)
            else:
                t = 0
        if texto != "=" and texto != "delete":
            self.form.insert(INSERT, texto)
            self.t = 0
        elif texto == "=":
            x = self.form.get(1.0, END)
            self.form.delete(1.0, END)
            self.form.insert(END, eval(x))
            self.t += 1
        else:
            str = self.form.get(1.0, END)
            str = str[:-2]
            self.form.delete(1.0, END)
            self.form.insert(END, str)

    def invoca(self, t):
        self.pop.invoke()

# Cria a nossa tela
instancia = Tk()

# Criamos uma instancia da calculadora
Calculadora(instancia)

# Dá um título a tela
instancia.title('Calculadora')

# Dá um tamanho a tela
instancia.geometry("800x600")

# Definir cor de background
instancia['bg'] = 'white'

instancia.resizable(FALSE, FALSE)

instancia.mainloop()