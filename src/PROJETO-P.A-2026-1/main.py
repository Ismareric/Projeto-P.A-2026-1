from modelo.formas import Figuras
from visao.interface import PaintView
from controlador.controlador import PaintControler

def main():
    modelo = Figuras()
    visao = PaintView()
    
    controlador = PaintControler(modelo, visao)

    controlador.executar()

if __name__ == "__main__":
    main()