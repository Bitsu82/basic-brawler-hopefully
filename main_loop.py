import pygame
import sys
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
guy1.rect = guy1.image.get_rect()

guy2_og = pygame.image.load('guy2.jpeg').convert() #load sprite so we can transform it
guy2_scaled = pygame.transform.scale_by(guy2_og, 0.25)
guy2 = pygame.sprite.Sprite()
guy2.image = guy2_scaled
guy2.rect = guy2.image.get_rect()

screen.blit(guy1.image, (100, 200))

guy1_group = pygame.sprite.GroupSingle(guy1)
guy2_group = pygame.sprite.GroupSingle(guy2)


while True:
 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            print("skibidi for now")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            print("skibidi for now")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            print("skibidi for now")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            print("skibidi for now")
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    guy1_group.draw(screen)
    pygame.display.update()
    screen.fill((30, 30, 30))
            
