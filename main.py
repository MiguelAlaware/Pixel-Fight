import sys, pygame

pygame.init()

#? Gui configuration code
size = width, height = 800, 800
window_name = pygame.display.set_caption("Pixel-Fight")
screen = pygame.display.set_mode(size) 
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
CYAN = 135, 206, 235 
clock = pygame.time.Clock()

#? Player code
player = pygame.image.load("images/knight.png") 
DEFAULT_IMAGE_SIZE = (50, 50)        
player = pygame.transform.scale(player, DEFAULT_IMAGE_SIZE)
player_rect = player.get_rect()
speed = 5
isJump = False
jumpCount = 10 
run = True

#? Program loop code
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
            
    #? Movement code
    keys = pygame.key.get_pressed()
    
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_LEFT] and player_rect.x > speed:
            player_rect.x -= speed

        if keys[pygame.K_RIGHT] and player_rect.x < width - 50 - speed:
            player_rect.x += speed

        if not(isJump):  
            if keys[pygame.K_SPACE]:
                isJump = True 
            
            if keys[pygame.K_DOWN] and player_rect.y < height - 50 - speed:
                player_rect.y += speed
                 
            if keys[pygame.K_UP] and player_rect.y > speed:
                player_rect.y -= speed 
        
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                player_rect.y -= (jumpCount * abs(jumpCount)) * 0.5 * neg 
                jumpCount -=1
            else:
                jumpCount = 10
                isJump = False     

    #? Display code
    screen.fill(CYAN) 
    screen.blit(player, player_rect)   
    pygame.display.flip() 
    clock.tick(144)