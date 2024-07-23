import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 820))
clock = pygame.time.Clock()
running = True
dt = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Ação de clicar no X da janela
            running = False

    screen.fill('white')

    pygame.display.flip()

    clock.tick(120)
    dt = clock.tick(120) / 1000


pygame.quit()
