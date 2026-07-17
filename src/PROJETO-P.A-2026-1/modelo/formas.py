from abc import ABC, abstractmethod
from tkinter import *
import pickle
import math
import copy
#Apenas guarda as informações referentes às figuras
class Figuras:
    def __init__(self):
        #Lista com todas as figuras
        self.figuras = []

        #Lista com os Indices das figuras selecionadas
        self.indice_selecionado=[]

        #Lista dos objetos copiados
        self.objetoscopiados=[]

    def salvar_arquivo(self, caminho):
        with open(caminho, 'wb') as arquivo:
            pickle.dump(self.figuras, arquivo)

    def abrir_arquivo(self, caminho):
        with open(caminho, 'rb') as arquivo:
            self.figuras = pickle.load(arquivo)

    #Desseleciona as figuras quando clica em uma área vazia
    def removerselecionados(self):
        for i in self.figuras:
                        i.selecionado=False

    #Procura(de cima para baixo) a figura que contem o ponto clicado no modo de seleção
    def procurar_figura(self,event,ctrl):

        index = len(self.figuras) - 1
    
        while index >= 0:
            if self.figuras[index].verificar_ponto(event):
                if index in self.indice_selecionado:
                    
                    return
                
                if not ctrl:
                    self.removerselecionados()
                    self.indice_selecionado = [index]
                else:
                    self.indice_selecionado.append(index)
                
                self.figuras[index].selecionado = True
                return 
            index -= 1
            
        if not ctrl:
            self.removerselecionados()
            self.indice_selecionado = []

    def procurar_figuras(self, coord):
        """ Função que deveria procurar as figuras dentro do quadrado de seleção"""
        pass

    #trocar layer       
    def subirum(self,event): 
        if self.indice_selecionado!=None and self.indice_selecionado<len(self.figuras)-1:
            self.figuras[self.indice_selecionado],self.figuras[self.indice_selecionado+1]=self.figuras[self.indice_selecionado+1],self.figuras[self.indice_selecionado]
            self.indice_selecionado += 1
    
    def descerum(self,event): 
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
    
    #Apaga as figuras selecionadas
    def apagar(self, event):
        if self.indice_selecionado != [] :  #Verifica se existe figura selecionada
            objetosdeletados=[] #Cria a lista de objetos que devem ser deletados
            
            for obj in self.figuras: #Varre toda a lista de figuras 
                if obj.selecionado==True: #Verifica se o objeto atual está selecionando
                    objetosdeletados.append(obj) #SE estiver, adiciona à lista de objetos que devem ser apagados
            
            for i in objetosdeletados: #Varre toda a lista de objetos a serem apagados
                self.figuras.remove(i) #Apaga os objetos

            self.indice_selecionado = [] #Limpa a lista dos selecionado, pois, eles já foram apagados

    #Apaga toda a lista de figuras
    def apagartudo(self):
        self.figuras = []

    def copiar(self):
        self.objetoscopiados = [] #Cria lista do objts copiados
        if self.indice_selecionado!=[]: #Verifica se há seleção
            for i in self.indice_selecionado: #Navega pela lista de selecionados
                self.objetoscopiados.append(copy.deepcopy(self.figuras[i])) #Cria um cópia do obj selecionado
                self.objetoscopiados[i].selecionado=False #Tira o atributo de selecionado desse obj para que quando ele seja colado ele não esteja selecionado
    
    def colar(self,event):
        objetoscolados=copy.deepcopy(self.objetoscopiados) #CRia uma cópia da lista de copiados.
        for i in objetoscolados: #Navega pela lista
            i.modificarposicao(15, 15) #Altera a posição de  coda obj para que ele não seja colado em cima do original
        self.figuras.extend(objetoscolados) #Adiciona os objs colados à lista de figuras
    
    #Muda cor das selecionadas
    def alterar_cor_de_dentro(self, cor):
        if  self.indice_selecionado !=[]: #Verifica se há seleccionanda
            for i in self.indice_selecionado: #Navega pelos selecionados
                self.figuras[i].cordedentro = cor[1] #Muda a cor
    #Muda cor das selecionadas
    def alterar_cor_de_fora(self, cor):
        if  self.indice_selecionado !=[]: #Verifica se há seleccionanda
            for i in self.indice_selecionado: #Navega pelos selecionados
                self.figuras[i].cordefora = cor[1] #Muda a cor

