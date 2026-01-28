import pygame  # Import pygame library
pygame.init()  # Initialize pygame
window_width_height = (800, 600)  # Set window size
window = pygame.display.set_mode(window_width_height)  # Create and open window
is_running = True  # Set game loop flag

while is_running:  # Start main loop
    for event in pygame.event.get():  # Get all events
        if event.type == pygame.QUIT:  # Check if close button clicked
            is_running = False  # Exit loop

pygame.quit()  # Close pygame and window