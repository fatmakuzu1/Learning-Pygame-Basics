import pygame
pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
character = pygame.image.load("monster.png")  # Load PNG image file
character_rect = character.get_rect()  # Get rectangle bounds of image
character_rect.topleft = (10, 10)  # Set image top-left position

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    display.blit(character, character_rect)
    pygame.display.update()




pygame.quit()