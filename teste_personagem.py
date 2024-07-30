import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 820))
clock = pygame.time.Clock()
running = True
dt = 0

# variáveis
food_left = 0
power_up_active = False
power_up_timer = 0

# dicionário para imagens e blocos
char_to_color = {
    '1': 'white',  # passagem
    '0': 'grey',    # parede
    '2': 'red',     # power-up
}

pygame.display.set_caption("personagem principal")

# constantes
BLOCK_SIZE = 40
GRID_WIDTH = screen.get_width() // BLOCK_SIZE
GRID_HEIGHT = screen.get_height() // BLOCK_SIZE

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def load_level():
    global food_left
    food_left = 0
    world = []
    # layout do nível diretamente no código, ajustado para 32x20 blocos
    level_layout = [
        "00000000100000000000000000000000",
        "01111110100011011101101111010110",
        "00010010111111111101101000010110",
        "01110010100000000111101000010100",
        "01111110101111100111111011111110",
        "01000110111111110000111000010000",
        "01101110101111111110101111111110",
        "00001010101111111010100000000010",
        "01111011101111100010101111111110",
        "00000000101111111010101000010010",
        "00000000101111111110111111111110",
        "01111100100000000110100111000010",
        "01001100111111111111110111111110",
        "01001111100100111111110100001110",
        "01111001100100111111110111111110",
        "01011001100100111111110110000010",
        "01011111111111110000011111111110",
        "00000000000000000000001100000000"
    ]

    for line in level_layout:
        row = []
        for block in line:
            row.append(block)
            if block == '1':
                food_left += 1
        world.append(row)
    return world

def draw_world(screen, world):
    for y, row in enumerate(world):
        for x, block in enumerate(row):
            if block in char_to_color:
                color = char_to_color[block]
                pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def eat_food(player_pos, world):
    global food_left, power_up_active, power_up_timer
    ix, iy = int(player_pos.x / BLOCK_SIZE), int(player_pos.y / BLOCK_SIZE)
    # Verificar se ix e iy estão dentro dos limites do mundo
    if 0 <= iy < len(world) and 0 <= ix < len(world[iy]):
        if world[iy][ix] == '2':
            world[iy][ix] = None
            power_up_active = True
            power_up_timer = 5  # 15 segundos de power-up

# carregar o nível
world = load_level()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # desenhar o mundo
    draw_world(screen, world)

    # velocidade do personagem
    speed = 300
    if power_up_active:
        speed = 500
