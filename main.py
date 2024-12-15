import pygame
import sys
from bird import Bird
from pipe import Pipe
from config import SCREEN_WIDTH, SCREEN_HEIGHT
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Initialize bird and pipes
bird = Bird(100, SCREEN_HEIGHT // 2)
pipes = [Pipe(300), Pipe(500), Pipe(700)]

def draw_start_button(screen):
    font = pygame.font.Font(None, 74)
    text = font.render("START", True, (255, 255, 255))
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    pygame.draw.rect(screen, (0, 0, 0), rect.inflate(20, 20))
    screen.blit(text, rect)
    return rect

def check_collision(bird, pipes):
    for pipe in pipes:
        if bird.get_rect().colliderect(pipe.get_top_rect()) or bird.get_rect().colliderect(pipe.get_bottom_rect()):
            return True
    if bird.y < 0 or bird.y > SCREEN_HEIGHT - bird.height:
        return True
    return False

# Game state
game_started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_started:
                bird.flap()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            if start_button_rect.collidepoint(event.pos):
                game_started = True

    if game_started:
        bird.move()

        for pipe in pipes:
            pipe.move(3)
            if pipe.x < -pipe.width:
                pipes.remove(pipe)
                pipes.append(Pipe(SCREEN_WIDTH))

        screen.fill((135, 206, 235))  # Light blue background
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        if check_collision(bird, pipes):
            print("Game Over")
            pygame.quit()
            sys.exit()
    else:
        screen.fill((135, 206, 235))  # Light blue background
        start_button_rect = draw_start_button(screen)

    pygame.display.flip()
    clock.tick(30)
