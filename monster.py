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

        #If you collide with a wall, move out based on velocity
        collide = False
        from main import walls
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                collide = True

                if dx > 0: #Moving right, hit the left side of wall
                    self.rect.right = wall.rect.left
                if dx < 0: #Moving left, hit the right side of wall
                    self.rect.left = wall.rect.right
                if dy > 0: #Moving down, hit the top side of wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: #Moving up, hit the bottom side of wall
                    self.rect.top = wall.rect.bottom

        self.steps -= 1
        if collide or self.steps == 0:
            # new random direction
            self.direction = random.randint(0, 3)
            self.steps = random.randint(3, 6) * 40