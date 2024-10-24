import pygame, sys, random

pygame.init()
WIDTH, HEIGHT, SIZE = 400, 400, 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100, 100)]
dx, dy = 0, 0  
food = (random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0: dx, dy = 0, -SIZE
    if keys[pygame.K_DOWN] and dy == 0: dx, dy = 0, SIZE
    if keys[pygame.K_LEFT] and dx == 0: dx, dy = -SIZE, 0
    if keys[pygame.K_RIGHT] and dx == 0: dx, dy = SIZE, 0
    
    if dx != 0 or dy != 0:
        new_head = (snake[0][0] + dx, snake[0][1] + dy)
        snake = [new_head] + snake
        
        if new_head == food:
            food = (random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE))
        else:
            snake.pop() 

        if new_head in snake[1:] or not 0 <= new_head[0] < WIDTH or not 0 <= new_head[1] < HEIGHT:
            break

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (*food, SIZE, SIZE))
    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, SIZE, SIZE))
    
    pygame.display.update()
    clock.tick(10)  
