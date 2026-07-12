from abc import ABC, abstractmethod
from tkinter import *
import pickle
#Apenas guarda as informações referentes às figuras
class Figuras:
    def __init__(self):
        self.figuras = []
        self.indice_selecionado=None

    def salvar_arquivo(self, caminho):
        with open(caminho, 'wb') as arquivo:
            pickle.dump(self.figuras, arquivo)

    def abrir_arquivo(self, caminho):
        with open(caminho, 'rb') as arquivo:
            self.figuras = pickle.load(arquivo)
    def procurar_figura(self,event):
        index=len(self.figuras)-1
        while index>=0:
            if self.figuras[index].verificar_ponto(event):
                for i in self.figuras:
                        i.selecionado=False
                self.indice_selecionado = index
                self.figuras[index].selecionado=True
                return
            else :
                if self.indice_selecionado!=None:
                    for i in self.figuras:
                        i.selecionado=False
                    #self.modelo.figuras[self.indice_selecionado].selecionado=False
                    self.indice_selecionado=None
            index-=1
    def subirum(self,event): #mover para o modelo
        print(self.figuras)
        if self.indice_selecionado!=None and self.indice_selecionado>0:
            self.figuras[self.indice_selecionado],self.figuras[self.indice_selecionado-1]=self.figuras[self.indice_selecionado-1],self.figuras[self.indice_selecionado]
            print(self.figuras)
    def descerum(self,event): #mover para o modelo 
        print(self.figuras)
        if self.indice_selecionado!=None and self.indice_selecionado<len(self.figuras):
            self.figuras[self.indice_selecionado],self.figuras[self.indice_selecionado+1]=self.figuras[self.indice_selecionado+1],self.figuras[self.indice_selecionado-1]
            print(self.figuras)
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

    @abstractmethod
    def verificar_ponto(self, event):
        pass

class Linha(FigurA):
    def __init__(self, event, cordeoutline):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cor = cordeoutline[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y

    def desenhar(self, canvas):
        canvas.create_line(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=self.cor)

    def desenhar_incompleto(self, canvas):
        canvas.create_line(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=self.cor, dash=(4,4))
    def verificar_ponto(self, event):
        pass

class Rabisco(FigurA):
    def __init__(self, event, cordeoutline):
        self.coord = [(event.x, event.y)]
        self.cor = cordeoutline[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord.append((event.x, event.y))
    def desenhar(self, canvas):
        canvas.create_line(self.coord, fill=self.cor)

    def desenhar_incompleto(self, canvas):
        canvas.create_line(self.coord, fill=self.cor, dash=(4,4))
    def verificar_ponto(self, event):
        pass
    
class Circulos(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y
    def desenhar(self, canvas):
        raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
        canvas.create_oval(self.coord[0]-raio, self.coord[1]-raio, self.coord[0]+raio, self.coord[1]+raio, outline= self.cordefora, fill=self.cordedentro)
    def desenhar_incompleto(self, canvas):
        raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
        canvas.create_oval(self.coord[0]-raio, self.coord[1]-raio, self.coord[0]+raio, self.coord[1]+raio, outline= self.cordefora, fill=self.cordedentro,dash=(4,4), stipple="gray75")
    def verificar_ponto(self, event):
        pass    
class Retangulo(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]
        self.selecionado = False
        
    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y
    def desenhar(self, canvas):
        canvas.create_rectangle(self.coord, fill=self.cordedentro,outline=self.cordefora)

    def desenhar_incompleto(self, canvas):
        canvas.create_rectangle(self.coord, fill=self.cordedentro,outline=self.cordefora, dash=(4,4), stipple="gray75")

    def verificar_ponto(self, event):
        x, y = event.x, event.y
        

        if (self.coord[0] <= x <=self.coord[2] and self.coord[1] <= y <=self.coord[3])or(self.coord[0] >= x >=self.coord[2] and self.coord[1] >= y >=self.coord[3])or(self.coord[0] >= x >=self.coord[2] and self.coord[1] <= y <=self.coord[3])or(self.coord[0] <= x <=self.coord[2] and self.coord[1] >= y >=self.coord[3]) :
            return True

        else :
            return False
        

class Oval(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y
    def desenhar(self, canvas):
        canvas.create_oval(self.coord, fill=self.cordedentro,outline=self.cordefora)

    def desenhar_incompleto(self, canvas):
        canvas.create_oval(self.coord, fill=self.cordedentro,outline=self.cordefora, dash=(4,4), stipple="gray75")
    def verificar_ponto(self, event):
        pass
class Poligonos(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord[-2] = event.x
        self.coord[-1] = event.y

    def adicionar_ponto(self, event):
        self.coord.append(event.x)
        self.coord.append(event.y)
    def desenhar(self, canvas):
        canvas.create_polygon(self.coord, outline=self.cordefora, fill= self.cordedentro )

    def desenhar_incompleto(self, canvas):
        canvas.create_polygon(self.coord, outline=self.cordefora, fill= self.cordedentro ,dash=(4,4), stipple="gray75")
    def verificar_ponto(self, event):
        pass