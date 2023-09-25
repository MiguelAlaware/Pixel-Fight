import sys, pygame

pygame.init()

#? Gui configuration code
size = width, height = 500, 500  #* Size of the display window
window_name = pygame.display.set_caption("Pixel-Fight")
screen = pygame.display.set_mode(size) #* Creates the graphical window
icon = pygame.image.load("Pixel-Fight/images/icon.png")
pygame.display.set_icon(icon)
CYAN = 135, 206, 235 
clock = pygame.time.Clock()

#? Player code
player = pygame.image.load("Pixel-Fight/images/knight.png") #* Loads player image
DEFAULT_IMAGE_SIZE = (50, 50)        
player = pygame.transform.scale(player, DEFAULT_IMAGE_SIZE)
player_rect = player.get_rect() #* Gets player collision
speed = 5
isJump = False
jumpCount = 10

run = True
#? Program loop code
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #* Checks for event QUIT
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and player_rect.x > speed:
            player_rect.right -= speed
        if event.key == pygame.K_RIGHT and player_rect.x < 500 - speed - 50:
            player_rect.left += speed
        if not(isJump):
            if event.key == pygame.K_SPACE:
                isJump = True 
            if event.key == pygame.K_DOWN and player_rect.y < 500 - speed - 50:
                player_rect.bottom += speed 
            if event.key == pygame.K_UP and player_rect.y > speed:
                player_rect.top -= speed 
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 10:
                    neg = -1
                player_rect.y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -=1
            else:
                jumpCount = 10
                isJump = False     
    screen.fill(CYAN) #* Updates the images (background)
    screen.blit(player, player_rect) #* Draws the images in code  
    
    pygame.display.flip() #* Buffer of pygame
    clock.tick(144) #* FPS ingame