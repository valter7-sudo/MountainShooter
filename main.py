import pygame
print(pygame.QUIT)
print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(900, 800))
print('Setup End')

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            quit()  # End pygame
