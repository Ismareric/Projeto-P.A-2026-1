from abc import ABC, abstractmethod
from tkinter import *
import pickle
import math
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
    def removerselecionados(self):
        for i in self.figuras:
                        i.selecionado=False
    def procurar_figura(self,event):
        index=len(self.figuras)-1
        while index>=0:
            if self.figuras[index].verificar_ponto(event):
                self.removerselecionados()
                self.indice_selecionado = index
                self.figuras[index].selecionado=True
                return
            else :
                if self.indice_selecionado!=None:
                    self.removerselecionados()
                    #self.modelo.figuras[self.indice_selecionado].selecionado=False
                    self.indice_selecionado=None
            index-=1

    def subirum(self,event): #mover para o modelo
        if self.indice_selecionado!=None and self.indice_selecionado<len(self.figuras)-1:
            self.figuras[self.indice_selecionado],self.figuras[self.indice_selecionado+1]=self.figuras[self.indice_selecionado+1],self.figuras[self.indice_selecionado]
            self.indice_selecionado += 1
    
    def descerum(self,event): #mover para o modelo 
        if self.indice_selecionado!=None and self.indice_selecionado>0:
            self.figuras[self.indice_selecionado],self.figuras[self.indice_selecionado-1]=self.figuras[self.indice_selecionado-1],self.figuras[self.indice_selecionado]
            self.indice_selecionado -= 1

    def subirtudo(self, event):
        if self.indice_selecionado!=None and self.indice_selecionado<len(self.figuras)-1:
            figura = self.figuras.pop(self.indice_selecionado)
            self.figuras.append(figura)

            self.indice_selecionado = len(self.figuras)-1

    def descertudo(self, event):
        if self.indice_selecionado != None and self.indice_selecionado>0:
            figura = self.figuras.pop(self.indice_selecionado)
            self.figuras.insert(0, figura)

            self.indice_selecionado = 0
    
    def apagar(self, event):
        if self.indice_selecionado != None :
            self.figuras.pop(self.indice_selecionado)

            self.indice_selecionado = None
    
    def alterar_cor_de_dentro(self, cor):
        self.figuras[self.indice_selecionado].cordedentro = cor[1]

    def alterar_cor_de_fora(self, cor):
        self.figuras[self.indice_selecionado].cordefora = cor[1]


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
    
    # distancia entre o segmento ((x1,y1), (x2,y2)) e o ponto (px, py)
    def distancia(self, x1, y1, x2, y2, px, py) :
        # Vetor direção do segmento (AB)
        dx = x2 - x1
        dy = y2 - y1

        # Comprimento do segmento ao quadrado
        ab_len_sq = dx**2 + dy**2

        # Caso o segmento seja apenas um ponto (A e B são iguais)
        if ab_len_sq == 0:
            return math.sqrt((px - x1)**2 + (py - y1)**2)

        # Vetor do ponto A ao ponto P (AP)
        ap_x = px - x1
        ap_y = py - y1

        # Produto escalar de AP e AB dividido pelo comprimento ao quadrado (fator t)
        t = (ap_x * dx + ap_y * dy) / ab_len_sq

        # Limita t entre 0 e 1 para garantir que a projeção fique dentro do segmento
        t = max(0.0, min(1.0, t))

        # Coordenadas do ponto mais próximo no segmento
        ponto_proximo_x = x1 + t * dx
        ponto_proximo_y = y1 + t * dy

        return math.sqrt((px - ponto_proximo_x)**2 + (py - ponto_proximo_y)**2)
    
class Linha(FigurA):
    def __init__(self, event, cordeoutline):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y

    def desenhar(self, canvas):
        canvas.create_line(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=self.cordefora)

    def desenhar_incompleto(self, canvas):
        canvas.create_line(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=self.cordefora, dash=(4,4))
    def verificar_ponto(self, event):
        
        x1, y1, x2, y2 = self.coord
        px, py = event.x, event.y
        
        if self.distancia(x1, y1, x2, y2, px, py) <= 10:
            return True
        else :
            return False

class Rabisco(FigurA):
    def __init__(self, event, cordeoutline):
        self.coord = [(event.x, event.y)]
        self.cordefora = cordeoutline[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord.append((event.x, event.y))
    def desenhar(self, canvas):
        canvas.create_line(self.coord, fill=self.cordefora)

    def desenhar_incompleto(self, canvas):
        canvas.create_line(self.coord, fill=self.cordefora, dash=(4,4))
    
    def verificar_ponto(self, event):
        
        for i in range(len(self.coord)-2):
            x1, y1 = self.coord[i]
            x2, y2 = self.coord[i+1]
            px, py = event.x, event.y

            if self.distancia(x1, y1, x2, y2, px, py) <= 10:
                return True
        
        return False

    
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
        self.raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
        canvas.create_oval(self.coord[0]-self.raio, self.coord[1]-self.raio, self.coord[0]+self.raio, self.coord[1]+self.raio, outline= self.cordefora, fill=self.cordedentro)
    def desenhar_incompleto(self, canvas):
        raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
        canvas.create_oval(self.coord[0]-raio, self.coord[1]-raio, self.coord[0]+raio, self.coord[1]+raio, outline= self.cordefora, fill=self.cordedentro,dash=(4,4), stipple="gray75")
    def verificar_ponto(self, event):
        x1, y1 =  self.coord[0], self.coord[1]
        px, py = event.x, event.y

        if (px - x1)**2 + (py - y1)**2 <= self.raio**2:
            return True
        else :
            return False
        
          
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
        x1, y1, x2, y2 = self.coord
        px, py = event.x, event.y

        h, k = (x1 + x2)/2, (y1 + y2)/2
        a, b = abs(x2-x1)/2, abs(y2 -y1)/2

        if (((px - h)**2)/a**2) + (((py - k)**2)/b**2) <= 1  :
            return True
        else: 
            return False

class Poligonos(FigurA):
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [(event.x, event.y), (event.x, event.y)]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord[-1] = (event.x,event.y)

    def adicionar_ponto(self, event):
        self.coord.append((event.x,event.y))
    def desenhar(self, canvas):
        print(self.coord)
        canvas.create_polygon(self.coord, outline=self.cordefora, fill= self.cordedentro )

    def desenhar_incompleto(self, canvas):
        canvas.create_polygon(self.coord, outline=self.cordefora, fill= self.cordedentro ,dash=(4,4), stipple="gray75")
    def verificar_ponto(self, event):
        x,y=event.x,event.y
        dentro = False
        n = len(self.coord)

        # Se o polígono não tiver pelo menos 3 vértices, não é um polígono válido
        if n < 3:
            return dentro

        # Inicializa o último vértice do polígono como ponto de partida
        p1x, p1y = self.coord[0]

        for i in range(n + 1):
            # Avança para o próximo vértice
            p2x, p2y = self.coord[i % n]

            # Verifica se o raio horizontal intercepta a aresta do polígono
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        # Calcula a interceptação X exata da aresta
                        if p1y != p2y:
                            x_interceptado = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        # Se o ponto estiver à esquerda da interceptação, inverte o estado
                        if p1x == p2x or x <= x_interceptado:
                            dentro = not dentro

            p1x, p1y = p2x, p2y

        return dentro