import pygame
pygame.init()
window_dimensions = (800, 600)
display = pygame.display.set_mode(window_dimensions)
BLUE = (0, 0, 255)
is_running = True
sound_effect1 = pygame.mixer.Sound("sound.wav")  # Load first sound
sound_effect1.play()
pygame.time.delay(2000)  # Wait 2 seconds
sound_effect2 = pygame.mixer.Sound("sound2.wav")  # Load second sound
sound_effect2.play()
pygame.time.delay(2000)  # Wait 2 seconds
pygame.mixer.music.load("arkaplanses.wav")  # Load background music
pygame.mixer.music.play(-1, 0.0)  # Play infinite loop
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    pygame.display.update()
pygame.quit()