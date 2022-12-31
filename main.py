import tkinter
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"

# configurando a janela
janela= Tk()
janela.title('')
janela.geometry('360x300')
janela.config(bg=fundo)

#dividindo a janela

frame_cima = Frame(janela, width=360, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)

frame_baixo = Frame(janela, width=360, height=200, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#configurando o frame cima
#pontuacao do usuario
app_1 = Label(frame_cima, text="Voce", height=1, anchor='center', font=('Ivy 15 bold'), bg=co1, fg=co0)
app_1.place(x=30, y=70)

app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 15 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)

app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=70, y=15)

#os dois pontos
app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co0)
app_.place(x=170, y=20)

#pontuacao do PC
app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=250, y=15)

app_2 = Label(frame_cima, text="PC", height=1, anchor='center', font=('Ivy 15 bold'), bg=co1, fg=co0)
app_2.place(x=300, y=70)

app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 15 bold'), bg=co0, fg=co0)
app_2_linha.place(x=355, y=0)

app_linha = Label(frame_cima, text="", width=255,anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)


janela.mainloop()