from abc import ABC, abstractmethod
from modelo.formas import *

class EstadoFerramenta(ABC):
    @abstractmethod
    def ao_clicar(self, controlador, event):
        pass
    @abstractmethod
    def ao_arrastar(self, controlador, event):
        pass
    @abstractmethod
    def ao_soltar(self, controlador, event):
        pass
    


class EstadoLinha(EstadoFerramenta):

    def ao_clicar(self, controlador, event):
        controlador.fig_nova = Linha(event, controlador.cordeoutline)

    def ao_arrastar(self, controlador, event):
        if controlador.fig_nova != None:
            controlador.fig_nova.atualizar_figura_nova(event)
            controlador.visao.desenhar_todas(controlador.modelo.figuras)
            controlador.visao.desenhar_incompleto(controlador.fig_nova)
    
    def ao_soltar(self, controlador, event):
        if controlador.incompleta(controlador.fig_nova):
            controlador.modelo.figuras.append(controlador.fig_nova)
        controlador.fig_nova = None
        controlador.visao.desenhar_todas(controlador.modelo.figuras)

class EstadoRabisco(EstadoFerramenta):
    def ao_clicar(self, controlador, event):
        controlador.fig_nova = Rabisco(event, controlador.cordeoutline)
    
    def ao_arrastar(self, controlador, event):
        if controlador.fig_nova != None:
            controlador.fig_nova.atualizar_figura_nova(event)
            controlador.visao.desenhar_todas(controlador.modelo.figuras)
            controlador.visao.desenhar_incompleto(controlador.fig_nova)
    
    def ao_soltar(self, controlador, event):
        if controlador.incompleta(controlador.fig_nova):
            controlador.modelo.figuras.append(controlador.fig_nova)
        controlador.fig_nova = None
        controlador.visao.desenhar_todas(controlador.modelo.figuras)

class EstadoRetangulo(EstadoFerramenta):
    def ao_clicar(self, controlador, event):
        controlador.fig_nova = Retangulo(event, controlador.cordeoutline,controlador.cordepreenchimento)
    
    def ao_arrastar(self, controlador, event):
        if controlador.fig_nova != None:
            controlador.fig_nova.atualizar_figura_nova(event)
            controlador.visao.desenhar_todas(controlador.modelo.figuras)
            controlador.visao.desenhar_incompleto(controlador.fig_nova)
    
    def ao_soltar(self, controlador, event):
        if controlador.incompleta(controlador.fig_nova):
            controlador.modelo.figuras.append(controlador.fig_nova)
        controlador.fig_nova = None
        controlador.visao.desenhar_todas(controlador.modelo.figuras)

class EstadoOval(EstadoFerramenta):
    def ao_clicar(self, controlador, event):
        controlador.fig_nova = Oval(event, controlador.cordeoutline, controlador.cordepreenchimento)
    
    def ao_arrastar(self, controlador, event):
        if controlador.fig_nova != None:
            controlador.fig_nova.atualizar_figura_nova(event)
            controlador.visao.desenhar_todas(controlador.modelo.figuras)
            controlador.visao.desenhar_incompleto(controlador.fig_nova)
    
    def ao_soltar(self, controlador, event):
        if controlador.incompleta(controlador.fig_nova):
            controlador.modelo.figuras.append(controlador.fig_nova)
        controlador.fig_nova = None
        controlador.visao.desenhar_todas(controlador.modelo.figuras)

class EstadoCirculo(EstadoFerramenta):
    def ao_clicar(self, controlador, event):
        controlador.fig_nova = Circulos(event, controlador.cordeoutline, controlador.cordepreenchimento)
    
    def ao_arrastar(self, controlador, event):
        if controlador.fig_nova != None:
            controlador.fig_nova.atualizar_figura_nova(event)
            controlador.visao.desenhar_todas(controlador.modelo.figuras)
            controlador.visao.desenhar_incompleto(controlador.fig_nova)

    def ao_soltar(self, controlador, event):
        if controlador.incompleta(controlador.fig_nova):
            controlador.modelo.figuras.append(controlador.fig_nova)
        controlador.fig_nova = None
        controlador.visao.desenhar_todas(controlador.modelo.figuras)

class EstadoPoligono(EstadoFerramenta):
    def ao_clicar(self, controlador, event):
        if  controlador.fig_nova is not None and isinstance(controlador.fig_nova, Poligonos):
            controlador.fig_nova.adicionar_ponto(event)
            return
        controlador.fig_nova = Poligonos(event, controlador.cordeoutline, controlador.cordepreenchimento)
    
    def ao_arrastar(self, controlador, event):
        if controlador.fig_nova != None:
            controlador.fig_nova.atualizar_figura_nova(event)
            controlador.visao.desenhar_todas(controlador.modelo.figuras)
            controlador.visao.desenhar_incompleto(controlador.fig_nova)

    def ao_soltar(self, controlador, event):
        return
    
    def ao_clicar_direito(self,controlador,event):
        if controlador.incompleta(controlador.fig_nova):
            controlador.modelo.figuras.append(controlador.fig_nova)
        controlador.fig_nova = None
        controlador.visao.desenhar_todas(controlador.modelo.figuras)

class EstadoSeleçao(EstadoFerramenta):
    def ao_clicar(self, controlador, event):
        controlador.procurar_figuranomodelo(event)
    def ao_arrastar(self, controlador, event):
        pass
    def ao_soltar(self, controlador, event):
        pass