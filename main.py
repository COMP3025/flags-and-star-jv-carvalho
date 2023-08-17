import sys
import pygame
from pygame.locals import QUIT
import math

# Inicialização do Pygame
pygame.init()
DISPLAYSURF = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Tentativa da Bandeira do Suriname")

# Cores da bandeira
GREEN = (0, 156, 59)
WHITE = (255, 255, 255)
RED = (206, 17, 38)

# Função para desenhar a estrela
def drawStar(screen, color, position, size, angle):
    points = []
    x, y = position

    for i in range(5):
        pointX = x - size * math.cos((2 * math.pi) * (i / 5) + (math.pi / 2) + angle * math.pi / 180)
        pointY = y - size * math.sin((2 * math.pi) * (i / 5) + (math.pi / 2) + angle * math.pi / 180) 
        
        point = (pointX, pointY)
        points.append(point)

        innerPointX = x - size / 3 * math.cos((2 * math.pi) * (i / 5) + (math.pi / 2) + (2 * math.pi / 10) + angle * math.pi / 180)
        innerPointY = y - size / 3 * math.sin((2 * math.pi) * (i / 5) + (math.pi / 2) + (2 * math.pi / 10) + angle * math.pi / 180)

        innerPoint = (innerPointX, innerPointY)
        points.append(innerPoint)

    pygame.draw.polygon(screen, color, points)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Preencher a tela com a cor de fundo
    DISPLAYSURF.fill(WHITE)

    # Desenhar as faixas horizontais
    pygame.draw.rect(DISPLAYSURF, GREEN, pygame.Rect(0, 0, 300, 40))
    pygame.draw.rect(DISPLAYSURF, GREEN, pygame.Rect(0, 200 - 40, 300, 40))

    # Desenhar as faixas verticais
    pygame.draw.rect(DISPLAYSURF, RED, pygame.Rect(0, 40, 40, 160))
    pygame.draw.rect(DISPLAYSURF, RED, pygame.Rect(260, 40, 40, 160))

    # Desenhar a estrela
    drawStar(
        DISPLAYSURF, 
        (248, 196, 0),  
        (150, 100),     
        30,             
        0               
    )
    
    pygame.display.update()
