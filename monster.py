import random
import pygame


class Monster(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 40, 40)
        self.dist = 3
        self.direction = random.randint(0, 3)
        self.steps = random.randint(3, 6) * 40

    def move(self):
        direction_list = ((-10, 0), (10, 0), (0, -10), (0, 10))
        dx, dy = direction_list[self.direction]
        self.rect.x += dx
        self.rect.y += dy

        # Limitar a saída do monstro da tela
        if self.rect.top < 120:
            self.rect.top = 120
            self.direction = random.randint(0, 3)
        if self.rect.bottom > 770:
            self.rect.bottom = 770
            self.direction = random.randint(0, 3)

        # Colide com a parede, move pro outro lado aleatório
        collide = False
        from main import walls
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                collide = True

                if dx > 0:  # Move pra direita, bateu no lado esquerdo da parede
                    self.rect.right = wall.rect.left
                if dx < 0:  # Move para esquerda, bateu no lado direito da parede
                    self.rect.left = wall.rect.right
                if dy > 0:  # Move para baixo, bateu no lado de cima da parede
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Move para cima, bateu no lado de baixo da parede
                    self.rect.top = wall.rect.bottom

        self.steps -= 1
        if collide or self.steps == 0:
            # new random direction
            self.direction = random.randint(0, 3)
            self.steps = random.randint(3, 6) * 40
