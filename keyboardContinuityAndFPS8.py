import pygame
# FPS = Frame Per Second

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
SPEED = 5
character = pygame.image.load("monster.png")
character_rect = character.get_rect()
character_rect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
# FPS Configuration
FPS = 30
clock = pygame.time.Clock()


display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()  # Get continuous key press state
    if keys[pygame.K_LEFT]:  # Move left
        character_rect.x -= SPEED
    elif keys[pygame.K_UP]:  # Move up
        character_rect.y -= SPEED
    elif keys[pygame.K_RIGHT]:  # Move right
        character_rect.x += SPEED
    elif keys[pygame.K_DOWN]:  # Move down
        character_rect.y += SPEED
    display.fill((0, 0, 0))
    display.blit(character, character_rect)
    pygame.display.update() 
    clock.tick(FPS)  # Control frame rate


pygame.quit()