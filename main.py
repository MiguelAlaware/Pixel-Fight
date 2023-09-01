import sys, pygame, assets
pygame.init()


#? Gui configuration code
size = width, height = 640, 480  #* Size of the display window
screen = pygame.display.set_mode(size) #* Creates the graphical window
CYAN = 135, 206, 235 
clock = pygame.time.Clock()

#? Player code
player = pygame.image.load("images/knight.png") #* Loads player image
DEFAULT_IMAGE_SIZE = (50, 50)        
player = pygame.transform.scale(player, DEFAULT_IMAGE_SIZE)
player_rect = player.get_rect() #* Gets player collision
speed = 5

run = True
#? Program loop code
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #* Checks for event QUIT
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print('left')
            player_rect.right -= speed
        if event.key == pygame.K_RIGHT:
            print('right')
            player_rect.left += speed
        if event.key == pygame.K_UP:
            print('up')
            player_rect.top -= speed 
        if event.key == pygame.K_DOWN:
            print('down')      
            player_rect.bottom += speed

     
    screen.fill(CYAN) #* Updates the images (background)
    screen.blit(player, player_rect) #* Draws the images in code  
    
    pygame.display.flip() #* Buffer of pygame
    clock.tick(144) #* FPS ingame