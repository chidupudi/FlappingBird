import pygame
import random
from config import PIPE_WIDTH, PIPE_HEIGHT, PIPE_GAP, SCREEN_HEIGHT
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = PIPE_WIDTH
        self.gap = PIPE_GAP
        self.top_height = random.randint(50, SCREEN_HEIGHT - self.gap - 50)
        self.bottom_height = SCREEN_HEIGHT - self.top_height - self.gap
        self.image_top = pygame.image.load('pipe.png')
        self.image_bottom = pygame.image.load('pipe.png')
        print(f"Initialized pipe at ({self.x}, {self.top_height}, {self.bottom_height})")
    def move(self, speed):
        self.x -= speed
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image_top, False, True), (self.x, self.top_height - PIPE_HEIGHT))
        screen.blit(self.image_bottom, (self.x, self.top_height + self.gap))
    def get_top_rect(self):
        return pygame.Rect(self.x, self.top_height - PIPE_HEIGHT, self.width, PIPE_HEIGHT)

    def get_bottom_rect(self):
        return pygame.Rect(self.x, self.top_height + self.gap, self.width, PIPE_HEIGHT)
