from tkinter import *
from tkinter import ttk
import tkinter.colorchooser
from abc import ABC, abstractmethod
##aqui a parte nova !
class figuras:
    def __init__(self):
        self.figuras=[]
    ##polemica do desenhar_figuras! perdeu tudo e ta morando de aluguel como método da classe figuras
    ##cor 1 é o outline, cor 2 é o preenchimento (SUJEITO A MUDANÇA)
    def desenhar_figuras(self):
        desenho.delete("all")
        for fig in self.figuras:
            fig.desenhar()
        
##já que toda figura tem que começar e se atualizar, eu criei essa classe abstráta, eu tirei iniciar figura pq meio que o criarobjeto ja faz isso
class figurA(ABC):
    @abstractmethod
    def atualizar_figura_nova(self):
        pass
    @abstractmethod
    def desenhar(self):
        pass
    @abstractmethod
    def desenharincompleto(self):
        pass
class linha(figurA):
    def __init__(self,event,cordeoutline):
        self.coord=[event.x,event.y,event.x,event.y]##PONTO INICIAL e ponto final
        self.cor=cordeoutline
    def atualizar_figura_nova(self,event):
            self.coord[2]=event.x
            self.coord[3]=event.y
            figs.desenhar_figuras()
            self.desenharincompleto()
    def desenhar(self):
        desenho.create_line(self.coord[0],self.coord[1],self.coord[2],self.coord[3],fill=self.cor[1])
    def desenharincompleto(self):
        desenho.create_line(self.coord[0],self.coord[1],self.coord[2],self.coord[3],fill=self.cor[1],dash=(4,2))
class rabisco(figurA):
    def __init__(self,event,cordeoutline):
        self.coord=[(event.x,event.y)]##PONTO INICIAL e ponto final
        self.cor=cordeoutline
    def atualizar_figura_nova(self,event):
        self.coord.append((event.x, event.y))
        figs.desenhar_figuras()
        self.desenharincompleto()
    def desenhar(self):
        desenho.create_line(self.coord,fill=self.cor[1])
    def desenharincompleto(self):
        desenho.create_line(self.coord,fill=self.cor[1],dash=(4,2))
class circulos(figurA):
    def __init__(self,event,cordeoutline,cordeprenchimento):
        self.coord=[event.x,event.y,event.x,event.y]##PONTO INICIAL e ponto final
        self.cordefora=cordeoutline
        self.cordedentro=cordeprenchimento
    def atualizar_figura_nova(self,event):
            self.coord[2]=event.x
            self.coord[3]=event.y
            figs.desenhar_figuras()
            self.desenharincompleto()
    def desenhar(self):
      raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
      desenho.create_oval(self.coord[0]-raio,self.coord[1]-raio,self.coord[0]+raio,self.coord[1]+raio,outline=self.cordefora[1],fill=self.cordedentro[1])
    def desenharincompleto(self):
        raio = ((self.coord[2] - self.coord[0])**2 + (self.coord[3]- self.coord[1])**2)**0.5
        desenho.create_oval(self.coord[0]-raio,self.coord[1]-raio,self.coord[0]+raio,self.coord[1]+raio,outline=self.cordefora[1],fill=self.cordedentro[1],dash=(4,2))
class retangulo(figurA):
    def __init__(self,event,cordeoutline,cordeprenchimento):
        self.coord=[event.x,event.y,event.x,event.y]##PONTO INICIAL e ponto final
        self.cordefora=cordeoutline
        self.cordedentro=cordeprenchimento
    def atualizar_figura_nova(self,event):
            self.coord[2]=event.x
            self.coord[3]=event.y
            figs.desenhar_figuras()
            self.desenharincompleto()
    def desenhar(self):
        desenho.create_rectangle(self.coord[0],self.coord[1],self.coord[2],self.coord[3],outline=self.cordefora[1],fill=self.cordedentro[1])
    def desenharincompleto(self):
        desenho.create_rectangle(self.coord[0],self.coord[1],self.coord[2],self.coord[3],outline=self.cordefora[1],fill=self.cordedentro[1],dash=(4,2))
class oval(figurA):
    def __init__(self,event,cordeoutline,cordeprenchimento):
        self.coord=[event.x,event.y,event.x,event.y]##PONTO INICIAL e ponto final
        self.cordefora=cordeoutline
        self.cordedentro=cordeprenchimento
    def atualizar_figura_nova(self,event):
            self.coord[2]=event.x
            self.coord[3]=event.y
            figs.desenhar_figuras()
            self.desenharincompleto()
    def desenhar(self):
        desenho.create_oval(self.coord[0],self.coord[1],self.coord[2],self.coord[3],outline=self.cordefora[1],fill=self.cordedentro[1])
    def desenharincompleto(self):
        desenho.create_oval(self.coord[0],self.coord[1],self.coord[2],self.coord[3],outline=self.cordefora[1],fill=self.cordedentro[1],dash=(4,2))
