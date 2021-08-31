from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dado import *
from Model import regras_jogo
from Controller import event_handler
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog

global coord_casas, coord_retasfinais, coord_peoes, lista_casas, qtd_peoes_base, cb
global botao_novojogo, botao_carregar, botao_salvar, botao_lancar, botao_confirmar

lista = ['red', 'green', 'yellow', 'blue']


def desenha_cor(cnv, vez):
    cnv.create_rectangle(670, 300, 720, 350, fill=lista[vez], outline=lista[vez])


def desenha_tabuleiro(cnv):
    cnv.delete("all")
    casa_inicial(cnv)
    desenha_casas(cnv)
    casas_finais(cnv)
    seta_casa_de_saida(cnv)
    desenha_peao(cnv)
    desenha_cor(cnv, regras_jogo.vez)


def casa_inicial(cnv):
    retangulo_cinza = cnv.create_rectangle(600, 900, 800, -10, fill='grey', outline='grey')
    casa_1 = cnv.create_rectangle(0, 0, 240, 240, fill='red', outline='red')
    casa_2 = cnv.create_rectangle(360, 0, 600, 240, fill='green', outline='green')
    casa_3 = cnv.create_rectangle(360, 360, 600, 600, fill='yellow', outline='yellow')
    casa_4 = cnv.create_rectangle(0, 360, 240, 600, fill='blue', outline='blue')

    # Bases (círculos brancos que abrigam os peoes)
    cnv.create_oval(10, 60, 40, 90, fill='white', outline='black')
    cnv.create_oval(200, 60, 230, 90, fill='white', outline='black')
    cnv.create_oval(10, 180, 40, 210, fill='white', outline='black')
    cnv.create_oval(200, 180, 230, 210, fill='white', outline='black')

    cnv.create_oval(400, 50, 430, 80, fill='white', outline='black')
    cnv.create_oval(550, 50, 580, 80, fill='white', outline='black')
    cnv.create_oval(400, 180, 430, 210, fill='white', outline='black')
    cnv.create_oval(550, 180, 580, 210, fill='white', outline='black')

    cnv.create_oval(400, 400, 430, 430, fill='white', outline='black')
    cnv.create_oval(550, 400, 580, 430, fill='white', outline='black')
    cnv.create_oval(550, 560, 580, 590, fill='white', outline='black')
    cnv.create_oval(400, 560, 430, 590, fill='white', outline='black')

    cnv.create_oval(10, 400, 40, 430, fill='white', outline='black')
    cnv.create_oval(200, 400, 230, 430, fill='white', outline='black')
    cnv.create_oval(10, 560, 40, 590, fill='white', outline='black')
    cnv.create_oval(200, 560, 230, 590, fill='white', outline='black')


def get_coord_casas():
    global coord_casas, coord_retasfinais, coord_peoes
    return coord_casas


def get_coord_retasfinais():
    global coord_casas, coord_retasfinais, coord_peoes
    return coord_retasfinais


def get_coord_peoes():
    global coord_casas, coord_retasfinais, coord_peoes
    return coord_peoes


