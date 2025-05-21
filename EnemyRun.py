import pygame  # type: ignore
import math

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the font — Verdana, size 10
font = pygame.font.SysFont('verdana', 10)

# Player (red rectangle)
player_x, player_y = 300, 200
player_width, player_height = 25, 25
player_speed = 0.5

# Enemy (green rectangle)
enemy_x, enemy_y = 100, 100
enemy_width, enemy_height = 25, 25
enemy_speed = 0.25

score = 0

# Set up a timer event for increasing score every 1000 ms (1 second)
INCREMENT_SCORE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(INCREMENT_SCORE_EVENT, 1000)


run = True
while run:
    screen.fill((0, 0, 0))

    # Update player and enemy rectangles
    player = pygame.Rect(int(player_x), int(player_y), player_width, player_height)
    enemy = pygame.Rect(int(enemy_x), int(enemy_y), enemy_width, enemy_height)

    # Draw the rectangles
    pygame.draw.rect(screen, (255, 0, 0), player)  # Red for player
    pygame.draw.rect(screen, (0, 255, 0), enemy)  # Green for enemy

    # Render and draw the score in the top-right corner
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    text_rect = score_text.get_rect(topright=(SCREEN_WIDTH - 5, 5))  # small padding from edges
    screen.blit(score_text, text_rect)

    # Move player with boundary checks
    key = pygame.key.get_pressed()
    if (key[pygame.K_a] or key[pygame.K_LEFT]) and player_x > 0:  # Left
        player_x -= player_speed
    if (key[pygame.K_d] or key[pygame.K_RIGHT]) and player_x + player_width < SCREEN_WIDTH:  # Right
        player_x += player_speed
    if (key[pygame.K_w] or key[pygame.K_UP]) and player_y > 0:  # Up
        player_y -= player_speed
    if (key[pygame.K_s] or key[pygame.K_DOWN]) and player_y + player_height < SCREEN_HEIGHT:  # Down
        player_y += player_speed

    # Move enemy toward the player
    dx = player_x - enemy_x
    dy = player_y - enemy_y
    distance = math.sqrt(dx**2 + dy**2)
    if distance != 0:  # Avoid division by zero
        enemy_x += (dx / distance) * enemy_speed
        enemy_y += (dy / distance) * enemy_speed


    # Check for collision
    if player.colliderect(enemy):
        print("Collision Detected!")
        run = False

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run = False
        if event.type == INCREMENT_SCORE_EVENT:
            score += 1  # Increase score every second

    pygame.display.update()

pygame.quit()
