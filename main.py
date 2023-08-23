import math
import sys

import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

def drawStar(screen, color, position, size, angle):
    points = []
    x, y = position

    for i in range(5):
        pointX = x - size * math.cos((2 * math.pi) * (i / 5) +
(math.pi / 2) + angle * math.pi / 180)
        pointY = y - size * math.sin((2 * math.pi) * (i / 5) +
(math.pi / 2) + angle * math.pi / 180)

        point = (pointX, pointY)
        points.append(point)

        innerPointX = x - size / 3 * math.cos((2 * math.pi) * (i / 5)
+ (math.pi / 2) + (2 * math.pi / 10) + angle * math.pi / 180)
        innerPointY = y - size / 3 * math.sin((2 * math.pi) * (i / 5)
+ (math.pi / 2) + (2 * math.pi / 10) + angle * math.pi / 180)

        innerPoint = (innerPointX, innerPointY)
        points.append(innerPoint)

    pygame.draw.polygon(screen, color, points)

while True:
    pygame.draw.rect(
        DISPLAYSURF,
        (158, 17, 17),
        pygame.Rect(0, 0, 300, 200)
    )

    pygame.draw.rect(
        DISPLAYSURF,
        (20, 117, 2),
        pygame.Rect(0, 160, 300, 40)
    )

    pygame.draw.rect(
        DISPLAYSURF,
        (20, 117, 2),
        pygame.Rect(0, 0, 300, 40)
    )

    pygame.draw.rect(
        DISPLAYSURF,
        (255, 255, 255),
        pygame.Rect(0, 40, 300, 20)
    )

    pygame.draw.rect(
        DISPLAYSURF,
        (255, 255, 255),
        pygame.Rect(0, 140, 300, 20)
    )

    drawStar(
        DISPLAYSURF,
        (248, 196, 0),  # RGB Color
        (150, 100),     # Center of the star
        35,             # Distance from center to vertex
        0               # Angle in degrees
    )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
