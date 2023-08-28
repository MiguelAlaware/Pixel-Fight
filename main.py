import sys, pygame
pygame.init()

#? Gui configuration code
size = width, height = 249, 140  #* Size of the display window
screen = pygame.display.set_mode(size) #* Creates the graphical window
cyan = 100, 0, 200

#? Player code
player = pygame.image.load("images/knight.png") #* Loads player image
player = pygame.transform.scale(player, (size[0] / 2, size[1] / 2))
player_rect = player.get_rect() #* Gets player collision

speed = [1, 1]

#? Program loop code
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #* Checks for event QUIT
            sys.exit()

    player_rect = player_rect.move(speed) #* Get the player movement going
    if player_rect.left < 0 or player_rect.right > width:
        speed[0] = -speed[0]
    if player_rect.top < 0 or player_rect.bottom > height:
        speed[1] = -speed[1]
        
    screen.fill(cyan) #* Updates the images
    screen.blit(player, player_rect) #* Draws the images in code  
    pygame.display.flip() #* Buffer of pygame