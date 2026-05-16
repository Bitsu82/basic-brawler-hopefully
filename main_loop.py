import pygame,sys
import basic_brawler as bb

pygame.init()

#making the screen
HIEGHT = 800
WIDTH = 1200
screen = pygame.display.set_mode((WIDTH, HIEGHT))
clock = pygame.time.Clock()

    #setting up player character 

all_sprites = pygame.sprite.Group()
guy1 = bb.PlayerCharacter("Arthur", "guy.jpg", 100, 400, all_sprites, scale = 0.25)
guy2 = bb.PlayerCharacter("Merlin", "guy2.jpeg", 1000, 400, all_sprites, scale = 0.505)
    




while True:   

    keys = pygame.key.get_pressed()

    #guy1 controls

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
        if event.type == pygame.K_UP:
            guy2.jump
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung tung sahur')
                pygame.quit()
                sys.exit()
            if event.key  ==  pygame.K_w:
                guy1.jump()
            if event.key  ==  pygame.K_UP:
                guy2.jump()
    




    all_sprites.update()
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)
            