def desenha_peao(cnv):
    global coord_casas, coord_retasfinais, coord_peoes, lista_casas, qtd_peoes_base

    coord_peoes = list()
    lista_casas = regras_jogo.get_casas()
    qtd_peoes_base = regras_jogo.get_qtd_peoes_base()

    '''Vermelho'''

    peoes_vermelhos = list()
    peoes_vermelhos.append([14, 64, 36, 86])
    peoes_vermelhos.append([204, 64, 226, 86])
    peoes_vermelhos.append([14, 184, 36, 206])
    peoes_vermelhos.append([204, 184, 226, 206])

    coord_peoes.append(peoes_vermelhos)

    '''Verde'''

    peoes_verdes = list()
    peoes_verdes.append([404, 54, 426, 76])
    peoes_verdes.append([554, 54, 576, 76])
    peoes_verdes.append([404, 184, 426, 206])
    peoes_verdes.append([554, 184, 576, 206])

    coord_peoes.append(peoes_verdes)

    '''Amarelo'''
    peoes_amarelos = list()
    peoes_amarelos.append([404, 404, 426, 426])
    peoes_amarelos.append([554, 404, 576, 426])
    peoes_amarelos.append([554, 564, 576, 586])
    peoes_amarelos.append([404, 564, 426, 586])

    coord_peoes.append(peoes_amarelos)

    '''Azul'''
    peoes_azuis = list()
    peoes_azuis.append([14, 404, 36, 426])
    peoes_azuis.append([204, 404, 226, 426])
    peoes_azuis.append([14, 564, 36, 586])
    peoes_azuis.append([204, 564, 226, 586])

    coord_peoes.append(peoes_azuis)

    for i in range(4):
        peoes_restantes = qtd_peoes_base[i]
        for j in range(4):

            if peoes_restantes <= 0:
                break

            x1 = coord_peoes[i][j][0]
            y1 = coord_peoes[i][j][1]
            x2 = coord_peoes[i][j][2]
            y2 = coord_peoes[i][j][3]

            if i == 0:
                cor = 'red'
            elif i == 1:
                cor = 'green'
            elif i == 2:
                cor = 'yellow'
            else:
                cor = 'blue'

            cnv.create_oval(x1, y1, x2, y2, fill=cor, outline='black')
            peoes_restantes -= 1

    # Desenha peões no caminho branco
    for i in range(52):
        if len(lista_casas[i]['peoes']) == 1:
            cor_num = lista_casas[i]['peoes'][0]

            if cor_num == 0:
                cor = 'red'
            elif cor_num == 1:
                cor = 'green'
            elif cor_num == 2:
                cor = 'yellow'
            else:
                cor = 'blue'

            x1 = coord_casas[i][0]
            y1 = coord_casas[i][1]
            x2 = coord_casas[i][2]
            y2 = coord_casas[i][3]
            cnv.create_oval(x1, y1, x2, y2, fill=cor, outline='black')

        if len(lista_casas[i]['peoes']) == 2:
            # Aqui é o caso em que temos uma barreira (ou dois peões qualquer) na casa

            x1 = coord_casas[i][0]
            y1 = coord_casas[i][1]
            x2 = coord_casas[i][2]
            y2 = coord_casas[i][3]
            print('coord. da barreira:', x1, y1, x2, y2)

            first = lista_casas[i]['peoes'][0]
            second = lista_casas[i]['peoes'][1]
            if first == second:
                cnv.create_oval(x1 + 8, y1 + 8, x2 - 8, y2 - 8, fill=lista[first], outline=lista[first])
                cnv.create_oval(x1, y1, x2, y2, outline=lista[first])

            else:
                cnv.create_oval(x1, y1, x2, y2, fill=lista[second], outline=lista[second])
                cnv.create_oval(x1 + 8, y1 + 8, x2 - 8, y2 - 8, fill=lista[first], outline=lista[first])

    # Mostra peoes nas retas finais
    for i in range(4):
        for j in range(6):

            if i == 0:
                cor_num = 'red'
            elif i == 1:
                cor_num = 'green'
            elif i == 2:
                cor_num = 'yellow'
            else:
                cor_num = 'blue'

            x1 = coord_retasfinais[i][j][0]
            y1 = coord_retasfinais[i][j][1]
            x2 = coord_retasfinais[i][j][2]
            y2 = coord_retasfinais[i][j][3]

            retas_finais = regras_jogo.get_retas_finais()

            if len(retas_finais[i][j]['peoes']) == 1:
                cnv.create_oval(x1, y1, x2, y2, fill=cor_num, outline='black')


