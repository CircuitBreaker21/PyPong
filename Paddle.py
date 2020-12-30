import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (51, 0, 111)
CYAN = (0, 255, 255)
GOLD = (232, 211, 162)
Viking_Blue = (0, 63, 135, 40)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def moveUp(self, pixel_amount):
        self.rect.y -= pixel_amount
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixel_amount):
        self.rect.y += pixel_amount
        if self.rect.y > 400:
            self.rect.y = 400
