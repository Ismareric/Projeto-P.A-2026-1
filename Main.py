from tkinter import *
from tkinter import ttk
import tkinter.colorchooser

#Identifica qual figura será desenhada
def iniciar_figura_nova(event): 
    global fig_nova
    if formato.get() == 'linha':
        fig_nova = ("linha", (event.x, event.y, event.x, event.y),cordeoutline[1],cordeprenchimento[1])
    elif formato.get() == 'rabisco':
        fig_nova = ("rabisco", [(event.x, event.y)],cordeoutline[1],cordeprenchimento[1])
    elif formato.get() == 'retângulo':
        fig_nova = ("retângulo", (event.x, event.y, event.x, event.y),cordeoutline[1],cordeprenchimento[1])
    elif formato.get() == 'oval':
        fig_nova = ('oval', (event.x, event.y, event.x, event.y),cordeoutline[1],cordeprenchimento[1])
    else : #circulo 
        fig_nova = ('circulo', (event.x, event.y, event.x, event.y),cordeoutline[1],cordeprenchimento[1])

# Quando mouse é movido com o botão pressionado
##fig_nova[2] e [3 ] sao as cores, já que elas já se incluem em iniciarfiguranova, achei melhor só usar o valor do proprio fig nova
def atualizar_figura_nova(event):
    global fig_nova
    if fig_nova[0] == "rabisco":
        fig_nova[1].append((event.x, event.y))
    elif fig_nova[0] == "linha":
        fig_nova = ("linha", (fig_nova[1][0], fig_nova[1][1], event.x, event.y),fig_nova[2],fig_nova[3])
    elif fig_nova[0] == "retângulo":
        fig_nova = ("retângulo", (fig_nova[1][0], fig_nova[1][1], event.x, event.y),fig_nova[2],fig_nova[3])
    elif fig_nova[0] == 'oval':
        fig_nova = ('oval', (fig_nova[1][0], fig_nova[1][1], event.x, event.y),fig_nova[2],fig_nova[3])
    else:
        fig_nova = ('circulo', (fig_nova[1][0], fig_nova[1][1], event.x, event.y), fig_nova[2], fig_nova[3])
        
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(fig_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figs.append(fig_nova) 
    desenhar_figuras()
##cor 1 é o outline, cor 2 é o preenchimento
def desenhar_figuras():
    desenho.delete("all")
    for fig, values,cor1,cor2 in figs:
        if fig == "linha":
            desenho.create_line(values[0], values[1], values[2], values[3],fill=cor1)
        elif fig == "rabisco":
            desenho.create_line(values,fill=cor1)
        elif fig == "retângulo":
            desenho.create_rectangle(values[0], values[1], values[2], values[3],outline=cor1,fill=cor2)
        elif fig == 'oval':
            desenho.create_oval(values[0], values[1], values[2], values[3],outline=cor1,fill=cor2)
        else : #circulo
            raio = ((values[2] - values[0])**2 + (values[3]- values[1])**2)**0.5
            desenho.create_oval(values[0] - raio, values[1] - raio, values[0]+raio, values[1] + raio,outline=cor1,fill=cor2)
def desenhar_figura_nova():
    fig, values,cor1,cor2 = fig_nova
    if fig == "linha":
        desenho.create_line(values[0], values[1], values[2], values[3], dash=(4, 2),fill=cor1)
    elif fig == "rabisco":
        desenho.create_line(values, dash=(4, 2),fill=cor1)
    elif fig == "retângulo":
        desenho.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2),outline=cor1,fill=cor2)
    elif fig == 'oval':
        desenho.create_oval(values[0], values[1], values[2], values[3], dash=(4, 2),outline=cor1,fill=cor2)
    else : #circulo
        raio = ((values[2] - values[0])**2 + (values[3]- values[1])**2)**0.5
        desenho.create_oval(values[0] - raio, values[1] - raio, values[0]+raio, values[1] + raio, dash=(4, 2),outline=cor1,fill=cor2)

def incompleta(figura):
    fig, values,cor1,cor2 = figura
    if fig == "linha" or fig == "retângulo" or fig == 'circulo' or fig == 'oval':
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "rabisco":
        return len(values) <= 1
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
  

#teoricamente você poderia digitar toda vez que colocasse um widget no frmae mas me poupe
espacaomento={'padx':2,'pady':2}


#lista serve pra guardar as figs desenhadas, o fig_nova guarda as características dessa nova figura  sendo desenhada(incluidndo tipo e coordenadas)
figs=[]
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

desenho.bind('<ButtonPress-1>', iniciar_figura_nova)
desenho.bind('<B1-Motion>', atualizar_figura_nova)
desenho.bind('<ButtonRelease-1>', incluir_figura_nova)


janela.mainloop()