import pygame
from config import BIRD_WIDTH, BIRD_HEIGHT, FLAP_STRENGTH, GRAVITY

class Bird:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.velocity = 0
        self.image = pygame.image.load('bird.png')
        print(f"Initialized bird at ({self.x}, {self.y})")
        

    def flap(self):
        self.velocity = FLAP_STRENGTH
        

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        print(f"Bird position: ({self.x}, {self.y})")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
