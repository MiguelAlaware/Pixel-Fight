import sys, pygame


pygame.init()

# ? Gui configuration code
size = width, height = 800, 800
window_name = pygame.display.set_caption("Pixel-Fight")
SCREEN = pygame.display.set_mode(size)
icon = pygame.image.load("data/images/icon.png")
pygame.display.set_icon(icon)

# ? Color definition
CYAN = (135, 206, 235)
BROWN = (150, 75, 0)

# ? Player code
player = pygame.transform.scale(pygame.image.load("data/images/knight.png"), (50, 50))
x_position, y_position = 400, 660
player_rect = player.get_rect(center=(x_position, y_position))
speed = 5
jumping = False
jumpCount = 10

# ? Map code

level = [pygame.Rect(0, height - 40, width, 40), pygame.Rect(300, 450, 200, 20)]

# ? Ground code
ground = pygame.Rect


# ? Program loop code
run = True
clock = pygame.time.Clock()

while run:
    # ? Display config
    clock.tick(60)
    SCREEN.blit(player, player_rect)
    pygame.display.flip()

    # ? Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ? Movement code
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x > speed:
        player_rect.x -= speed

    if keys[pygame.K_RIGHT] and player_rect.x < 760:
        player_rect.x += speed
        print(player_rect.x)

    if not (jumping):
        if keys[pygame.K_DOWN] and player_rect.y < 750:
            player_rect.y += speed
            print(player_rect.y)

        if keys[pygame.K_UP] and player_rect.y > speed:
            player_rect.y -= speed
            print(player_rect.y)

        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            player_rect.y -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1
        else:
            jumping = False
            jumpCount = 10

    # ? Update display
    SCREEN.fill(CYAN)

    # ? Game rules
    player_rect.y += 1 

    # ? Map rendering
    for platform in level:
        if player_rect.colliderect(platform) and player_rect.y < platform.y:
            player_rect.y = platform.y - player_rect.height
            
        if player_rect.colliderect(platform) and player_rect.y > platform.y:
            player_rect.y = platform.y + player_rect.height
    for platform in level:
        pygame.draw.rect(SCREEN, BROWN, platform)
