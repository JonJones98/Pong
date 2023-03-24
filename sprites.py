import pygame
from random import randint
# Define Colors (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED =(255,0,0)
BLUE = (0,0,255)
ORANGE = (255,165,0)
GREEN = (0,255,0)
PURPLE =(128,128,0)
COLORS = [RED, BLUE, WHITE, ORANGE, GREEN, PURPLE]
#Sprites
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y =0
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #Draw Ball
        pygame.draw.rect(self.image, color, [0,0,width, height])
        self.velocity = [randint(4,6),randint(-8,6)]
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
