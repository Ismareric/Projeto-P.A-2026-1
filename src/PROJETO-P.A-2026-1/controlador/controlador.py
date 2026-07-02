from modelo.formas import *
from visao.interface import PaintView
from controlador.estados import *


class PaintControler: #Classe chamada pela Main
    def __init__(self):
        self.modelo = Figuras()
        self.visao= PaintView()

        self.ferramentas = {
            "Linha" : EstadoLinha()
        }

        self.estado_atual = self.ferramentas["Linha"]

        self.cordeoutline = (None, "#000000")
        self.cordepreenchimento = (None, '')
        self.fig_nova = None
        self.rastrear_mouse()
        self.visao.alterarcoresdeoutline.config(command=self.mudarcordeoutline)
        self.visao.alterarcoresdprenchimento.config(command=self.mudarcordepreenchimento)
        self.visao.semprenchimento.config(command=self.remover_preenchimento)

        self.visao.formato.trace_add("write", self.mudar_ferramenta)
    
    def mudar_ferramenta(self, *args):
        nome_ferramenta = self.visao.formato.get()

        self.estado_atual = self.ferramentas[nome_ferramenta]
        
        self.fig_nova = None
        self.visao.desenhar_todas(self.modelo.figuras)

    def executar(self): # Chamda pela Main
        self.visao.iniciar_loop()
    
    def incompleta(self, figura): #Mesma função do anterior, falta modificar para aceitar o poligono
        if isinstance(figura, Rabisco):
            return len(figura.coord)>1
        if isinstance(figura, Poligonos):
            return len(figura.coord) >= 6
        else :
            return (figura.coord[0] != figura.coord[2]) and (figura.coord[1]!=figura.coord[3])
    
    def mudarcordeoutline(self): #ainda falta chamar e fazer a outra
        cor_escolhida = self.visao.abrir_seletor_de_cor()
        if cor_escolhida != (None, None):
            self.cordeoutline = cor_escolhida

    def mudarcordepreenchimento(self): 
        cor_escolhida = self.visao.abrir_seletor_de_cor()
        if cor_escolhida != (None, None):
            self.cordepreenchimento = cor_escolhida

    def criar_objeto(self, event): 
        
        if self.visao.formato.get() == 'Polígonos' and self.fig_nova is not None and isinstance(self.fig_nova, Poligonos):
            self.fig_nova.adicionar_ponto(event)
            return
        
        match self.visao.formato.get():
            
            case 'Linha':
                self.fig_nova=Linha(event, self.cordeoutline)
            case 'Rabisco':
                self.fig_nova=Rabisco(event, self.cordeoutline)
            case 'Retângulo':
                self.fig_nova= Retangulo(event, self.cordeoutline, self.cordepreenchimento)
            case 'Oval':
                self.fig_nova= Oval(event, self.cordeoutline, self.cordepreenchimento)
            case 'Círculos':
                self.fig_nova= Circulos(event, self.cordeoutline, self.cordepreenchimento)
            case 'Polígonos':
                self.fig_nova= Poligonos(event, self.cordeoutline, self.cordepreenchimento)
            case _:
                return None

    def modificar_coordenadas(self, event):
        if self.fig_nova != None:
            self.fig_nova.atualizar_figura_nova(event)
            self.visao.desenhar_todas(self.modelo.figuras)
            self.visao.desenhar_incompleto(self.visao.formato.get(), self.fig_nova.coord, self.cordeoutline[1], self.cordepreenchimento[1])

    def incluir_figura_nova(self, event):
        if self.visao.formato.get() == 'Polígonos':
            return

        if self.incompleta(self.fig_nova):
            self.modelo.figuras.append(self.fig_nova)
        self.fig_nova = None
        self.visao.desenhar_todas(self.modelo.figuras)

    def fechar_poligono(self, event):
        if self.fig_nova is not None and isinstance(self.fig_nova, Poligonos):
            if len(self.fig_nova.coord) >= 6:
                self.modelo.figuras.append(self.fig_nova)
            self.fig_nova = None
            self.visao.desenhar_todas(self.modelo.figuras)

    def remover_preenchimento(self):
        self.cordepreenchimento = (None, '') 
    
    def rastrear_mouse(self): #É chamada no __init__
        self.visao.desenho.bind('<ButtonPress-1>', self.criar_objeto) 
        self.visao.desenho.bind('<B1-Motion>', self.modificar_coordenadas) 
        self.visao.desenho.bind('<ButtonRelease-1>', self.incluir_figura_nova) 
        self.visao.desenho.bind('<Button-3>', self.fechar_poligono) 