from tkinter import *

def adicionar(i):
    if dysplay["text"] == '':
        dysplay["text"] = i
    else:
        dysplay["text"] = dysplay["text"] + i

def remove():
    if dysplay["text"] == '':
        pass
    else:
        palavra = dysplay["text"].split()
        palavra.pop()
        dysplay["text"] = palavra

def remove_tudo():
    if dysplay["text"] == '':
        pass
    else:
        dysplay["text"] = ''

def resultado():
    total_no_display = 0
    condicao = False
    total = dysplay['text'].split()
    for i in range(len(total)):
        if i % 2 == 0:
            total[i] = float(total[i])

    if '/' in total or 'x' in total:
        condicao = True

    if condicao:
        for j in range(total.count('x') + total.count('/')):
            for i in range(len(total)):
                if total[i] == 'x':
                    total_no_display = total[i - 1] * total[i + 1]
                    total.insert(i - 1, total_no_display)
                    del total[i]
                    del total[i]
                    del total[i]
                    break
                if total[i] == '/':
                    total_no_display = total[i - 1] / total[i + 1]
                    total.insert(i - 1, total_no_display)
                    del total[i]
                    del total[i]
                    del total[i]
                    break

    for i in range(len(total)):
        if total[i] == '+':
            if i == 1:
                total_no_display = total[i-1] + total[i+1]
            else:
                total_no_display += total[i+1]
        if total[i] == '-':
            if i == 1:
                total_no_display = total[i - 1] - total[i + 1]
            else:
                total_no_display -= total[i + 1]

    total_no_display = str(total_no_display)
    dysplay["text"] = total_no_display

janela = Tk()
janela.title('Calculadora')
janela.config(bg='black', width=177, height='220px')


nome = Label(janela, text='Calculadora', background='black', foreground='#FFFFFF')
nome.pack()
nome.place(x = 1, y = 1, width=177)
nome.config(font=16)

dysplay = Label(janela, text='', bg='#FFFFFF')
dysplay.pack()
dysplay.place(x = 10, y = 30, width=157)

botao_1 = Button(janela, text='1',height=2, command=lambda: adicionar('1'), foreground='#FFFFFF', bg='#FF4000')
botao_1.place(x=10, y = 105, width=37)

botao_2 = Button(janela, text='2',height=2, command=lambda: adicionar('2'), foreground='#FFFFFF', bg='#FF4000')
botao_2.place(x=50, y = 105, width=37)

botao_3 = Button(janela, text='3',height=2, command=lambda: adicionar('3'), foreground='#FFFFFF', bg='#FF4000')
botao_3.place(x=90, y = 105, width=37)

botao_4 = Button(janela, text='4',height=2, command=lambda: adicionar('4'), foreground='#FFFFFF', bg='#FF4000')
botao_4.place(x=10, y = 150, width=37)

botao_5 = Button(janela, text='5',height=2, command=lambda: adicionar('5'), foreground='#FFFFFF', bg='#FF4000')
botao_5.place(x=50, y = 150, width=37)

botao_6 = Button(janela, text='6',height=2, command=lambda: adicionar('6'), foreground='#FFFFFF', bg='#FF4000')
botao_6.place(x=90, y = 150, width=37)

botao_7 = Button(janela, text='7',height=2, command=lambda: adicionar('7'), foreground='#FFFFFF', bg='#FF4000')
botao_7.place(x=10, y = 195, width=37)

botao_8 = Button(janela, text='8',height=2, command=lambda: adicionar('8'), foreground='#FFFFFF', bg='#FF4000')
botao_8.place(x=50, y = 195, width=37)

botao_9 = Button(janela, text='9',height=2, command=lambda: adicionar('9'), foreground='#FFFFFF', bg='#FF4000')
botao_9.place(x=90, y = 195, width=37)

divisao = Button(janela, text='/', height=2, command=lambda: adicionar(' / '), foreground='#FFFFFF', bg='#0B4C5F')
divisao.place(x=130, y=60, width=37)

soma = Button(janela, text='+', height=2, command=lambda: adicionar(' + '), foreground='#FFFFFF', bg='#0B4C5F')
soma.place(x=130, y=105, width=37)

subtracao = Button(janela, text='-', height=2, command=lambda: adicionar(' - '), foreground='#FFFFFF', bg='#0B4C5F')
subtracao.place(x=130, y=150, width=37)

multiplicacao = Button(janela, text='x', height=2, command=lambda: adicionar(' x '), foreground='#FFFFFF', bg='#0B4C5F')
multiplicacao.place(x=130, y=195, width=37)

igual = Button(janela, text='=',height=2, command=resultado, foreground='#FFFFFF', bg='#0B4C5F')
igual.place(x=90, y=240, width=77)

ponto = Button(janela, text='.', height=2, command=lambda: adicionar('.'), foreground='#FFFFFF', bg='#FF4000')
ponto.place(x=50, y=240, width=37)

zero = Button(janela, text='0', height=2, command=lambda: adicionar('0'), foreground='#FFFFFF', bg='#FF4000')
zero.place(x=10, y=240, width=37)

remover = Button(janela, text='C', height=2, command=lambda: remove(), foreground='#FFFFFF', bg='#0B4C5F')
remover.place(x=90, y=60, width=37)

remover_tudo = Button(janela, text='CA', height=2, command=lambda: remove_tudo(), foreground='#FFFFFF', bg='#0B4C5F')
remover_tudo.place(x=50, y=60, width=37)


janela.mainloop()

