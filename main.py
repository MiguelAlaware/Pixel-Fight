import sys, pygame, assets
pygame.init()


#? Gui configuration code
size = width, height = 640, 480  #* Size of the display window
screen = pygame.display.set_mode(size) #* Creates the graphical window
cyan = 135, 206, 235 
clock = pygame.time.Clock()

#? Player code
player = pygame.image.load("images/knight.png") #* Loads player image
DEFAULT_IMAGE_SIZE = (50, 50)        
player = pygame.transform.scale(player, DEFAULT_IMAGE_SIZE)
player_rect = player.get_rect() #* Gets player collision
speed = 3

speed = [1, 1]

#? Program loop code
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #* Checks for event QUIT
            sys.exit()

        
     
    screen.fill(cyan) #* Updates the images (background)
    screen.blit(player, player_rect) #* Draws the images in code  
    
    pygame.display.flip() #* Buffer of pygame
    clock.tick(144) #* FPS ingame