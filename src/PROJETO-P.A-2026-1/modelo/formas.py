from abc import ABC, abstractmethod
from tkinter import *
#Apenas guarda as informações referentes às figuras
class Figuras:
    def __init__(self):
        self.figuras = []

class FigurA(ABC):
    @abstractmethod
    def atualizar_figura_nova(self, event):
        pass

    @abstractmethod
    def desenhar(self, canva):
        pass

    @abstractmethod
    def desenhar_incompleto(self, canva):
        pass

class Linha(FigurA):
    def __init__(self, event, cordeoutline):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cor = cordeoutline[1]

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y

    def desenhar(self, canvas):
        canvas.create_line(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=self.cor)

    def desenhar_incompleto(self, canvas):
        canvas.create_line(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=self.cor, dash=(4,4))

class Rabisco(FigurA):
    def __init__(self, event, cordeoutline):
        self.coord = [(event.x, event.y)]
        self.cor = cordeoutline[1]
    
    def atualizar_figura_nova(self, event):
        self.coord.append((event.x, event.y))
    def desenhar(self, canvas):
        canvas.create_line(self.coord, fill=self.cor)

    def desenhar_incompleto(self, canvas):
        canvas.create_line(self.coord, fill=self.cor, dash=(4,4))
    
class Circulos(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]
    
    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y
    def desenhar(self, canvas):
        raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
        canvas.create_oval(self.coord[0]-raio, self.coord[1]-raio, self.coord[0]+raio, self.coord[1]+raio, outline= self.cordefora, fill=self.cordedentro)
    def desenhar_incompleto(self, canvas):
        raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
        canvas.create_oval(self.coord[0]-raio, self.coord[1]-raio, self.coord[0]+raio, self.coord[1]+raio, outline= self.cordefora, fill=self.cordedentro,dash=(4,4))

class Retangulo(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y
    def desenhar(self, canvas):
        canvas.create_rectangle(self.coord, fill=self.cordedentro,outline=self.cordefora)

    def desenhar_incompleto(self, canvas):
        canvas.create_rectangle(self.coord, fill=self.cordedentro,outline=self.cordefora, dash=(4,4))

class Oval(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y
    def desenhar(self, canvas):
        canvas.create_oval(self.coord, fill=self.cordedentro,outline=self.cordefora)

    def desenhar_incompleto(self, canvas):
        canvas.create_oval(self.coord, fill=self.cordedentro,outline=self.cordefora, dash=(4,4))

class Poligonos(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]

    def atualizar_figura_nova(self, event):
        self.coord[-2] = event.x
        self.coord[-1] = event.y

    def adicionar_ponto(self, event):
        self.coord.append(event.x)
        self.coord.append(event.y)
    def desenhar(self, canvas):
        canvas.create_polygon(self.coord, outline=self.cordefora, fill= self.cordedentro )

    def desenhar_incompleto(self, canvas):
        canvas.create_polygon(self.coord, outline=self.cordefora, fill= self.cordedentro ,dash=(4,4))