def desenha_casas(cnv):
    global coord_casas, coord_retasfinais, coord_peoes

    coord_casas = list()
    coord_retasfinais = list()

    coord_casas.append([40, 240, 80, 280])
    coord_casas.append([80, 240, 120, 280])
    coord_casas.append([120, 240, 160, 280])
    coord_casas.append([160, 240, 200, 280])
    coord_casas.append([200, 240, 240, 280])
    coord_casas.append([240, 200, 280, 240])
    coord_casas.append([240, 160, 280, 200])
    coord_casas.append([240, 120, 280, 160])
    coord_casas.append([240, 80, 280, 120])
    coord_casas.append([240, 40, 280, 80])
    coord_casas.append([240, 0, 280, 40])
    coord_casas.append([280, 0, 320, 40])
    coord_casas.append([320, 0, 360, 40])
    coord_casas.append([320, 40, 360, 80])
    coord_casas.append([320, 80, 360, 120])
    coord_casas.append([320, 120, 360, 160])
    coord_casas.append([320, 160, 360, 200])
    coord_casas.append([320, 200, 360, 240])
    coord_casas.append([360, 240, 400, 280])
    coord_casas.append([400, 240, 440, 280])
    coord_casas.append([440, 240, 480, 280])
    coord_casas.append([480, 240, 520, 280])
    coord_casas.append([520, 240, 560, 280])
    coord_casas.append([560, 240, 600, 280])
    coord_casas.append([560, 280, 600, 320])
    coord_casas.append([560, 320, 600, 360])
    coord_casas.append([520, 320, 560, 360])
    coord_casas.append([480, 320, 520, 360])
    coord_casas.append([440, 320, 480, 360])
    coord_casas.append([400, 320, 440, 360])
    coord_casas.append([360, 320, 400, 360])
    coord_casas.append([320, 360, 360, 400])
    coord_casas.append([320, 400, 360, 440])
    coord_casas.append([320, 440, 360, 480])
    coord_casas.append([320, 480, 360, 520])
    coord_casas.append([320, 520, 360, 560])
    coord_casas.append([320, 560, 360, 600])
    coord_casas.append([280, 560, 320, 600])
    coord_casas.append([240, 560, 280, 600])
    coord_casas.append([240, 520, 280, 560])
    coord_casas.append([240, 480, 280, 520])
    coord_casas.append([240, 440, 280, 480])
    coord_casas.append([240, 400, 280, 440])
    coord_casas.append([240, 360, 280, 400])
    coord_casas.append([200, 320, 240, 360])
    coord_casas.append([160, 320, 200, 360])
    coord_casas.append([120, 320, 160, 360])
    coord_casas.append([80, 320, 120, 360])
    coord_casas.append([40, 320, 80, 360])
    coord_casas.append([0, 320, 40, 360])
    coord_casas.append([0, 280, 40, 320])
    coord_casas.append([0, 240, 40, 280])

    for i in range(52):

        if i == 0:
            cor_casa = 'red'
        elif i == 13:
            cor_casa = 'green'
        elif i == 26:
            cor_casa = 'yellow'
        elif i == 39:
            cor_casa = 'blue'
        elif i == 9 or i == 22 or i == 35 or i == 48:
            cor_casa = 'black'
        else:
            cor_casa = 'white'

        x1 = coord_casas[i][0]
        y1 = coord_casas[i][1]
        x2 = coord_casas[i][2]
        y2 = coord_casas[i][3]

        cnv.create_rectangle(x1, y1, x2, y2, fill=cor_casa, outline='black')

    '''Reta final vermelha na ordem até a casa final'''
    retafinal1 = list()
    retafinal1.append([40, 280, 80, 320])
    retafinal1.append([80, 280, 120, 320])
    retafinal1.append([120, 280, 160, 320])
    retafinal1.append([160, 280, 200, 320])
    retafinal1.append([200, 280, 240, 320])
    retafinal1.append([240, 280, 280, 320])

    coord_retasfinais.append(retafinal1)

    '''Reta Final Verde na ordem até a casa final'''
    retafinal2 = list()
    retafinal2.append([280, 40, 320, 80])
    retafinal2.append([280, 80, 320, 120])
    retafinal2.append([280, 120, 320, 160])
    retafinal2.append([280, 160, 320, 200])
    retafinal2.append([280, 200, 320, 240])
    retafinal2.append([280, 240, 320, 280])

    coord_retasfinais.append(retafinal2)

    '''Reta Final Amarela na ordem até a casa final'''
    retafinal3 = list()
    retafinal3.append([520, 280, 560, 320])
    retafinal3.append([480, 280, 520, 320])
    retafinal3.append([440, 280, 480, 320])
    retafinal3.append([400, 280, 440, 320])
    retafinal3.append([360, 280, 400, 320])
    retafinal3.append([320, 280, 360, 320])

    coord_retasfinais.append(retafinal3)

    '''Reta Final Azul na ordem até a casa final'''
    retafinal4 = list()
    retafinal4.append([280, 520, 320, 560])
    retafinal4.append([280, 480, 320, 520])
    retafinal4.append([280, 440, 320, 480])
    retafinal4.append([280, 400, 320, 440])
    retafinal4.append([280, 360, 320, 400])
    retafinal4.append([280, 320, 320, 360])

    coord_retasfinais.append(retafinal4)

    for i in range(4):
        for j in range(6):

            if i == 0:
                cor_casa = 'red'
            elif i == 1:
                cor_casa = 'green'
            elif i == 2:
                cor_casa = 'yellow'
            else:
                cor_casa = 'blue'

            x1 = coord_retasfinais[i][j][0]
            y1 = coord_retasfinais[i][j][1]
            x2 = coord_retasfinais[i][j][2]
            y2 = coord_retasfinais[i][j][3]

            cnv.create_rectangle(x1, y1, x2, y2, fill=cor_casa, outline='black')


