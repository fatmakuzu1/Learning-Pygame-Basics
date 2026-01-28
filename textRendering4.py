import pygame
pygame.init() 
window_dimensions = (800, 600)
display = pygame.display.set_mode(window_dimensions)
BLUE = (0, 0, 255)
is_running = True
font_list = pygame.font.get_fonts()
for font in font_list:
    print(font)
font_name = pygame.font.SysFont("optima", 64)  # Load font
text = font_name.render("hello world", True, BLUE)  # Render text
text_rect = text.get_rect()  # Get text rectangle
text_rect.topleft = (150, 150)  # Set text position
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    display.blit(text, text_rect)  # Draw text
    pygame.display.update()
pygame.quit()