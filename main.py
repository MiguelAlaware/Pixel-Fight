import sys, pygame

pygame.init()

# ? Gui configuration code
size = width, height = 800, 800
window_name = pygame.display.set_caption("Pixel-Fight")
SCREEN = pygame.display.set_mode(size)
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
CYAN = 135, 206, 235

# ? Player code
player = pygame.transform.scale(pygame.image.load("images/knight.png"), (50, 50))
x_position, y_position = 400, 660
player_rect = player.get_rect(center=(x_position, y_position))
speed = 5
jumpHeight = 20
y_velocity = jumpHeight
jumping = False

# ? Game rules
y_gravity = 1

# ? Program loop code
run = True
CLOCK = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # ? Movement code
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        player_rect.y += speed
        print(player_rect.y)

    if keys[pygame.K_LEFT]:
        player_rect.x -= speed

    if keys[pygame.K_RIGHT]:
        player_rect.x += speed

    if keys[pygame.K_UP]:
        player_rect.y -= speed

    if keys[pygame.K_SPACE]:
        jumping = True

    if jumping:
        y_position -= y_velocity
        y_velocity -= y_gravity
        if y_velocity < -jumpHeight:
            jumping = False
            y_velocity = jumpHeight
        player_rect = player.get_rect()

    # ? Display config
    SCREEN.fill(CYAN)
    SCREEN.blit(player, player_rect)
    pygame.display.flip()
    CLOCK.tick(60)
