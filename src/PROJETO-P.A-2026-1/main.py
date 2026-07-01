from modelo.formas import Figuras
from visao.interface import PaintView
from controlador.controlador import PaintControler

def main():
    
    controlador = PaintControler()

    controlador.executar()


main()