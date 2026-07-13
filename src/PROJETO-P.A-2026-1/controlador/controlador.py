from modelo.formas import *
from visao.interface import PaintView
from controlador.estados import *
from tkinter import filedialog


class PaintControler: #Classe chamada pela Main
    def __init__(self):
        self.modelo = Figuras()
        self.visao= PaintView()

        self.ferramentas = {
            "Linha" : EstadoLinha(),
            "Rabisco" : EstadoRabisco(),
            "Retângulo" : EstadoRetangulo(),
            "Oval" : EstadoOval(),
            "Círculos" : EstadoCirculo(),
            "Polígonos":EstadoPoligono(),
            'Seleção' : EstadoSeleçao()
        }

        self.estado_atual = self.ferramentas["Linha"]

        self.cordeoutline = (None, "#000000")
        self.cordepreenchimento = (None, '')
        self.fig_nova = None
        self.rastrear_mouse()
        self.visao.alterarcoresdeoutline.config(command=self.mudarcordeoutline)
        self.visao.alterarcoresdprenchimento.config(command=self.mudarcordepreenchimento)
        self.visao.semprenchimento.config(command=self.remover_preenchimento)
        self.visao.salvar.config(command=self.salvar)
        self.visao.abrir.config(command= self.abrir)

        self.visao.formato.trace_add("write", self.mudar_ferramenta)

    def salvar(self):
        caminho = filedialog.asksaveasfilename(
            title= 'Salvar o Desenho',
            defaultextension=".paint",
            filetypes=[("Arquivos Paint", "*.paint"), ("Todos os arquivos", "*.*")],
            initialdir= "/home/luis/Projeto/Projeto-P.A-2026-1/src/PROJETO-P.A-2026-1/Desenhos Salvos"
        )

        if caminho:
            self.modelo.salvar_arquivo(caminho)

    def abrir(self):
        caminho = filedialog.askopenfilename(
            title="Abrir Desenho",
            filetypes=[("Arquivos Paint", "*.paint"), ("Todos os arquivos", "*.*")],
            initialdir="/home/luis/Projeto/Projeto-P.A-2026-1/src/PROJETO-P.A-2026-1/Desenhos Salvos"
        )

        if caminho:
            self.modelo.abrir_arquivo(caminho)
            self.visao.desenhar_todas(self.modelo.figuras)
    
    def mudar_ferramenta(self, *args):
        nome_ferramenta = self.visao.formato.get()

        self.estado_atual = self.ferramentas[nome_ferramenta]
        
        self.fig_nova = None
        self.modelo.removerselecionados()
        self.visao.desenhar_todas(self.modelo.figuras)

    def executar(self): # Chamda pela Main
        self.visao.iniciar_loop()
    
    def incompleta(self, figura):
        if isinstance(figura, Rabisco):
            return len(figura.coord)>1
        if isinstance(figura, Poligonos):
            if len(figura.coord) >= 1:
                print('oba')
                return True
        else :
            return (figura.coord[0] != figura.coord[2]) and (figura.coord[1]!=figura.coord[3])
    
    def mudarcordeoutline(self):
        cor_escolhida = self.visao.abrir_seletor_de_cor()

        if isinstance(self.estado_atual, EstadoSeleçao):
            self.modelo.alterar_cor_de_fora(cor_escolhida)
            self.visao.desenhar_todas(self.modelo.figuras)

        if cor_escolhida != (None, None):
            self.cordeoutline = cor_escolhida
            self.visao.alterarcoresdeoutline.config(bg=cor_escolhida[1])

    def mudarcordepreenchimento(self): 
        cor_escolhida = self.visao.abrir_seletor_de_cor()

        if isinstance(self.estado_atual, EstadoSeleçao):
            self.modelo.alterar_cor_de_dentro(cor_escolhida)
            self.visao.desenhar_todas(self.modelo.figuras)

        
        if cor_escolhida != (None, None):
            self.cordepreenchimento = cor_escolhida
            self.visao.alterarcoresdprenchimento.config(bg=cor_escolhida[1])

    def criar_objeto(self, event): 
        
       self.estado_atual.ao_clicar(self, event)

    
    def modificar_coordenadas(self, event):
       
       self.estado_atual.ao_arrastar(self, event)

    def incluir_figura_nova(self, event):
        self.estado_atual.ao_soltar(self, event)

    def fechar_poligono(self, event):
        if self.fig_nova is not None and isinstance(self.fig_nova, Poligonos):
            if len(self.fig_nova.coord) >= 3:
                self.modelo.figuras.append(self.fig_nova)
            self.fig_nova = None
            self.visao.desenhar_todas(self.modelo.figuras)

    def remover_preenchimento(self):

        if isinstance(self.estado_atual, EstadoSeleçao):
            self.modelo.alterar_cor_de_dentro((None, ''))
            self.visao.desenhar_todas(self.modelo.figuras)

        else :

            self.cordepreenchimento = (None, '') 
            self.visao.alterarcoresdprenchimento.config(bg="#d9d9d9")
    
    def procurar_figuranomodelo(self, event): #mover para o modelo
        self.modelo.procurar_figura(event)
        self.visao.desenhar_todas(self.modelo.figuras)
    
    def subirumnomodelo(self,event): #mover para o modelo
        self.modelo.subirum(event)
        self.visao.desenhar_todas(self.modelo.figuras)
    
    def descerumnomodelo(self,event): #mover para o modelo 
        self.modelo.descerum(event)
        self.visao.desenhar_todas(self.modelo.figuras)

    def subirtudomodelo(self, event):
        self.modelo.subirtudo(event)
        self.visao.desenhar_todas(self.modelo.figuras)

    def descertudomodelo(self, event):
        self.modelo.descertudo(event)
        self.visao.desenhar_todas(self.modelo.figuras)

    def apagar(self, event):
        self.modelo.apagar(event)
        self.visao.desenhar_todas(self.modelo.figuras)
   
    def rastrear_mouse(self): #É chamada no __init__
        self.visao.desenho.bind('<ButtonPress-1>', self.criar_objeto) 
        self.visao.desenho.bind('<B1-Motion>', self.modificar_coordenadas) 
        self.visao.desenho.bind('<ButtonRelease-1>', self.incluir_figura_nova) 
        self.visao.desenho.bind('<Button-3>', self.fechar_poligono) 
        self.visao.janela.bind('<Right>', self.subirumnomodelo)
        self.visao.janela.bind('<Left>', self.descerumnomodelo)
        self.visao.janela.bind('<Up>', self.subirtudomodelo)
        self.visao.janela.bind('<Down>', self.descertudomodelo)
        self.visao.janela.bind("<Delete>", self.apagar)
        