def casas_finais(cnv):
    '''Casas finais'''
    cnv.create_polygon((300, 300), (240, 360), (240, 240), fill='red', outline='black')
    cnv.create_polygon((300, 300), (240, 360), (360, 360), fill='blue', outline='black')
    cnv.create_polygon((300, 300), (360, 360), (360, 240), fill='yellow', outline='black')
    cnv.create_polygon((300, 300), (240, 240), (360, 240), fill='green', outline='black')


def seta_casa_de_saida(cnv):
    '''Setas das Casas de Saídas 368 '''
    cnv.create_polygon((50, 270), (50, 250), (75, 260), fill='white')
    cnv.create_polygon((350, 50), (330, 50), (340, 75), fill='white')
    cnv.create_polygon((550, 350), (550, 330), (525, 340), fill='white')
    cnv.create_polygon((270, 550), (250, 550), (260, 525), fill='white')


def dado_aparece(cnv, dado):
    '''Fazer Dado do Número Sorteado Aparecer'''
    global img, dado1
    desenha_vez = regras_jogo.get_vez()
    print("Vez:", desenha_vez)
    desenha_cor(cnv, desenha_vez)
    if dado == 1:
        img = PhotoImage(file='dado/dado_1.png')
        i1 = cnv.create_image(712, 325, image=img, anchor=E)
    if dado == 2:
        img = PhotoImage(file='dado/dado_2.png')
        i2 = cnv.create_image(712, 325, image=img, anchor=E)
    if dado == 3:
        img = PhotoImage(file='dado/dado_3.png')
        i3 = cnv.create_image(712, 325, image=img, anchor=E)
    if dado == 4:
        img = PhotoImage(file='dado/dado_4.png')
        i4 = cnv.create_image(712, 325, image=img, anchor=E)
    if dado == 5:
        img = PhotoImage(file='dado/dado_5.png')
        i5 = cnv.create_image(712, 325, image=img, anchor=E)
    if dado == 6:
        img = PhotoImage(file='dado/dado_6.png')
        i6 = cnv.create_image(712, 325, image=img, anchor=E)


