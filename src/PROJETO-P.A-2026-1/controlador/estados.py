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
    @abstractmethod
    def ao_clicar_direito(self, controlador, event):
        pass


class EstadoLinha(EstadoFerramenta):

    def ao_clicar(self, controlador, event):
        controlador.fig_nova = Linha(event, controlador.cordeoutline)

    def ao_arrastar(self, controlador, event):
        if controlador.fig_nova != None:
            controlador.fig_nova.atualizar_figura_nova(event)
            controlador.visao.desenhar_todas(controlador.modelo.figuras)
            controlador.visao.desenhar_incompleto('Linha',
                                                  controlador.fig_nova.coord,
                                                  controlador.cordeoutline[1]
                                                  controlador.cordepreenchimento[1])
    
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
            controlador.visao.desenhar_incompleto('Rabisco',
                                                  controlador.fig_nova.coord,
                                                  controlador.cordeoutline[1],
                                                  controlador.cordepreenchimento[1])
    
    def ao_soltar(self, controlador, event):
        if controlador.incompleta(controlador.fig_nova):
            controlador.modelo.figuras.append(controlador.fig_nova)
        controlador.fig_nova = None
        controlador.visao.desenhar_todas(controlador.modelo.figuras)

class EstadoRetangulo(EstadoFerramenta):
    def ao_clicar(self, controlador, event):
        controlador.fig_nova = Retangulo(event, controlador.cordeoutline)
    
    def ao_arrastar(self, controlador, event):
        if controlador.fig_nova != None:
            controlador.fig_nova.atualizar_figura_nova(event)
            controlador.visao.desenhar_todas(controlador.modelo.figuras)
            controlador.visao.desenhar_incompleto('Retângulo',
                                                  controlador.fig_nova.coord,
                                                  controlador.cordeoutline[1],
                                                  controlador.cordepreenchimento[1])
    
    def ao_soltar(self, controlador, event):
        if controlador.incompleta(controlador.fig_nova):
            controlador.modelo.figuras.append(controlador.fig_nova)
        controlador.fig_nova = None
        controlador.visao.desenhar_todas(controlador.modelo.figuras)

class EstadoOval(EstadoFerramenta):
    def ao_clicar(self, controlador, event):
        controlador.fig_nova = Rabisco(event, controlador.cordeoutline)
    
    def ao_arrastar(self, controlador, event):
        if controlador.fig_nova != None:
            controlador.fig_nova.atualizar_figura_nova(event)
            controlador.visao.desenhar_todas(controlador.modelo.figuras)
            controlador.visao.desenhar_incompleto('Oval',
                                                  controlador.fig_nova.coord,
                                                  controlador.cordeoutline[1],
                                                  controlador.cordepreenchimento[1])
    
    def ao_soltar(self, controlador, event):
        if controlador.incompleta(controlador.fig_nova):
            controlador.modelo.figuras.append(controlador.fig_nova)
        controlador.fig_nova = None
        controlador.visao.desenhar_todas(controlador.modelo.figuras)