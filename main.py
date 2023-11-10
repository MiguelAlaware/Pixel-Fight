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
BLACK = (0, 0, 0)

# ? Player code
rect = pygame.Rect(300, 200, 50, 50)
rect_surface = pygame.Surface((rect.width, rect.height))
rect_surface.fill(BLACK)
speed = 5
jumping = False
jumpCount = 10

# ? Map code
level = [pygame.Rect(0, height - 40, width, 40), pygame.Rect(300, 450, 200, 30)]

# ? Ground code
ground = pygame.Rect


# ? Program loop code
run = True
clock = pygame.time.Clock()

# * Game functions

while run:
    # ? Display config
    clock.tick(60)
    SCREEN.blit(rect_surface, (rect.x, rect.y))
    pygame.display.flip()

    # ? Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ? Movement code
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect.x > speed:
        rect.x -= speed
        print(f"Player x:{rect.x}")

    if keys[pygame.K_RIGHT] and rect.x < 760:
        rect.x += speed
        print(f"Player x:{rect.x}")

    if not (jumping):
        if keys[pygame.K_DOWN] and rect.y < 750:
            rect.y += speed
            print(f"Player y: {rect.y}")

        if keys[pygame.K_UP] and rect.y > speed:
            rect.y -= speed
            print(f"Player y: {rect.y}")

        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            rect.y -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1
            if rect.colliderect(platform):
                if rect.y + rect.height > platform.y:
                    rect.y = platform.y - rect.height
                    jumpCount = 0
        else:
            jumping = False
            jumpCount = 10

    # ? Update display
    SCREEN.fill(CYAN)

    # ? Game rules
    #rect.y += 1

    # ? Map rendering
    for platform in level:
        if rect.colliderect(platform):
           if rect.y < platform.y:
              rect.y = platform.y - rect.height
           if rect.x < platform.x:
               rect.x = platform.x - rect.width
           else:
               rect.x = platform.x + rect.width 
              
    
            
    for platform in level:
        pygame.draw.rect(SCREEN, BROWN, platform)
