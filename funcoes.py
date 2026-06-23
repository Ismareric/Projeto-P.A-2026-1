from tkinter import *
from tkinter import ttk
import tkinter.colorchooser
from classes import *

def incluir_figura_nova(event): 
    global fig_nova
    if incompleta(fig_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figs.figuras.append(fig_nova)
        fig_nova=None
    figs.desenhar_figuras(desenho)



def incompleta(figura):
    if isinstance(figura,rabisco):
        return len(figura.coord)>1
    else:
        return (figura.coord[0]!=figura.coord[2])and(figura.coord[1]!=figura.coord[3])
#a funcaomudarcordeoutline e a outra checkam pra ver se o usuario nao cancelou/ fechou a janela e muda a cor pra cor do metodo
def mudarcordeoutline():
    global cordeoutline
    corbruta=tkinter.colorchooser.askcolor()
    if corbruta!=(None,None):
        cordeoutline=corbruta
    
def mudarcordedentro(transparente=False):
    global cordeprenchimento
    if transparente :
        cordeprenchimento = (None, '')

    else :
        corbruta=tkinter.colorchooser.askcolor()
    
        if corbruta!=(None,None):
            cordeprenchimento=corbruta
  
def criarObjeto(event):
    dict={'linha':linha}
    global fig_nova

    match formato.get():
        case 'linha':
            fig_nova=linha(event,cordeoutline)
        case 'rabisco':
            fig_nova=rabisco(event,cordeoutline)
        case 'retângulo':
            fig_nova=retangulo(event,cordeoutline,cordeprenchimento)
        case 'oval':
            fig_nova=oval(event,cordeoutline,cordeprenchimento)
        case 'círculos':
            fig_nova=circulos(event,cordeoutline,cordeprenchimento)
        case 'polígonos':
            fig_nova=poligonos(event,cordeoutline,cordeprenchimento)
        case _:
            return None
def modificarcoordenadas(event):
    if fig_nova!=None:
        fig_nova.atualizar_figura_nova(event, figs, desenho)
#teoricamente você poderia digitar toda vez que colocasse um widget no frmae mas me poupe
espacaomento={'padx':2,'pady':2}


#lista serve pra guardar as figs desenhadas, o fig_nova guarda as características dessa nova figura  sendo desenhada(incluidndo tipo e coordenadas)
figs=figuras()
fig_nova=None

#criação da tela
janela=Tk()
janelapropria=Frame(janela,width=1280,height=720)

#criação dos textos na tela(obs: preciso adicionar mais)
texto1=Label(janelapropria,text='desenhos e diversões',font='Arial')
texto1.grid(column=0,row=0,**espacaomento,sticky=W)


#menu de opções(precisamos colocar retangulo e oval basicamente)
#obs1 eu nao sabia oque esse string var era até olhar a documentação
#obs2 eu nao sei se precisa ser exatamente atribuido à janela ou poderia ser o frame tbm
formato=StringVar(janela)
menu=ttk.OptionMenu(janelapropria,formato,'linha',*['linha','rabisco','retângulo','oval','círculos'])
menu.grid(column=1,row=0,sticky=W,**espacaomento)

#cores padrão
cordeoutline=(None,'#000000')
cordeprenchimento=(None,'')

#botões
alterarcoresdeoutline=Button(janelapropria,text='Alterar Cor da Borda',command=mudarcordeoutline)
alterarcoresdprenchimento=Button(janelapropria,text='Alterar Cor de preenchimento',command=mudarcordedentro)
semprenchimento = Button(janelapropria, text="Tirar Preenchimento", command=lambda :mudarcordedentro(transparente=True))

alterarcoresdeoutline.grid(column=2,row=0,sticky=W,**espacaomento)
alterarcoresdprenchimento.grid(column=3,row=0,sticky=W,**espacaomento)
semprenchimento.grid(column=4, row=0, sticky=W, **espacaomento)

#criar o canvas
desenho=Canvas(janelapropria,width=1280,height=720,bg='white')
desenho.grid(column=0,row=1,columnspan=5,**espacaomento)

janelapropria.pack()

desenho.bind('<ButtonPress-1>', criarObjeto)
desenho.bind('<B1-Motion>', modificarcoordenadas)
desenho.bind('<ButtonRelease-1>', incluir_figura_nova)##mexer aqui


janela.mainloop()