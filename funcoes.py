from tkinter import *
from tkinter import ttk
import tkinter.colorchooser
from classes import *
# Quando mouse é solto
def incluir_figura_nova(event): 
    global fig_nova
    if incompleta(fig_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figs.figuras.append(fig_nova)
        fig_nova=None
    figs.desenhar_figuras()



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
def modificarcoordenadas(event):
    if fig_nova!=None:
        fig_nova.atualizar_figura_nova(event)