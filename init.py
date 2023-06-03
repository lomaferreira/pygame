import pygame  # importa a biblioteca
# importa do sub modulo locals todas as funções e constantes
from pygame.locals import *
# importa do modulo sys a função exit(fecha a janela do jogo)
from sys import exit

pygame.init()  # inicializa todas as funções e variaveis


largura = 640
altura = 480
x=largura/2 #controlam o movimento dos objetos(ta no centro(n exatamente))
y=0

relogio= pygame.time.Clock() #velocidade do movimento

# cria um objeto que vai ser a tela largura=640 e h=480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Game")  # muda o nome da janela

# loop infinito principal do jogo(atualização do jogo)
while True:
    tela.fill((0,0,0))#preenche a tela da cor preta a cada interação(n ver a prolongação do movimento )
    relogio.tick(100)
   
    # detecta se algum evento ocorreu
    for event in pygame.event.get():
        # testa se o evento fechar a janela do jogo ocorreu
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
    pygame.draw.rect(tela,(255,0,0),(x,y,40,50))#desenha objeto na tela(superfice, cor, posição(x,y,width,height))
    if(y>=altura):  #não sumir da tela
        y=0
    y+=1
    
   
    
    
    
    # a cada interação do loop principal atualiza o jogo, para nao travar
    pygame.display.update()






    '''
    pygame.draw.circle(tela,(0,98,55),(300,260),40)# 40 é o raio
    pygame.draw.line(tela,(255,255,0),(390,10),(90,600),10)# coordenada inicio e fim da linha e espersura da linha
    '''
    
    