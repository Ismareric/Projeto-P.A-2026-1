from tkinter import *
from tkinter import ttk

#Código de Giovanny
def iniciar_figura_nova(event): 
    global figura_nova
    if formato.get() == 'linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y))
    elif formato.get() == 'rabisco':
        figura_nova = ("rabisco", [(event.x, event.y)])
    elif formato.get() == 'retângulo':
        figura_nova = ("retângulo", (event.x, event.y, event.x, event.y))
    elif formato.get() == 'oval':
        figura_nova = ('oval', (event.x, event.y, event.x, event.y))

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "linha":
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    elif figura_nova[0] == "retângulo":
        figura_nova = ("retângulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    elif figura_nova[0] == 'oval':
        figura_nova = ('oval', (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figs.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    desenho.delete("all")
    for fig, values in figs:
        if fig == "linha":
            desenho.create_line(values[0], values[1], values[2], values[3])
        elif fig == "rabisco":
            desenho.create_line(values)
        elif fig == "retângulo":
            desenho.create_rectangle(values[0], values[1], values[2], values[3])
        elif fig == 'oval':
            desenho.create_oval(values[0], values[1], values[2], values[3])
def desenhar_figura_nova():
    fig, values = figura_nova
    if fig == "linha":
        desenho.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == "rabisco":
        desenho.create_line(values, dash=(4, 2))
    elif fig == "retângulo":
        desenho.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == 'oval':
        desenho.create_oval(values[0], values[1], values[2], values[3], dash=(4, 2))

def incompleta(figura):
    fig, values = figura
    if fig == "linha" or fig == "retângulo":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "rabisco":
        return len(values) <= 1





#teoricamente você poderia digitar toda vez que colocasse um widget no frmae mas me poupe
espacaomento={'padx':5,'pady':5}


#lista serve pra guardar as figs desenhadas, o fig_nova guarda as características dessa nova figura  sendo desenhada(incluidndo tipo e coordenadas)
figs=[]
fig_nova=None

#criação da tela
janela=Tk()
janelapropria=Frame(janela,width=1280,height=720)

#criação dos textos na tela(obs: preciso adicionar mais)
texto1=Label(janelapropria,text='desenhos')
texto1.grid(column=0,row=0,**espacaomento,sticky=W)


#menu de opções(precisamos colocar retangulo e oval basicamente)
#obs1 eu nao sabia oque esse string var era até olhar a documentação
#obs2 eu nao sei se precisa ser exatamente atribuido à janela ou poderia ser o frame tbm
formato=StringVar(janela)
menu=ttk.OptionMenu(janelapropria,formato,'linha','linha','rabisco','retângulo','oval','círculos')
menu.grid(column=1,row=0,sticky=W,**espacaomento)


#criar o canvas
desenho=Canvas(janelapropria,width=1280,height=720,bg='white')
desenho.grid(column=0,row=1,columnspan=2,**espacaomento)

janelapropria.pack()

desenho.bind('<ButtonPress-1>', iniciar_figura_nova)
desenho.bind('<B1-Motion>', atualizar_figura_nova)
desenho.bind('<ButtonRelease-1>', incluir_figura_nova)


janela.mainloop()