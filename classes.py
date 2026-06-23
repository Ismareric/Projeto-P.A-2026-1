from tkinter import *
from tkinter import ttk
import tkinter.colorchooser
from abc import ABC, abstractmethod


class figuras:
    def __init__(self):
        self.figuras=[]
    ##polemica do desenhar_figuras! perdeu tudo e ta morando de aluguel como método da classe figuras
    ##cor 1 é o outline, cor 2 é o preenchimento (SUJEITO A MUDANÇA)
    def desenhar_figuras(self, desenho):
        desenho.delete("all")
        for fig in self.figuras:
            fig.desenhar(desenho)
        
##já que toda figura tem que começar e se atualizar, eu criei essa classe abstráta, eu tirei iniciar figura pq meio que o criarobjeto ja faz isso
class figurA(ABC):
    @abstractmethod
    def atualizar_figura_nova(self, event, figs, desenho):
        pass
    @abstractmethod
    def desenhar(self, desenho):
        pass
    @abstractmethod
    def desenharincompleto(self, desenho):
        pass


class linha(figurA):
    def __init__(self,event,cordeoutline):
        self.coord=[event.x,event.y,event.x,event.y]##PONTO INICIAL e ponto final
        self.cor=cordeoutline

    def atualizar_figura_nova(self,event,figs, desenho):
            self.coord[2]=event.x
            self.coord[3]=event.y
            figs.desenhar_figuras(desenho)
            self.desenharincompleto(desenho)

    def desenhar(self, desenho):
        desenho.create_line(self.coord[0],self.coord[1],self.coord[2],self.coord[3],fill=self.cor[1])

    def desenharincompleto(self, desenho):
        desenho.create_line(self.coord[0],self.coord[1],self.coord[2],self.coord[3],fill=self.cor[1],dash=(4,2))


class rabisco(figurA):
    def __init__(self,event,cordeoutline):
        self.coord=[(event.x,event.y)]##PONTO INICIAL e ponto final
        self.cor=cordeoutline
    
    def atualizar_figura_nova(self,event, figs, desenho):
        self.coord.append((event.x, event.y))
        figs.desenhar_figuras(desenho)
        self.desenharincompleto(desenho)
    
    def desenhar(self, desenho):
        desenho.create_line(self.coord,fill=self.cor[1])
    
    def desenharincompleto(self, desenho):
        desenho.create_line(self.coord,fill=self.cor[1],dash=(4,2))


class circulos(figurA):
    def __init__(self,event,cordeoutline,cordeprenchimento):
        self.coord=[event.x,event.y,event.x,event.y]##PONTO INICIAL e ponto final
        self.cordefora=cordeoutline
        self.cordedentro=cordeprenchimento
    
    def atualizar_figura_nova(self,event, figs, desenho):
            self.coord[2]=event.x
            self.coord[3]=event.y
            figs.desenhar_figuras(desenho)
            self.desenharincompleto(desenho)
    
    def desenhar(self, desenho):
      raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
      desenho.create_oval(self.coord[0]-raio,self.coord[1]-raio,self.coord[0]+raio,self.coord[1]+raio,outline=self.cordefora[1],fill=self.cordedentro[1])
    
    def desenharincompleto(self, desenho):
        raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
        desenho.create_oval(self.coord[0]-raio,self.coord[1]-raio,self.coord[0]+raio,self.coord[1]+raio,outline=self.cordefora[1],fill=self.cordedentro[1],dash=(4,2))


class retangulo(figurA):
    def __init__(self,event,cordeoutline,cordeprenchimento):
        self.coord=[event.x,event.y,event.x,event.y]##PONTO INICIAL e ponto final
        self.cordefora=cordeoutline
        self.cordedentro=cordeprenchimento

    def atualizar_figura_nova(self,event, figs, desenho):
            self.coord[2]=event.x
            self.coord[3]=event.y
            figs.desenhar_figuras(desenho)
            self.desenharincompleto(desenho)

    def desenhar(self, desenho):
        desenho.create_rectangle(self.coord[0],self.coord[1],self.coord[2],self.coord[3],outline=self.cordefora[1],fill=self.cordedentro[1])

    def desenharincompleto(self, desenho):
        desenho.create_rectangle(self.coord[0],self.coord[1],self.coord[2],self.coord[3],outline=self.cordefora[1],fill=self.cordedentro[1],dash=(4,2))


class oval(figurA):
    def __init__(self,event,cordeoutline,cordeprenchimento):
        self.coord=[event.x,event.y,event.x,event.y]##PONTO INICIAL e ponto final
        self.cordefora=cordeoutline
        self.cordedentro=cordeprenchimento

    def atualizar_figura_nova(self,event, figs, desenho):
            self.coord[2]=event.x
            self.coord[3]=event.y
            figs.desenhar_figuras(desenho)
            self.desenharincompleto(desenho)

    def desenhar(self, desenho):
        desenho.create_oval(self.coord[0],self.coord[1],self.coord[2],self.coord[3],outline=self.cordefora[1],fill=self.cordedentro[1])

    def desenharincompleto(self, desenho):
        desenho.create_oval(self.coord[0],self.coord[1],self.coord[2],self.coord[3],outline=self.cordefora[1],fill=self.cordedentro[1],dash=(4,2))


class poligonos(figurA):
    def __init__(self,event,cordeoutline,cordeprenchimento):
        self.coord=[event.x,event.y,event.x,event.y]##PONTO INICIAL e ponto final
        self.cordefora=cordeoutline
        self.cordedentro=cordeprenchimento

    def atualizar_figura_nova(self,event, figs, desenho):
            self.coord[-2]=event.x
            self.coord[-1]=event.y
            figs.desenhar_figuras(desenho)
            self.desenharincompleto(desenho)

    def adicionar_ponto(self, event):
        self.coord.append(event.x)
        self.coord.append(event.y)
        
    def desenhar(self, desenho):

        if len(self.coord) >= 6:
            desenho.create_polygon(self.coord, outline=self.cordefora[1], fill=self.cordedentro[1])

    def desenharincompleto(self, desenho):
        if len(self.coord) == 4:
            desenho.create_line(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=self.cordefora[1], dash=(4, 2))

        elif len(self.coord) >= 4:
            desenho.create_polygon(self.coord, outline=self.cordefora[1], fill=self.cordedentro[1], dash=(4, 2))