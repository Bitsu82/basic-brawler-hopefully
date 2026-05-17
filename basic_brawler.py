import pygame,sys,time
from enum import Enum

# All possible states a character can be in
#enums are a list of named options
# yk so like here is a list what are u going to choose 
# this helps like with errors and stuff so if i mispell it it immediately noticeable
#its also just good common practice
class State(Enum):
    IDLE = "idle"
    SHIELDING = "shielding"
    SHIELD_BROKEN = "shield_broken"
    ATTACKING = "attacking"
    HURT = "hurt"

class PlayerCharacter(pygame.sprite.Sprite):
    def __init__(self, char_name, image_path, x, y, groups, scale = 1.0):
        super().__init__(groups)


        self.char_name = char_name
        image_og = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale_by(image_og, scale) 
        self.rect = self.image.get_rect(topleft=(x, y))
        self.max_health = 100
        self.health = self.max_health#boring health stuff
        self.gravity = 0 
        self.gravity_strength = 1 #boring gravity stuff
        self.ground_level = 700 # where the floor is
        self.attack_mod = 1.0# cuz this is the parent class it is one but it is an attack mult
        self.state = State.IDLE # starting tate is doing nothing
        self.state_start_time = 0 #we need a starting point for the later states to ovveride so we just bs one
        self.shield_hits_remaining = 4 #max hits of the shield basically
        self.SHIELD_DURATION = 4000      # 4 seconnds for how long the shield will live
        self.SHIELD_BREAK_ENDLAG = 3000  # 3 seconds of endlag once the shield breaks
        self.combo_count = 0
        self.max_combo = 3
        self.last_hit_time = 0
        self.combo_window = 750
        self.punch_hitbox = None
        self.shield_hitbox = None
        self.hitstun_duration = 0
        self.facing = "right"


    def update(self):
        self.grav()
        self.state_check_timers()
        self.update_hitboxes()

    def update_hitboxes(self):
        if self.shield_hitbox:
            self.shield_hitbox.topleft = (self.rect.left, self.rect.top)

        if self.punch_hitbox:
            if self.facing == "right":
                self.punch_hitbox.topleft = (self.rect.right, self.rect.centery - 20)
            else:
                self.punch_hitbox.topleft = (self.rect.left - 80, self.rect.centery - 20)

    def state_check_timers(self):
        elapsed = pygame.time.get_ticks() - self.state_start_time  

        if self.state == State.SHIELDING:          #this is all checking what state ypu are in and then like updateing it if certain conditions are met
            if elapsed >= self.SHIELD_DURATION:
                self.change_state(State.IDLE)

        elif self.state == State.SHIELD_BROKEN:
            if elapsed >= self.SHIELD_BREAK_ENDLAG:
                self.shield_hitbox = None                
                self.change_state(State.IDLE)


        elif self.state == State.HURT:
            if elapsed >= self.hitstun_duration:   # hitstun over you can act again
                self.change_state(State.IDLE)

        elif self.state == State.ATTACKING:
            if elapsed >= 300:                     # we have endlag now yay
                self.punch_hitbox = None                
                self.change_state(State.IDLE)


    def change_state(self,new_state):
        self.state = new_state
        self.state_start_time = pygame.time.get_ticks()

    def grav(self):
        if self.rect.bottom >= self.ground_level:
            self.rect.bottom = self.ground_level
            self.gravity = 0
        else:
            self.gravity += 1 * self.gravity_strength
            self.rect.y += self.gravity

        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= 1200:
            self.rect.right = 1200
    

    def jump(self):
        if self.rect.bottom >= self.ground_level:
            self.gravity -= 20
            self.rect.y -= 10

    def damage_taken(self,incoming_damage,hitstun =0):
        if self.state == State.SHIELDING:
            self.shield_hits_remaining -= 1
            print(f"{self.char_name} shield hits left: {self.shield_hits_remaining}")
            if self.shield_hits_remaining <= 0:
                self.shield_hitbox = None
                self.change_state(State.SHIELD_BROKEN)
                print(f"{self.char_name} shield broke!")
            return

        if self.state == State.SHIELD_BROKEN:
            # No defense while stunned, take full damage
            self.health = max(0, self.health - incoming_damage)
            return

        damage = max(0, incoming_damage)
        self.health = max(0, self.health - damage)

        if hitstun > 0:
            self.hitstun_duration = hitstun
            self.change_state(State.HURT)

    def use_shield(self):
        if self.state != State.IDLE:
            return 
        self.shield_hits_remaining = 3
        self.shield_hitbox = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)
        self.change_state(State.SHIELDING)

    def apply_hitstun(self, duration=500):
        if self.state != State.SHIELD_BROKEN:
            self.hitstun_duration = duration           
            self.change_state(State.HURT)


    def punch(self,target):

        if self.state != State.IDLE:
            return None
        
        now = pygame.time.get_ticks()

        if now - self.state_start_time > self.combo_window:
            self.combo_count = 0

        if self.combo_count >= self.max_combo:
            return
        
        self.combo_count += 1
        self.last_hit_time = now
        self.change_state(State.ATTACKING)

        if self.facing == "right":
            self.punch_hitbox = self.punch_hitbox = pygame.Rect(self.rect.right, self.rect.centery - 20, 80, 40) 
        else:
            self.punch_hitbox = pygame.Rect(self.rect.left - 80, self.rect.centery - 20, 80, 40)

        if self.punch_hitbox and self.punch_hitbox.colliderect(target.rect):
            target.damage_taken(self.attack_mod * 10, hitstun=300)

    



