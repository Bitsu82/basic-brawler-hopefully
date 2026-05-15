import pygame,sys,basic_brawler

pygame.init()

#making the screen
HIEGHT = 800
WIDTH = 1200
screen = pygame.display.set_mode((WIDTH, HIEGHT))

#setting up player character 
guy1_og = pygame.image.load('guy.jpg').convert() #load sprite so we can transform it
guy1_scaled = pygame.transform.scale_by(guy1_og, 0.25)
guy1 = pygame.sprite.Sprite()
guy1.image = guy1_scaled
guy1.rect = guy1.image.get_rect(topleft=(100,100))

guy2_og = pygame.image.load('guy2.jpeg').convert() #load sprite so we can transform it
guy2_scaled = pygame.transform.scale_by(guy2_og, 0.505)
guy2 = pygame.sprite.Sprite()
guy2.image = guy2_scaled
guy2.rect = guy2.image.get_rect(topright = (400,100))

player_grav = 0

guy1_group = pygame.sprite.GroupSingle(guy1)
guy2_group = pygame.sprite.GroupSingle(guy2)


while True:   

    keys = pygame.key.get_pressed()

    player_grav += 0.05        
    guy1.rect.y += player_grav        
    guy2.rect.y += player_grav 
    

    #guy1 controls
    if keys[pygame.K_w]:
        guy1.rect.y -= 1
    if keys[pygame.K_a]:
        guy1.rect.x -= 1
    if keys[pygame.K_s]:
         guy1.rect.y += 1
    if keys[pygame.K_d]:
        guy1.rect.x += 1

            #guy 2 controls
    if keys[pygame.K_UP]:
         guy2.rect.y -= 1
    if keys[pygame.K_LEFT]:
        guy2.rect.x -= 1
    if keys[pygame.K_DOWN]:
         guy2.rect.y += 1
    if keys[pygame.K_RIGHT]:
        guy2.rect.x += 1


    for event in pygame.event.get():

        if guy1.rect.bottom <= HIEGHT:
            player_grav = 0
            if keys[pygame.K_SPACE]:
                player_grav = -6
  
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print('tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung sahur')
            pygame.quit()
            sys.exit()
    





    screen.fill((30, 30, 30))
    guy1_group.draw(screen)
    guy2_group.draw(screen)
    pygame.display.update()
            
