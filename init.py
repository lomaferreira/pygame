import pygame  # importa a biblioteca
# importa do sub modulo locals todas as funções e constantes
from pygame.locals import *
# importa do modulo sys a função exit(fecha a janela do jogo)
from sys import exit
from random import randint  # importa a funçao randint(sortea valores)

pygame.init()  # inicializa todas as funções e variaveis


pygame.mixer.music.set_volume(0.1)#controla o volume da musica de fundo entre 0 e 1
musica_de_fundo=pygame.mixer.music.load('assets/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)#executa a música e repete depois que termina com o -1

barulho_colisao=pygame.mixer.Sound('assets/smw_1-up.wav')
barulho_colisao.set_volume(0.5)



largura = 640
altura = 480
x = int(largura/2)  # controlam o movimento dos objetos(ta no centro(n exatamente))
y = int(altura/2)

# posições de escolha pra x, desconsiderando a altura do retangulo pra n sair da tela
x_azul = randint(40, 600)
y_azul = randint(50, 430)


pontos = 0
# pygame.font.get_fonts() ver as fontes disponiveis
fonte = pygame.font.SysFont('arial', 40, True, True)


relogio = pygame.time.Clock()  # velocidade do movimento

# cria um objeto que vai ser a tela largura=640 e h=480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Game")  # muda o nome da janela

# loop infinito principal do jogo(atualização do jogo)
while True:
    # preenche a tela da cor preta a cada interação(n ver a prolongação do movimento )
    tela.fill((0, 0, 0))
    relogio.tick(30)

    mensagem = f"Pontos:{pontos}"

    # uni a msg e a fonte(mensagem, false=maisPixelado)
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    # detecta se algum evento ocorreu
    for event in pygame.event.get():
        # testa se o evento fechar a janela do jogo ocorreu
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:  # Se teclar ou precionar a tecla A
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20

    # desenha objeto na tela(superfice, cor, posição(x,y,width,height))
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 225), (x_azul, y_azul, 40, 50))

    # colliderect método do retangulo de colizão
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
    # rederiza a msg na tela na seguinte posição
    tela.blit(texto_formatado, (450, 440))

    # a cada interação do loop principal atualiza o jogo, para nao travar
    pygame.display.update()

    '''
    pygame.draw.circle(tela,(0,98,55),(300,260),40)# 40 é o raio
    pygame.draw.line(tela,(255,255,0),(390,10),(90,600),10)# coordenada inicio e fim da linha e espersura da linha
    '''

    '''
    if(y>=altura):  #não sumir da tela o objeto
        y=0
    y+=1
    '''

    '''
        #controla movimentos(dentro do for event) 
        if event.type == KEYDOWN:#qualquer tecla
           if event.key==K_a: #tecla A
               x-=20
           if event.key==K_d: #tecla D
               x+=20
           if event.key==K_w: #tecla W
               y-=20
           if event.key==K_s: #tecla S
               y+=20         
        '''
