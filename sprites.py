import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

preto = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

# animando os sprites com POO


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        # inicializar a class herdada do pygame chamada Sprite na nova class Sapo
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []  # criando uma lista pra amazenar as sprites
        # add img na lista sprites
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_1.png'))
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_2.png'))
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_3.png'))
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_4.png'))
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_5.png'))
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_6.png'))
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_7.png'))
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_8.png'))
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_9.png'))
        self.sprites.append(pygame.image.load(
            'animation_sprites/attack_10.png'))
        self.atual = 0
        # atributo da class Sprites do pygame que recebe o primeiro elemento da lista
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(
            self.image, (128*3, 64*3))  # aumentar a escala da imagem

        # o atributo da class Sprite vai receber um método do atributo image que pegar as coordenadas da sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100  # em cima na esquerda
        self.animar = False

    # método que faz o sapo se mover quando pressionado a tecla
    def atacar(self):
        self.animar = True

    # método da class Sprite do pygame
    def update(self):
        if self.animar == True:
            self.atual = self.atual + 1  # 0.05 diminui a velocidade que as sprites trocam
            # testa se chegou no fim da lista e volta pro começo
            if self.atual >= len(self.sprites):
                self.atual = 0
                # para a animação, que vai voltar se apertar a tecla novamente, já estando o indice na posição 0
                self.animar = False
            self.image = self.sprites[self.atual]  # mudando o índice da lista
            self.image = pygame.transform.scale(
                self.image, (128*3, 64*3))


# um grupo que vai armazenar as sprites
todas_as_sprites = pygame.sprite.Group()
# Criando um objeto
sapo = Sapo()
todas_as_sprites.add(sapo)

# ajustar os frame do jogo
relogio = pygame.time.Clock()

while True:
    tela.fill(preto)
    relogio.tick(10)  # escolho a quantidade de quadros
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # O objeto sapo recebe o metodo atacar quando pressionado qualquer tecla
        if event.type == KEYDOWN:
            sapo.atacar()

    todas_as_sprites.draw(tela)  # desenhar as sprites na tela
    todas_as_sprites.update()

    pygame.display.flip()  # Mesmo papel do display.update
