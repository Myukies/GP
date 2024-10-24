import pygame, sys

pygame.init()
WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(WIDTH//2 - 15, HEIGHT - 40, 30, 10)
player_speed = 5

bullets = []
bullet_speed = -7

alien_rows, alien_cols = 5, 8
alien_speed = 2
aliens = [pygame.Rect(50 + 40 * col, 50 + 30 * row, 30, 20) for row in range(alien_rows) for col in range(alien_cols)]
alien_direction = 1

game_over = False
score = 0
font = pygame.font.Font(None, 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.move_ip(-player_speed, 0)
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.move_ip(player_speed, 0)
        if keys[pygame.K_SPACE]:
            if len(bullets) < 3:
                bullets.append(pygame.Rect(player.centerx - 2, player.top - 5, 5, 10))

        bullets = [b.move(0, bullet_speed) for b in bullets if b.bottom > 0]

        alien_movement = alien_speed * alien_direction
        for alien in aliens:
            alien.move_ip(alien_movement, 0)
        if any(alien.right >= WIDTH or alien.left <= 0 for alien in aliens):
            alien_direction *= -1
            for alien in aliens:
                alien.move_ip(0, 20)

        for alien in aliens[:]:
            for bullet in bullets[:]:
                if bullet.colliderect(alien):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    score += 1
                    break

        if any(alien.bottom >= HEIGHT for alien in aliens):
            game_over = True

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)
    for alien in aliens:
        pygame.draw.rect(screen, (255, 0, 0), alien)

    if game_over:
        text = font.render("Game Over", True, (255, 255, 255))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    else:
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)
