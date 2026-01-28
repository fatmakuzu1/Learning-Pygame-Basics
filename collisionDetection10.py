import pygame
import random
pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
character1 = pygame.image.load("monster.png")
character1_rect = character1.get_rect()
character1_rect.topleft = (10, 10)
character2 = pygame.image.load("monster2.png")
character2_rect = character2.get_rect()
character2_rect.topleft = (100, 100)

SPEED = 7
FPS = 60
clock = pygame.time.Clock()
is_running = True
while is_running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            is_running = False
        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character1_rect.left > 0:
        character1_rect.x -= SPEED
    elif keys[pygame.K_UP] and character1_rect.top > 0:
        character1_rect.y -= SPEED
    elif keys[pygame.K_RIGHT] and character1_rect.right < WINDOW_WIDTH:
        character1_rect.x += SPEED
    elif keys[pygame.K_DOWN] and character1_rect.bottom < WINDOW_HEIGHT:
        character1_rect.y += SPEED
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (255, 0, 0), (character1_rect), 1)
    pygame.draw.rect(display, (255, 0, 0), (character2_rect), 1)
    # Collision detection - Check if two characters collide
    if character1_rect.colliderect(character2_rect):
        print("coin collected")
        character2_rect.x = random.randint(0, WINDOW_WIDTH - 32)
        character2_rect.y = random.randint(0, WINDOW_HEIGHT - 32)
    display.blit(character1, character1_rect)
    display.blit(character2, character2_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
