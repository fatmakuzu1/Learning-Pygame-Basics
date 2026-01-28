import pygame

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
character = pygame.image.load("monster2.png")
character_rect = character.get_rect()
character_rect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Check if mouse button clicked
            mouse_x_value = event.pos[0]  # Get mouse X position
            mouse_y_value = event.pos[1]  # Get mouse Y position
            character_rect.x = mouse_x_value  # Move character to mouse X
            character_rect.y = mouse_y_value  # Move character to mouse Y
        display.fill((0, 0, 0))
            
    display.blit(character, character_rect) 
    
    pygame.display.update()



pygame.quit()