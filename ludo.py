import tkinter
from View import teste_tab
from Model import regras_jogo
from Controller import event_handler

# Criação da janela principal
root = tkinter.Tk()

# Criação de um canvas na janela principal
regras_jogo.novo_jogo()
c = tkinter.Canvas(root, width=800, height=600)
c.bind('<ButtonRelease-1>', event_handler.click)

teste_tab.desenha_tabuleiro(c)
teste_tab.desenha_botoes(root, c)
teste_tab.combobox(root,c)

c.pack()
root.mainloop()
