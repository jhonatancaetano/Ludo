from View import teste_tab
from Model import regras_jogo

global casas_a_movimentar


def click(event):
    global casas_a_movimentar

    print('Coord. X:', event.x)
    print('Coord. Y:', event.y)

    vez = regras_jogo.get_vez()
    coord_casas = teste_tab.get_coord_casas()
    casas = regras_jogo.get_casas()

    # Verifica se o clique foi dado em uma casa "normal"
    for i in range(len(coord_casas)):

        casa = coord_casas[i]

        if casa[0] < event.x < casa[2] and casa[1] < event.y < casa[3]:
            print('clique aconteceu na casa', i)

            if regras_jogo.tem_que_escolher_peao and len(casas[i]['peoes']) >= 1:
                for peao in casas[i]['peoes']:
                    if peao == vez:

                        if casas_a_movimentar == -1:  # Sinaliza um movimento extra
                            regras_jogo.movimentar(i, peao, 6)
                            regras_jogo.capturou = False
                            regras_jogo.mov_consecutivos = 0

                        regras_jogo.movimentar(i, peao, casas_a_movimentar)

                        if regras_jogo.capturou:
                            print("Capturou! Jogador", vez, "escolha um peão para movimentar 6 casas!")
                            casas_a_movimentar = -1  # Sinaliza um movimento extra
                            break

                        if regras_jogo.mov_consecutivos == 0:
                            regras_jogo.passar_a_vez()
                            vez = regras_jogo.get_vez()
                            print('vez do', vez, '!')
                            regras_jogo.tem_que_escolher_peao = False

                    teste_tab.ativar_botoes()
            break

    coord_peoes = teste_tab.get_coord_peoes()

    # Verifica se o clique foi dado em um peão na base
    for i in range(4):
        for j in range(4):

            peao = coord_peoes[i][j]

            if peao[0] < event.x < peao[2] and peao[1] < event.y < peao[3]:
                print('clique aconteceu num peao da cor', i)
                break

    coord_retasfinais = teste_tab.get_coord_retasfinais()

    # Verifica se o clique foi dado em uma casa final
    for i in range(4):
        for j in range(6):

            casa = coord_retasfinais[i][j]

            if casa[0] < event.x < casa[2] and casa[1] < event.y < casa[3]:
                print('clique aconteceu na casa final', j, 'da cor', i)
                if i == vez:
                    if regras_jogo.ir_para_casa_final(i, j, casas_a_movimentar):
                        regras_jogo.passar_a_vez()
                        vez = regras_jogo.get_vez()
                        print('vez do', vez, '!')
                        regras_jogo.tem_que_escolher_peao = False
                    else:
                        print('Escolha outro peão para movimentar')
                teste_tab.ativar_botoes()
                break

    teste_tab.desenha_tabuleiro(event.widget)

    if not regras_jogo.jogo_acontecendo:
        teste_tab.vencedor()

    '''
    global c, cx, cy

    c = c+1
    cx  =  root.winfo_pointerx() -  root.winfo_rootx()   # Esta fórmula retorna as coordenadas x, y do ponteiro do mouse em relação ao quadro.
    cy  =  root.winfo_pointery() -  root.winfo_rooty()

    print ( "Clique em:" , cx , cy )
    '''


def novo_jogo_pressed(cnv):
    global casas_a_movimentar

    regras_jogo.novo_jogo()
    teste_tab.desenha_tabuleiro(cnv)


def lancar_dado_pressed(cnv):
    global casas_a_movimentar

    casas_a_movimentar = regras_jogo.rolardados()
    regras_jogo.jogada(casas_a_movimentar)
    print(casas_a_movimentar)
    print(regras_jogo.mov_consecutivos)
    vez = regras_jogo.get_vez()
    print('vez do', vez, '!')
    teste_tab.desenha_tabuleiro(cnv)
    teste_tab.dado_aparece(cnv, casas_a_movimentar)
    if regras_jogo.tem_que_escolher_peao:
        teste_tab.desativar_botoes()
    else:
        teste_tab.ativar_botoes()


def carrega_jogo_pressed(cnv):
    regras_jogo.novo_jogo()
    teste_tab.abre_arquivo()
    teste_tab.desenha_tabuleiro(cnv)

    
def combobox_pressed(cnv, num_casas):
    global casas_a_movimentar

    casas_a_movimentar = num_casas
    regras_jogo.jogada(casas_a_movimentar)
    print(casas_a_movimentar)
    print(regras_jogo.mov_consecutivos)
    vez = regras_jogo.get_vez()
    print('vez do', vez, '!')
    teste_tab.desenha_tabuleiro(cnv)
    teste_tab.dado_aparece(cnv, casas_a_movimentar)
    if regras_jogo.tem_que_escolher_peao:
        teste_tab.desativar_botoes()
    else:
        teste_tab.ativar_botoes()