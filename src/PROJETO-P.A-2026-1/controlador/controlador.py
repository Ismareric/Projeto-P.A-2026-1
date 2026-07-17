from modelo.formas import *
from visao.interface import PaintView
from controlador.estados import *
from tkinter import filedialog


class PaintControler: #Classe chamada pela Main
    def __init__(self):
        #Inicia modelo e visão
        self.modelo = Figuras()
        self.visao= PaintView()

        #Dicionário de Ferramentas
        self.ferramentas = {
            "Linha" : EstadoLinha(),
            "Rabisco" : EstadoRabisco(),
            "Retângulo" : EstadoRetangulo(),
            "Oval" : EstadoOval(),
            "Círculos" : EstadoCirculo(),
            "Polígonos":EstadoPoligono(),
            'Seleção' : EstadoSeleçao()
        }

        #Estado/Feerramenta atual
        self.estado_atual = self.ferramentas["Linha"]

        #Define as cores padrão
        self.cordeoutline = (None, "#000000")
        self.cordepreenchimento = (None, '')

        #Figura que está sendo desenhada
        self.fig_nova = None

        #É verdadeiro quando o ctrl é pressionado
        self.ctrl=False

        #Monitora o mouse e o teclado
        self.rastrear_mouse()
        
        #Adiciona o comando aos botões da interface
        self.visao.alterarcoresdeoutline.config(command=self.mudarcordeoutline)
        self.visao.alterarcoresdprenchimento.config(command=self.mudarcordepreenchimento)
        self.visao.semprenchimento.config(command=self.remover_preenchimento)
        self.visao.apagartudo.config(command= self.apagartudo )
        self.visao.salvar.config(command=self.salvar)
        self.visao.abrir.config(command= self.abrir)
        self.visao.agrupar.config(command= self.agruparnomodelo)

        #Chama a função de mudar ferramenta toda vez que a StringVar associada ao Opition Menu é alterada
        self.visao.formato.trace_add("write", self.mudar_ferramenta)
    
    #Ao apertar o botão de salvar, abre uma caixa de dialogo do sist para copiar o caminho de onde o arquivo será salvo
    def salvar(self):
        caminho = filedialog.asksaveasfilename(
            title= 'Salvar o Desenho',
            defaultextension=".paint",
            filetypes=[("Arquivos Paint", "*.paint"), ("Todos os arquivos", "*.*")],
            initialdir= "/home/luis/Projeto/Projeto-P.A-2026-1/src/PROJETO-P.A-2026-1/Desenhos Salvos"
        )

        #Salva os desenhos no local selecionando
        if caminho:
            self.modelo.salvar_arquivo(caminho)

    #Ao apertar o botão de salvar, abre uma caixa de dialogo do sist para copiar o caminho de onde o arquivo a ser abrido está
    def abrir(self):
        caminho = filedialog.askopenfilename(
            title="Abrir Desenho",
            filetypes=[("Arquivos Paint", "*.paint"), ("Todos os arquivos", "*.*")],
            initialdir="/home/luis/Projeto/Projeto-P.A-2026-1/src/PROJETO-P.A-2026-1/Desenhos Salvos"
        )

        if caminho:
            self.modelo.abrir_arquivo(caminho)
            self.visao.desenhar_todas(self.modelo.figuras)
    
    #Troca o estado atual
    def mudar_ferramenta(self, *args):
        #Verifica a ferramenta selecionanda no OptionMenu
        nome_ferramenta = self.visao.formato.get()

        #Muda para o estado correspondente no dicionário
        self.estado_atual = self.ferramentas[nome_ferramenta]
        
        #Se houver uma figura incompleta sendo desenhada apaga
        self.fig_nova = None
        #Se houver figuras selecionadas, desceleciona
        self.modelo.removerselecionados()
        #Desenha tudo para aplicar as modificações anteriores
        self.visao.desenhar_todas(self.modelo.figuras)

    # Chamda pela Main para iniciar o loop da interface
    def executar(self): 
        self.visao.iniciar_loop()
    
    #Verifica se a Figura que está sendo desenhada possui coord final e inicial diferentes
    def incompleta(self, figura):
        if isinstance(figura, Rabisco):
            return len(figura.coord)>1
        if isinstance(figura, Poligonos):
            if len(figura.coord) >= 1:
                return True
        else :
            return (figura.coord[0] != figura.coord[2]) and (figura.coord[1]!=figura.coord[3])
    
    #Muda a cor atual
    def mudarcordeoutline(self):
        cor_escolhida = self.visao.abrir_seletor_de_cor()

        if isinstance(self.estado_atual, EstadoSeleçao): #Se estiver no modo de seleção, chama a função que altera a cor de figuras existentes
            self.modelo.alterar_cor_de_fora(cor_escolhida)
            self.visao.desenhar_todas(self.modelo.figuras)

        if cor_escolhida != (None, None): #Verifica se uma cor foi escolhida e altera-a
            self.cordeoutline = cor_escolhida
            self.visao.alterarcoresdeoutline.config(bg=cor_escolhida[1])
    def mudarcordepreenchimento(self): 
        cor_escolhida = self.visao.abrir_seletor_de_cor()

        if isinstance(self.estado_atual, EstadoSeleçao): #Se estiver no modo de seleção, chama a função que altera a cor de figuras existentes
            self.modelo.alterar_cor_de_dentro(cor_escolhida)
            self.visao.desenhar_todas(self.modelo.figuras)

        
        if cor_escolhida != (None, None): #Verifica se uma cor foi escolhida e altera-a
            self.cordepreenchimento = cor_escolhida
            self.visao.alterarcoresdprenchimento.config(bg=cor_escolhida[1])

    #Chamada ao clicar com o botão esquerdo, executa a função do estado atual
    def criar_objeto(self, event): 
        
       self.estado_atual.ao_clicar(self, event)

    
    def modificar_coordenadas(self, event):
        if isinstance(self.estado_atual, EstadoSeleçao):
            if self.modelo.indice_selecionado != []:
                self.estado_atual.ao_arrastar(self, event, selecionado=False)
            
            else :
                self.estado_atual.ao_arrastar(self, event, selecionado=True)
        
        else :
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
        self.ultimo_x = event.x
        self.ultimo_y = event.y
        self.modelo.procurar_figura(event, self.ctrl)
        self.visao.desenhar_todas(self.modelo.figuras)

    def figuras_contidas(self, coord):
        self.modelo.procurar_figuras(coord)
    
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

    def apagartudo(self):
        self.modelo.apagartudo()
        self.visao.desenhar_todas(self.modelo.figuras)

    def copiarnomodelo(self,event):
        self.modelo.copiar()

    def colarnomodelo(self,event):
        self.modelo.colar(event)
        self.visao.desenhar_todas(self.modelo.figuras)
    
    def moverfigura(self,event):

        if self.modelo.indice_selecionado is not None:
            dx = event.x - self.ultimo_x
            dy = event.y - self.ultimo_y
            for i in self.modelo.indice_selecionado:
                figura_selecionada = self.modelo.figuras[i]
                figura_selecionada.modificarposicao(dx, dy)
            
            
            self.ultimo_x = event.x
            self.ultimo_y = event.y
        
    
            self.visao.desenhar_todas(self.modelo.figuras)
        


    def controlpress(self,event):
        self.ctrl=True 
        print(self.modelo.figuras)       
    def controlrelease(self,event):
        self.ctrl=False
    def agruparnomodelo(self):
        self.modelo.agrupar()
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
        self.visao.janela.bind("<Control-c>", self.copiarnomodelo)
        self.visao.janela.bind("<Control-v>", self.colarnomodelo)
        self.visao.janela.bind("<KeyPress-Control_L>", self.controlpress)
        self.visao.janela.bind("<KeyRelease-Control_L>", self.controlrelease)