def desenha_botoes(root, cnv):
    global botao_novojogo, botao_carregar, botao_salvar, botao_lancar
    botao_novojogo = Button(root, text="Novo Jogo", width=13, height=1, font=("Arial", 15),
                            command=lambda: event_handler.novo_jogo_pressed(cnv))
    botao_carregar = Button(root, text="Carregar Jogo", width=13, height=1, font=("Arial", 15),
                            command=lambda: event_handler.carrega_jogo_pressed(cnv))
    botao_salvar = Button(root, text="Salvar", width=13, height=1, font=("Arial", 15),
                          command=lambda: regras_jogo.salva_lista())
    botao_lancar = Button(root, text="Lançar Dado", width=13, height=1, font=("Arial", 15),
                          command=lambda: event_handler.lancar_dado_pressed(cnv))
    l1 = Label(root, text="À Jogar: ")
    l1.place(x=670, y=260)
    botao_novojogo.place(x=625, y=20)
    botao_carregar.place(x=625, y=80)
    botao_salvar.place(x=625, y=140)
    botao_lancar.place(x=625, y=200)


def combobox(root, cnv):
    global cb, botao_confirmar
    l1 = Label(root, text="Escoha o Valor do Dado")
    l1.place(x=630, y=370)
    valor_dado = ["1", "2", "3", "4", "5", "6"]
    cb = ttk.Combobox(root, values=valor_dado, width=10)
    cb.place(x=650, y=400)
    cb.current(0)
    botao_confirmar = Button(root, text="Confirmar",
                             command=lambda: event_handler.combobox_pressed(cnv, (ord(cb.get()) - 48)))
    botao_confirmar.place(x=660, y=430)


def desativar_botoes():
    global botao_novojogo, botao_carregar, botao_salvar, botao_lancar, botao_confirmar

    botao_salvar['state'] = DISABLED
    botao_confirmar['state'] = DISABLED
    botao_lancar['state'] = DISABLED


def ativar_botoes():
    global botao_novojogo, botao_carregar, botao_salvar, botao_lancar, botao_confirmar

    botao_salvar['state'] = NORMAL
    botao_confirmar['state'] = NORMAL
    botao_lancar['state'] = NORMAL


def vencedor():
    mensagem = regras_jogo.fim_de_jogo()
    valor1 = mensagem[0][0]
    valor2 = mensagem[1][0]
    valor3 = mensagem[1][0]
    valor4 = mensagem[3][0]

    if (mensagem[0][1] == 0):
        vencedor = "Vermelho"
    if (mensagem[0][1] == 1):
        vencedor = "Verde"
    if (mensagem[0][1] == 2):
        vencedor = "Amarelo"
    if (mensagem[0][1] == 3):
        vencedor = "Azul"
    if (mensagem[1][1] == 0):
        vice = "Vermelho"
    if (mensagem[1][1] == 1):
        vice = "Verde"
    if (mensagem[1][1] == 2):
        vice = "Amarelo"
    if (mensagem[1][1] == 3):
        vice = "Azul"
    if (mensagem[2][1] == 0):
        terceiro = "Vermelho"
    if (mensagem[2][1] == 1):
        terceiro = "Verde"
    if (mensagem[2][1] == 2):
        terceiro = "Amarelo"
    if (mensagem[2][1] == 3):
        terceiro = "Azul"
    if (mensagem[3][1] == 0):
        quarto = "Vermelho"
    if (mensagem[3][1] == 1):
        quarto = "Verde"
    if (mensagem[3][1] == 2):
        quarto = "Amarelo"
    if (mensagem[3][1] == 3):
        quarto = "Azul"

def abre_arquivo():
    input = filedialog.askopenfile(initialdir=".", title="Abrir arquivo", filetypes=(("text files", "*.txt"),("all files", "*.*")))
    regras_jogo.carrega_jogo(input)
