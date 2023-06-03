import pygame #importa a biblioteca
from pygame.locals import * #importa do sub modulo locals todas as funções e constantes
from sys import exit #importa do modulo sys a função exit(fecha a janela do jogo)

pygame.init() #inicializa todas as funções e variaveis


largura=640
altura=480
#cria um objeto que vai ser a tela largura=640 e h=480
tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Game")#muda o nome da janela

#loop infinito principal do jogo(atualização do jogo)
while True:
    #detecta se algum evento ocorreu
    for event in pygame.event.get():
        #testa se o evento fechar a janela do jogo ocorreu 
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()#a cada interação do loop principal atualiza o jogo, para nao travar        
