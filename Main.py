from tkinter import *
from tkinter import ttk
#teoricamente você poderia digitar toda vez que colocasse um widget no frmae mas me poupe
espacaomento={'padx':5,'pady':5}

janela=Tk()
janelapropria=Frame(janela,width=1280,height=720)

texto1=ttk.Label(janelapropria,text='desenhos')
texto1.grid(column=0,row=0,**espacaomento)

desenho=Canvas(janelapropria,width=1280,height=720,bg='white')
desenho.grid(column=0,row=1,**espacaomento)


janelapropria.pack()
janela.mainloop()
