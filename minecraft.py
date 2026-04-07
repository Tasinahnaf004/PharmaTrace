import pygame

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# World: 10x10 grid, 0 = empty, 1 = block
world = [[0]*10 for _ in range(10)]

player_x, player_y = 5, 5

running = True
while running:
    screen.fill((135, 206, 235))  # sky blue background

    # Draw blocks
    for y in range(10):
        for x in range(10):
            if world[y][x] == 1:
                pygame.draw.rect(screen, (139, 69, 19), (x*40, y*40, 40, 40))  # brown block

    # Draw player
    pygame.draw.rect(screen, (255, 0, 0), (player_x*40, player_y*40, 40, 40))

    pygame.display.flip()
    clock.tick(30)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: player_x = max(0, player_x-1)
            if event.key == pygame.K_RIGHT: player_x = min(9, player_x+1)
            if event.key == pygame.K_UP: player_y = max(0, player_y-1)
            if event.key == pygame.K_DOWN: player_y = min(9, player_y+1)
            if event.key == pygame.K_SPACE:  # place block
                world[player_y][player_x] = 1
            if event.key == pygame.K_BACKSPACE:  # remove block
                world[player_y][player_x] = 0

pygame.quit()
