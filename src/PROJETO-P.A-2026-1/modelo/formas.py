from abc import ABC, abstractmethod
#Apenas guarda as informações referentes às figuras
class Figuras:
    def __init__(self):
        self.figuras = []

class FigurA(ABC):
    @abstractmethod
    def atualizar_figura_nova(self, event):
        pass

class Linha(FigurA):
    def __init__(self, event, cordeoutline):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cor = cordeoutline[1]

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y

class Rabisco(FigurA):
    def __init__(self, event, cordeoutline):
        self.coord = [(event.x, event.y)]
        self.cor = cordeoutline[1]
    
    def atualizar_figura_nova(self, event):
        self.coord.append((event.x, event.y))
    
class Circulos(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]
    
    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y

class Retangulo(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y

class Oval(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y

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