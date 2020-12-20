import pygame
import random as r
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (51, 0, 111)
CYAN = (0, 255, 255)
GOLD = (232,211,162)
Viking_Blue = (0, 63, 135, 40)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [r.randint(2,6), r.randint(-8,8)]

        self.rect = self.image.get_rect()

                                  

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


    def bounceX(self):
        self.velocity[0] = -self.velocity[0]


    def bounceY(self):
        self.velocity[1] = -self.velocity[1]