#Classe abstrata para os métodos de cada figura
class FigurA(ABC):
    @abstractmethod
    def atualizar_figura_nova(self, event):
        """Modifica as coords quando o mouse é movido"""
        pass

    @abstractmethod
    def desenhar(self, canva):
        """Desenha a figura"""
        pass

    @abstractmethod
    def desenhar_incompleto(self, canva):
        """Desenha com pontilhado"""
        pass

    @abstractmethod
    def verificar_ponto(self, event):
        """Verifica se um ponto está contido na figura"""
        pass
    
    # Modifica a posição das figuras, selecionadas(Exeto Rabisco e Poligono)
    def modificarposicao(self, dx, dy):
        self.coord = [
        self.coord[0] + dx, 
        self.coord[1] + dy, 
        self.coord[2] + dx, 
        self.coord[3] + dy
        ]   

    # distancia entre o segmento ((x1,y1), (x2,y2)) e o ponto (px, py)
    #Serve para verificar se o usuário clicou proximo a uma linha ou rabisco
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
    #Cria a linha
    def __init__(self, event, cordeoutline):
        self.coord = [event.x, event.y, event.x, event.y]
        self.cordefora = cordeoutline[1]
        self.selecionado = False

    #Atualiza as coord ao mover o mouse
    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y
    
    def desenhar(self, canvas):
        canvas.create_line(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=self.cordefora)

    def desenhar_incompleto(self, canvas):
        canvas.create_line(self.coord[0], self.coord[1], self.coord[2], self.coord[3], fill=self.cordefora, dash=(4,4))
    def verificar_ponto(self, event):
        
        x1, y1, x2, y2 = self.coord #Coords ini e fin
        px, py = event.x, event.y #Ponto clicado
        
        if self.distancia(x1, y1, x2, y2, px, py) <= 10:
            return True
        else :
            return False
    

class Rabisco(FigurA):
    #Cria o rabisco
    def __init__(self, event, cordeoutline):
        self.coord = [[event.x, event.y]]
        self.cordefora = cordeoutline[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord.append([event.x, event.y])
    def desenhar(self, canvas):
        canvas.create_line(self.coord, fill=self.cordefora)

    def desenhar_incompleto(self, canvas):
        canvas.create_line(self.coord, fill=self.cordefora, dash=(4,4))
    
    def verificar_ponto(self, event):
        
        #Separa o rabisco em várias linhas e verifica a distancia
        for i in range(len(self.coord)-2):
            x1, y1 = self.coord[i]
            x2, y2 = self.coord[i+1]
            px, py = event.x, event.y

            if self.distancia(x1, y1, x2, y2, px, py) <= 10:
                return True
        
        return False
    def modificarposicao(self, dx, dy):
        for i in self.coord:
            i[0] += dx
            i[1] += dy

    
class Circulos(FigurA):
    #Cria o circulo
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
    #Cria o retangulo
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
    #Cria o oval
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
    #CRia o poligono
    def __init__(self, event, cordeoutline, cordeprenchimento):
        self.coord = [[event.x, event.y], [event.x, event.y]]
        self.cordefora = cordeoutline[1]
        self.cordedentro = cordeprenchimento[1]
        self.selecionado = False

    def atualizar_figura_nova(self, event):
        self.coord[-1] = [event.x,event.y]

    def adicionar_ponto(self, event):
        self.coord.append([event.x,event.y])
    def desenhar(self, canvas):
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
    def modificarposicao(self, dx, dy):
        for i in self.coord:
            i[0] += dx
            i[1] += dy

#Classe para criar o retangulo de seleçaõ (Incompleta)
class Selecao(FigurA):
    def __init__(self, event):
        self.coord = [event.x, event.y, event.x, event.y]
    
    def desenhar(self, canva):
        return super().desenhar(canva)
    def atualizar_figura_nova(self, event):
        self.coord[2] = event.x
        self.coord[3] = event.y

    def desenhar_incompleto(self, canva):
        canva.create_rectangle(self.coord, dash=(4,4))
    def verificar_ponto(self, event):
        return super().verificar_ponto(event)