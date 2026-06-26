from modelo.formas import Figuras, Linha
from visao.interface import PaintView

class PaintControler:
    def __init__(self, modelo, visao):
        self.modelo = modelo
        self.visao=visao
    
    def executar(self):
        self.visao.iniciar_loop()
    