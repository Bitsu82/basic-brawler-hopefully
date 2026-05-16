import pygame,sys,time
from enum import Enum

# All possible states a character can be in

class State(Enum):
    IDLE = "idle"
    SHIELDING = "shielding"
    SHIELD_BROKEN = "shield_broken"
    ATTACKING = "attacking"
    HURT = "hurt"

class PlayerCharacter(pygame.sprite.Sprite):
    def __init__(self, char_name, image_path, x, y, groups):
        super().__init__(groups)

        self.char_name = char_name
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))#image loading and starting position
        self.max_health = 100
        self.health = self.max_health#boring health stuff
        self.gravity = 0 
        self.gravity_strength = 1 #boring gravity stuff
        self.ground_level = 700 # where the floor is
        self.attack_mod = 1.0# cuz this is the parent class it is one but it is an attack mult
        self.state = State.IDLE # starting tate is doing nothing
        self.state_start_time = 0 #we need a starting point for the later states to ovveride so we just bs one
        self.shield_hits_remaining = 2 #max hits of the shield basically
        self.SHIELD_DURATION = 4000      # 4 seconnds for how long the shield will live
        self.SHIELD_BREAK_ENDLAG = 3000  # 3 seconds of endlag once the shield breaks


    def update(self):
        self.grav()
        self.state_check_timers()

    def state_check_timers(self):
        elapsed = self.pygame.time.get_ticks() - self.state_start_time
        if elapsed <= self.SHIELD_DURATION:
            #i dont want a punishment for when the timer on the shield runs out sue me
            self.change_state(State.IDLE)

    def change_state(self,new_state):
        self.state = new_state
        self.state_start_time = pygame.time.get_ticks()

    def grav(self):
        if self.rect.bottom < self.ground_level: 
            self.gravity += 1 * self.gravity_strength
            self.rect.y += self.gravity
        if self.rect.bottom >= self.ground_level:
            self.rect.bottom = self.ground_level
            self.gravity = 0

    def damage_taken(self,incoming_damage):
        if self.State == State.SHIELDING:
            self.shield_hits_remaining -= 1
            if self.shield_hits_remaining <= 0:
                self.state = State.SHIELD_BROKEN
            return

        if self.state == State.SHIELD_BROKEN:
            # No defense while stunned, take full damage
            self.health = max(0, self.health - incoming_damage)
            return

        damage = max(0, incoming_damage)
        self.health = max(0, self.health - damage)

    def use_shield(self):
        if self.state != State.IDLE:
            return 
        self.shield_hits_remaining = 2
        self.change_state(State.SHIELDING)

    def hitstun(self, duration=500):
        if self.state != State.SHIELD_BROKEN:
            self.change_state(State.HURT)
            self.hitstun_duration = duration
            self.state_start_time = pygame.time.get_ticks()

    def punch(self):
        if self.state != State.IDLE:
            return None
        self.change_state(State.ATTACKING)
        return self.attack_mod * 10

    
    def kick(self):
        if self.state != State.IDLE:
            return None
        self.change_state(State.ATTACKING)
        return self.attack_mod * 15


