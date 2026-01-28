import pygame
pygame.init()
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 500
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

pygame.draw.line(display, RED, (0, 0), (150, 150), 5)  # Line
pygame.draw.line(display, BLUE, (150, 150), (350, 350), 7)  # Line
pygame.draw.circle(display, WHITE, (350, 350), 100, 10)  # Circle
pygame.draw.circle(display, BLUE, (450, 400), 100, 10)  # Circle
pygame.draw.circle(display, YELLOW, (250, 350), 100, 10)  # Circle
pygame.draw.rect(display, GREEN, (200, 200, 50, 75), 10)  # Rectangle

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    pygame.display.update()
pygame.quit()