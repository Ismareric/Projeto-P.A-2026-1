from tkinter import *
from tkinter import ttk
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
menu=ttk.OptionMenu(janelapropria,formato,'linha','linha','rabisco','retângulo','ovais','círculos')
menu.grid(column=1,row=0,sticky=W,**espacaomento)
#criar o canvas
desenho=Canvas(janelapropria,width=1280,height=720,bg='white')
desenho.grid(column=0,row=1,columnspan=2,**espacaomento)


janelapropria.pack()
janela.mainloop()
