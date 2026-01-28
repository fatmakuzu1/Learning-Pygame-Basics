import pygame
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
SPEED = 5
character = pygame.image.load("monster.png")
character_rect = character.get_rect()
character_rect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
FPS = 30
clock = pygame.time.Clock()
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character_rect.left > 0:  # Boundary check left
        character_rect.x -= SPEED
    elif keys[pygame.K_UP] and character_rect.top > 0:  # Boundary check top
        character_rect.y -= SPEED
    elif keys[pygame.K_RIGHT] and character_rect.right < WINDOW_WIDTH:  # Boundary check right
        character_rect.x += SPEED
    elif keys[pygame.K_DOWN] and character_rect.bottom < WINDOW_HEIGHT:  # Boundary check bottom
        character_rect.y += SPEED
    display.fill((0, 0, 0))
    display.blit(character, character_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()