# Quando mouse é movido com o botão pressionado
##fig_nova[2] e [3 ] sao as cores, já que elas já se incluem em iniciarfiguranova, achei melhor só usar o valor do proprio fig nova
##eu manti a definição de atualizar figura nova só pra lembrar, vamo remover issso no futuro
#def atualizar_figura_nova(event):
#    global fig_nova
 #   if fig_nova[0] == "rabisco":
 #       fig_nova[1].append((event.x, event.y))
  #  elif fig_nova[0] == "linha":
   #     fig_nova = ("linha", (fig_nova[1][0], fig_nova[1][1], event.x, event.y),fig_nova[2],fig_nova[3])
   # elif fig_nova[0] == "retângulo":
   #     fig_nova = ("retângulo", (fig_nova[1][0], fig_nova[1][1], event.x, event.y),fig_nova[2],fig_nova[3])
   # elif fig_nova[0] == 'oval':
   #     fig_nova = ('oval', (fig_nova[1][0], fig_nova[1][1], event.x, event.y),fig_nova[2],fig_nova[3])
   # else:
   #     fig_nova = ('circulo', (fig_nova[1][0], fig_nova[1][1], event.x, event.y), fig_nova[2], fig_nova[3])
        
   # figs.desenhar_figuras()
   # figs.desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    global fig_nova
    if incompleta(fig_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figs.figuras.append(fig_nova)
        fig_nova=None
    figs.desenhar_figuras()



def incompleta(figura):
    if isinstance(figura,rabisco):
        return len(figura.coord)>1
    else:
        return (figura.coord[0]!=figura.coord[2])and(figura.coord[1]!=figura.coord[3])
#a funcaomudarcordeoutline e a outra checkam pra ver se o usuario nao cancelou/ fechou a janela e muda a cor pra cor do metodo
def mudarcordeoutline():
    global cordeoutline
    corbruta=tkinter.colorchooser.askcolor()
    if corbruta!=(None,None):
        cordeoutline=corbruta
    
def mudarcordedentro(transparente=False):
    global cordeprenchimento
    if transparente :
        cordeprenchimento = (None, '')

    else :
        corbruta=tkinter.colorchooser.askcolor()
    
        if corbruta!=(None,None):
            cordeprenchimento=corbruta
  
def criarObjeto(event):
    global fig_nova
    match formato.get():
        case 'linha':
            fig_nova=linha(event,cordeoutline)
        case 'rabisco':
            fig_nova=rabisco(event,cordeoutline)
        case 'retângulo':
            fig_nova=retangulo(event,cordeoutline,cordeprenchimento)
        case 'oval':
            fig_nova=oval(event,cordeoutline,cordeprenchimento)
        case 'círculos':
            fig_nova=circulos(event,cordeoutline,cordeprenchimento)
        case 'polígonos':
            fig_nova=poligonos(event,cordeoutline,cordeprenchimento)
def modificarcoordenadas(event):
    if fig_nova!=None:
        fig_nova.atualizar_figura_nova(event)
#teoricamente você poderia digitar toda vez que colocasse um widget no frmae mas me poupe
espacaomento={'padx':2,'pady':2}


#lista serve pra guardar as figs desenhadas, o fig_nova guarda as características dessa nova figura  sendo desenhada(incluidndo tipo e coordenadas)
figs=figuras()
fig_nova=None

#criação da tela
janela=Tk()
janelapropria=Frame(janela,width=1280,height=720)

#criação dos textos na tela(obs: preciso adicionar mais)
texto1=Label(janelapropria,text='desenhos e diversões',font='Arial')
texto1.grid(column=0,row=0,**espacaomento,sticky=W)


#menu de opções(precisamos colocar retangulo e oval basicamente)
#obs1 eu nao sabia oque esse string var era até olhar a documentação
#obs2 eu nao sei se precisa ser exatamente atribuido à janela ou poderia ser o frame tbm
formato=StringVar(janela)
menu=ttk.OptionMenu(janelapropria,formato,'linha',*['linha','rabisco','retângulo','oval','círculos'])
menu.grid(column=1,row=0,sticky=W,**espacaomento)

#cores padrão
cordeoutline=(None,'#000000')
cordeprenchimento=(None,'')

#botões
alterarcoresdeoutline=Button(janelapropria,text='Alterar Cor da Borda',command=mudarcordeoutline)
alterarcoresdprenchimento=Button(janelapropria,text='Alterar Cor de preenchimento',command=mudarcordedentro)
semprenchimento = Button(janelapropria, text="Tirar Preenchimento", command=lambda :mudarcordedentro(transparente=True))

alterarcoresdeoutline.grid(column=2,row=0,sticky=W,**espacaomento)
alterarcoresdprenchimento.grid(column=3,row=0,sticky=W,**espacaomento)
semprenchimento.grid(column=4, row=0, sticky=W, **espacaomento)

#criar o canvas
desenho=Canvas(janelapropria,width=1280,height=720,bg='white')
desenho.grid(column=0,row=1,columnspan=5,**espacaomento)

janelapropria.pack()

desenho.bind('<ButtonPress-1>', criarObjeto)
desenho.bind('<B1-Motion>', modificarcoordenadas)
desenho.bind('<ButtonRelease-1>', incluir_figura_nova)##mexer aqui


janela.mainloop()