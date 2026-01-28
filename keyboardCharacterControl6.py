import pygame
pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SPEED = 50

# Load character image

character = pygame.image.load("monster2.png")
character_rect = character.get_rect()
character_rect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)


is_running = True  # Main loop control flag
while is_running:  # Start main game loop
    for event in pygame.event.get():  # Get all events from queue
        # print(event) - would print all events
        if event.type == pygame.QUIT:  # Check if quit button clicked
            is_running = False  # Exit loop
        if event.type == pygame.KEYDOWN:  # Check if key pressed
            if event.key == pygame.K_RIGHT:  # Move right
                character_rect.x += SPEED
            elif event.key == pygame.K_LEFT:  # Move left
                character_rect.x -= SPEED
            elif event.key == pygame.K_UP:  # Move up
                character_rect.y -= SPEED
            elif event.key == pygame.K_DOWN:  # Move down
                character_rect.y += SPEED
        display.fill((0, 0, 0))

        display.blit(character, character_rect)    
        pygame.display.update() 







pygame.quit()