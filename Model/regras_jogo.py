from enum import Enum
import random

"""
from tkinter import *
from tkinter import messagebox
import sys
import os
import random
import tkinter.messagebox
"""


class Cor(Enum):
    vermelho = 0
    verde = 1
    amarelo = 2
    azul = 3


global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
global mov_consecutivos, jogo_acontecendo, tem_que_escolher_peao, casas_finais, capturou


def novo_jogo():  # cria tudo necessário para o começo de uma partida
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo, tem_que_escolher_peao, casas_finais, capturou

    jogo_acontecendo = True
    mov_consecutivos = 0
    tem_que_escolher_peao = False
    capturou = False

    lista_peoes = [[-1, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
    peoes_iniciais = [4, 4, 4, 4]
    casas_finais = [0, 0, 0, 0]

    pontuacao_jogadores = [0, 0, 0, 0]

    vez = 0
    print("Começou! Vez do vermelho!")

    lista_casas = list()
    retasfinais = list()

    ultimo_movimentado = dict()

    for i in range(52):  # inicializa cada casa (menos as finais de cada cor)
        casa = dict()
        casa['numero'] = i
        casa['peoes'] = list()  # lista vazia de peões ocupando aquela casa
        if i == 0 or i == 13 or i == 26 or i == 39:
            casa['tipo'] = 'saida'
        elif i == 9 or i == 22 or i == 35 or i == 48:
            casa['tipo'] = 'abrigo'
        else:
            casa['tipo'] = 'comum'
        lista_casas.append(casa.copy())

    # for item in lista_casas:
    #   print(item)

    for i in range(4):
        retafinal = list()

        for _ in range(6):
            casa = dict()
            casa['peoes'] = list()
            retafinal.append(casa.copy())

        retasfinais.append(retafinal.copy())

        # print(retasfinais[i], i, Cor(i).name)


def get_casas():
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo

    return lista_casas


def get_qtd_peoes_base():
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo

    return peoes_iniciais


def get_vez():
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo

    return vez


def get_retas_finais():
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo

    return retasfinais


def passar_a_vez():
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado

    if vez >= 3:
        vez = 0
    else:
        vez += 1


def posicionar_na_saida(peao):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado

    if not retirar_do_inicio(peao):
        return False
    else:

        lista_casas[13 * peao]['peoes'].append(peao)
        # OBS: Os números das casas de saída são múltiplos de 13

        print('após inserção:')
        print(lista_casas[13 * peao])
        return True


def posicionar(num_casa, cor_peao):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado

    peao_na_casa = int()

    if len(lista_casas[num_casa]['peoes']) > 0:
        peao_na_casa = lista_casas[num_casa]['peoes'][0]
    else:
        peao_na_casa = -1

    if peao_na_casa != -1 and peao_na_casa != cor_peao and lista_casas[num_casa]['tipo'] != 'abrigo':
        if num_casa != (peao_na_casa * 13):
            captura(num_casa, peao_na_casa)

    lista_casas[num_casa]['peoes'].append(cor_peao)


def movimentar(casa_origem, cor_peao, movimentos):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado

    if cor_peao in lista_casas[casa_origem]['peoes']:
        lista_casas[casa_origem]['peoes'].remove(cor_peao)
    else:
        print('ERRO, não existe peão da cor especificada na casa especificada!')
        return

    casas_percorridas = 0

    while movimentos > 0:

        # REGRA DO 6: No caso de tirar 6 no dado, salvar a ultima posição e a cor do peão movimentado
        # Caso saia 6 pela terceira vez, pegar esse peão e trazê-lo de volta a casa inicial

        print(casa_origem)

        if deve_ir_retafinal(casa_origem, cor_peao):
            print('Peão', cor_peao, 'Deve ir à sua reta final!')
            ir_para_retafinal(cor_peao, movimentos - 1)
            break
        else:
            ultimo_movimentado['reta_final'] = False

        if existe_barreira(casa_origem):
            break

        if casa_origem == 51:
            casa_origem = 0
        else:
            casa_origem += 1

        movimentos -= 1
        casas_percorridas += 1
        pontuacao_jogadores[cor_peao] += 1

        ultimo_movimentado['cor'] = cor_peao
        ultimo_movimentado['casa'] = casa_origem

    if not ultimo_movimentado['reta_final']:
        posicionar(casa_origem, cor_peao)


def ir_para_retafinal(cor_peao, qtd_casas):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo, tem_que_escolher_peao, casas_finais

    retasfinais[cor_peao][qtd_casas]['peoes'].append(cor_peao)

    ultimo_movimentado['cor'] = cor_peao
    ultimo_movimentado['casa'] = qtd_casas
    ultimo_movimentado['reta_final'] = True

    pontuacao_jogadores[cor_peao] += qtd_casas + 1

    if len(retasfinais[cor_peao][5]['peoes']) >= 4:  # verifica se a ultima casa está com os 4 peoes
        fim_de_jogo()


def ir_para_casa_final(cor_peao, pos, num_casas):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo, tem_que_escolher_peao, casas_finais

    if len(retasfinais[cor_peao][pos]['peoes']) == 0:
        print("não há peão nessa casa final!")
        return False

    if pos != (5 - num_casas):
        print("não tirou a quantidade de casas necessárias para ir ao final!")
        return False
    else:
        retasfinais[cor_peao][pos]['peoes'].pop(0)
        retasfinais[cor_peao][5]['peoes'].append(cor_peao)
        pontuacao_jogadores[cor_peao] += num_casas
        casas_finais[vez] += 1

        print('Peões nas casas finais:', casas_finais)

        if casas_finais[vez] >= 4:
            fim_de_jogo()

        return True


def fim_de_jogo():
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo, tem_que_escolher_peao

    jogo_acontecendo = False

    podio = sorted(((value, index) for index, value in enumerate(pontuacao_jogadores)), reverse=True)
    print(podio)
    for i in range(4):
        if i == 0:
            print('O vencedor é o jogador', Cor(podio[i][1]).name, 'com a pontuação', podio[i][0], '! Parabéns!')
        elif i == 1:
            print('Em segundo lugar,', Cor(podio[i][1]).name, ', com a pontuação', podio[i][0], '!')
        elif i == 2:
            print('Em terceiro lugar,', Cor(podio[i][1]).name, ', com a pontuação', podio[i][0], '!')
        else:
            print('Em quarto lugar,', Cor(podio[i][1]).name, ', com a pontuação', podio[i][0],
                  '! Mais sorte da próxima vez!')

    return podio


def existe_barreira(posicao):
    if posicao == 51:
        if len(lista_casas[0]['peoes']) >= 2:
            print("Uma barreira ou um abrigo lotado foi encontrado na casa adjacente!")
            return True

    elif len(lista_casas[posicao + 1]['peoes']) >= 2:
        print("Uma barreira ou um abrigo lotado foi encontrado na casa adjacente!")
        return True

    return False


def retorna_barreira(posicao):
    if len(lista_casas[0]['peoes']) >= 2:
        print("Uma barreira ou um abrigo lotado foi encontrado na casa adjacente!")
        if lista_casas[posicao]['tipo'] == 'abrigo':
            return 1
        else:
            return -1
    return 0


def deve_ir_retafinal(posicao, cor_peao):
    if cor_peao == 0:
        if posicao == 50:
            return True
    elif cor_peao == 1:
        if posicao == 11:
            return True
    elif cor_peao == 2:
        if posicao == 24:
            return True
    elif cor_peao == 3:
        if posicao == 37:
            return True

    return False


def abrigo(posicao, peao):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo, tem_que_escolher_peao

    if len(lista_casas[posicao]['peoes']) < 2:
        lista_casas[posicao]['peoes'].append(peao)
    else:
        print("Abrigo so para 2 pecas diferentes")
        exit(0)


def voltar_ao_inicio(peao, casa):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo, tem_que_escolher_peao, casas_finais, capturou

    if peoes_iniciais[peao] == 4:
        print("ERRO: Base cheia")
        return
    else:
        b = lista_casas[casa]['peoes'].pop(0)
        print('Capturou:', b)
        peoes_iniciais[peao] = peoes_iniciais[peao] + 1

        while casa != peao * 13:  # Decrementa a pontuação do jogador
            print(casa)
            if casa == 0:
                casa = 51
            else:
                casa -= 1
            pontuacao_jogadores[peao] -= 1

        print(pontuacao_jogadores)
        capturou = True


def retirar_do_inicio(peao):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo, tem_que_escolher_peao

    if peoes_iniciais[peao] <= 0:
        print("Casas estão vazias")
        return False
    elif len(lista_casas[13 * peao]['peoes']) >= 2:
        print('Casa de saída', 13 * peao, 'está cheia!')
        return False
    elif len(lista_casas[13 * peao]['peoes']) == 1:
        peao_ocupante = lista_casas[13 * peao]['peoes'][0]
        if peao_ocupante == peao:
            print('Já existe um peão dessa cor na casa de saída', 13 * peao)
            return False
        else:
            peoes_iniciais[peao] = peoes_iniciais[peao] - 1
            captura(13 * peao, peao_ocupante)
            return True

    else:
        peoes_iniciais[peao] = peoes_iniciais[peao] - 1
        return True


def captura(posicao, cor):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais

    if len(lista_casas[posicao]['peoes']) == 0:
        print("Casa vazia")
        return
    elif lista_casas[posicao]['peoes'][0] != cor:
        print("Não existe peão da cor especificada a ser capturado nessa casa")
        return
    else:
        voltar_ao_inicio(cor, posicao)


def rolardados():
    num = random.randint(1, 6)
    return num


def jogada(dado):
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo, tem_que_escolher_peao, capturou

    if regra_5(dado, vez):
        print('Regra do 5! Peão sai da base')
        if not posicionar_na_saida(vez):
            print('...só q não')
        else:
            mov_consecutivos = 0
            if capturou:
                tem_que_escolher_peao = True
            else:
                passar_a_vez()
                tem_que_escolher_peao = False
            return dado

    if peoes_iniciais[vez] + casas_finais[vez] <= 3:
        if dado == 6:  # Regra do 6
            print("Regra do 6!!!")
            if mov_consecutivos < 2:
                print("Jogador", vez, " escolha um peão para movimentar e depois role o dado novamente!")
                mov_consecutivos += 1
                tem_que_escolher_peao = True
            else:
                print("Peao do jogador", vez, "volta ao início! TROLADO")
                voltar_ultimo_movimentado()
                mov_consecutivos = 0
                passar_a_vez()
                tem_que_escolher_peao = False

        else:
            print("Jogador", vez, "escolha um peão para movimentar")
            mov_consecutivos = 0
            tem_que_escolher_peao = True
    else:
        print("Jogador", vez, "não tem peças no tabuleiro! Passa a vez!")
        tem_que_escolher_peao = False
        mov_consecutivos = 0
        passar_a_vez()

    print(pontuacao_jogadores)
    return dado


def voltar_ultimo_movimentado():
    global vez, lista_casas, retasfinais, bases, pontuacao_jogadores, lista_peoes, peoes_iniciais, ultimo_movimentado
    global mov_consecutivos, jogo_acontecendo

    if ultimo_movimentado['reta_final']:
        print("Peão em reta final não pode voltar à sua base")
        return

    ult_cor = ultimo_movimentado['cor']
    ult_casa = ultimo_movimentado['casa']

    voltar_ao_inicio(ult_cor, ult_casa)


def salva_lista():
    global lista_casas, retasfinais
    arquivo = open("lista.txt", "w")
    for i in range(52):
        tamanho = (len(lista_casas[i]['peoes']))
        if tamanho != 0:
            for x in range(tamanho):
                arquivo.write("lista_casa %d %d\n" % (i, lista_casas[i]['peoes'][x]))
    for i in range(4):  # Sao as retas finais dos 4 peoes
        for j in range(6):  # porque essas retas finais tem 6 casas
            tamanho = (
                len(retasfinais[i][j]['peoes']))  # vendo cada casa da reta final,i e a cor e j sao as casas dessa cor
            # print("Tam%d peao %d\n"%(tamanho,retasfinais[0][2]['peoes'][0]))
            if tamanho != 0:
                for x in range(tamanho):
                    arquivo.write("retafinal %d %d \n" % (i, j))

    arquivo.close()


def carrega_jogo(linha):
    # novo_jogo()
    linha=open('lista', "r")
    for i in linha:
        elemento = i.split()  # o split le 1 linha, dando a opcao de cessar seus elementos
        lista = elemento[0]  # Ve se e a lista_casas ou casa finais
        tamanho = len(elemento)  # Quantos elementos tem naquela linha
        pos = int(elemento[1])
        peca_1 = int(elemento[2])
        if lista == 'lista_casa':
            retirar_do_inicio(peca_1)
            posicionar(pos, peca_1)
        else:
            retirar_do_inicio(peca_1)
            ir_para_retafinal(pos, peca_1)
    print(peoes_iniciais)

    linha.close()


def regra_5(dado, vez):
    if dado != 5:
        return False
    else:
        if peoes_iniciais[vez] == 0:
            print("Todos os peoes ja foram iniciados, escolha 1 peao para andar 5 casas")
            return False

        else:
            return True


# ---------------------------TESTES--------------------------------------------

"""
novo_jogo()

retirar_do_inicio(0)
retirar_do_inicio(2)
posicionar_na_saida(0)
posicionar_na_saida(2)

for i in range(10):
    passar_a_vez()

movimentar(0, 0, 5)

posicionar(10, 3)

movimentar(10, 3, 2)

movimentar(5, 0, 7)

posicionar(12, 0)

movimentar(20, lista_peoes[0][1], 5)

posicionar_na_saida(1)

posicionar(5, 0)
posicionar(5, 0)

movimentar(13, 1, 51)

movimentar(12, 0, 40)

for item in lista_casas:
    print(item)

for retafinal in retasfinais:
    print(retafinal)
"""


