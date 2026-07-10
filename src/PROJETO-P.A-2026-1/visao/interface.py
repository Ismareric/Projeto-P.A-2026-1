from tkinter import *
from tkinter import ttk
import tkinter.colorchooser
#Apenas Tkinter


class PaintView: #Classe chamada pela Main
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("1280x720")
        self.janela.rowconfigure(0, weight=1)
        self.janela.columnconfigure(0, weight=1)
        

        
        self.frame = Frame(self.janela)
        self.frame.grid(column=0, row=0, sticky='nsew')
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)

        espacamento = {'padx':2,'pady':2}

        texto1=Label(self.frame,text='desenhos e diversões',font='Arial')
        texto1.grid(column=0,row=0,**espacamento,sticky=W)

        self.formato = StringVar(self.janela)

        menu=ttk.OptionMenu(self.frame,self.formato,'Linha',*['Seleção','Linha','Rabisco','Retângulo','Oval','Círculos', 'Polígonos'])
        menu.grid(column=1,row=0,sticky=W,**espacamento)

        self.alterarcoresdeoutline=Button(self.frame, bg= 'black')
        self.alterarcoresdprenchimento=Button(self.frame)
        self.semprenchimento = Button(self.frame, text="Tirar Preenchimento")
        texto2 = Label(self.frame, text="Cor da Linha:")
        texto3= Label(self.frame, text="Cor de Preenchimento:")

        self.salvar = Button(self.frame, text='Salvar')
        self.abrir = Button(self.frame, text='Abrir')

        self.salvar.grid(column=7, row=0, **espacamento, sticky=W)
        self.abrir.grid(column=8, row=0, **espacamento, sticky=W)

        texto2.grid(column=2, row= 0)
        texto3.grid(column=4, row=0)
        self.alterarcoresdeoutline.grid(column=3,row=0,sticky=W,**espacamento)
        self.alterarcoresdprenchimento.grid(column=5,row=0,sticky=W,**espacamento)
        self.semprenchimento.grid(column=6, row=0, sticky=W, **espacamento)

        self.desenho = Canvas(self.frame, bg='#ffffff')
        self.desenho.grid(column=0, row=1, columnspan=9, **espacamento, sticky= 'nsew')

        

    def iniciar_loop(self): #Chamada pela função Executar do controlador
        self.janela.mainloop()

    def abrir_seletor_de_cor(self): #Função para abrir o seletor de cor, será chamada pelo controler na função pra mudar cor.
        return tkinter.colorchooser.askcolor()
    
    def desenhar_todas(self, figs):
        self.desenho.delete("all")

        for fig in figs:

            if fig.selecionado:
                fig.desenhar_incompleto(self.desenho)
            else:
                fig.desenhar(self.desenho)
            
            
    def desenhar_incompleto(self, fig):
        fig.desenhar_incompleto(self.desenho)
