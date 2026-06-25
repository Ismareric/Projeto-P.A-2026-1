from tkinter import *
from tkinter import ttk
import tkinter.colorchooser

class PaintView:
    def __init__(self):
        self.janela = Tk()
        self.frame = Frame(self.janela,width=1280,height=720)

        espacamento = {'padx':2,'pady':2}

        texto1=Label(self.frame,text='desenhos e diversões',font='Arial')
        texto1.grid(column=0,row=0,**espacamento,sticky=W)

        self.formato = StringVar(self.janela)

        menu=ttk.OptionMenu(self.frame,self.formato,'linha',*['linha','rabisco','retângulo','oval','círculos', 'polígonos'])
        menu.grid(column=1,row=0,sticky=W,**espacamento)

        self.alterarcoresdeoutline=Button(self.frame,text='Alterar Cor da Borda')
        self.alterarcoresdprenchimento=Button(self.frame,text='Alterar Cor de preenchimento')
        self.semprenchimento = Button(self.frame, text="Tirar Preenchimento")

        self.alterarcoresdeoutline.grid(column=2,row=0,sticky=W,**espacamento)
        self.alterarcoresdprenchimento.grid(column=3,row=0,sticky=W,**espacamento)
        self.semprenchimento.grid(column=4, row=0, sticky=W, **espacamento)

        self.desenho = Canvas(self.frame, width=1280, height=720, bg='#ffffff')
        self.desenho.grid(column=0, row=1, columnspan=5, **espacamento)

        self.frame.pack()

    def iniciar_loop(self):
        self.janela.mainloop()

    def abrir_seletor_de_cor(self):
        return tkinter.colorchooser.askcolor()
    
    def desenhar_todas(self, figs):
        self.desenho.delete("all")

        for fig in figs:

            if fig.__class__.__name__ == "Linha":
                self.desenho.create_line(fig.coord[0], fig.coord[1], fig.coord[2], fig.coord[3], fill=fig.cor[1])
    
    def desenhar_incompleto(self, forma, coord, cordeoutline, cordepreenchimento):
        if forma == "linha":
            self.desenho.create_line(coord[0], coord[1], coord[2], coord[3], fill= cordeoutline[1], dash=(4,4))
    