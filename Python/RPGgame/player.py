import pygame
import os

from inventory import Inventory

class Player(pygame.sprite.Sprite):
    def __init__(self,**kwargs):
        pygame.sprite.Sprite.__init__(self)

        # moving frames
        self.idle_frames_left = []
        self.idle_frames_right = []
        self.walking_frames_left = []
        self.walking_frames_right = []
        self.prepare_for_jump_left = []
        self.prepare_for_jump_right = []
        self.fall_jump_left = []
        self.fall_jump_right = []



        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.is_jumping, self.on_ground, self.falling = False, False, False
        self.gravity, self.friction = .35, -.12
        self.position, self.velocity = pygame.math.Vector2(500,750), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)
        self.load_frames()
        self.rect = self.idle_frames_right[0].get_rect()
        self.left_border, self.right_border = 250, 850
        self.last_updated = 0
        self.current_frame = 0
        self.state = 'idle'
        self.current_image = self.idle_frames_right[0]

        self.inventory = Inventory()

    def draw(self, display):
        display.blit(self.current_image, (self.rect.x, self.rect.y))

    def load_frames(self):

        #idle
        for frame in range(4):
            img = pygame.transform.scale(
                pygame.image.load(os.path.join('assets',f'adventurer-idle-0{str(frame)}.png')),(100,100))
            self.idle_frames_right.append(img)

        for frame in self.idle_frames_right:
            self.idle_frames_left.append(pygame.transform.flip(frame,True, False))

        #walking / run
        for frame in range(5):
            img = pygame.transform.scale(
                pygame.image.load(os.path.join('assets', f'adventurer-run-0{str(frame)}.png')), (100, 100))
            self.walking_frames_right.append(img)

        for frame in self.walking_frames_right:
            self.walking_frames_left.append(pygame.transform.flip(frame, True, False))

        #jumping
        for frame in range(4):
            img = pygame.transform.scale(
                pygame.image.load(os.path.join('assets', f'adventurer-jump-0{str(frame)}.png')), (100, 100))
            self.prepare_for_jump_right.append(img)

        for frame in self.prepare_for_jump_right:
            self.prepare_for_jump_left.append(pygame.transform.flip(frame, True, False))

        #falling
        for frame in range(2):
            img = pygame.transform.scale(
                pygame.image.load(os.path.join('assets', f'adventurer-fall-0{str(frame)}.png')), (100, 100))
            self.fall_jump_right.append(img)

        for frame in self.fall_jump_right:
            self.fall_jump_left.append(pygame.transform.flip(frame, True, False))


    def update(self,dt,display):
        self.horizontal_movement(dt)
        self.vertical_movement(dt,display)

    def horizontal_movement(self, dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .3
        elif self.RIGHT_KEY:
            self.acceleration.x += .3
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(4)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x

        self.animate()
        self.set_state()

    def vertical_movement(self, dt,display):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7: self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        if self.velocity.y >= 2:
            self.falling = True
        if self.position.y > display.get_height()-50:
            self.on_ground = True
            self.falling = False
            self.velocity.y = 0
            self.position.y = display.get_height()-50
        self.rect.bottom = self.position.y

        self.animate()
        self.set_state()

    def limit_velocity(self, max_vel):
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 8
            self.on_ground = False
            self.falling = False

    def set_state(self):
        self.state = 'idle'
        if self.velocity.x < 0:
            self.state = 'moving left'
        elif self.velocity.x > 0:
            self.state = 'moving right'
        elif self.is_jumping and self.FACING_LEFT:
            self.state = 'jumping left'
        elif self.is_jumping and not self.FACING_LEFT:
            self.state = 'jumping right'
        elif self.falling and self.FACING_LEFT:
            self.state = 'falling left'
        elif self.falling and not self.FACING_LEFT:
            self.state = 'falling right'


    def animate(self):
        now = pygame.time.get_ticks()
        if self.state == 'idle':
            if now - self.last_updated > 200:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_right)
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif not self.FACING_LEFT:
                    self.current_image = self.idle_frames_right[self.current_frame]

        else:
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_left)
                if self.state == 'moving left':
                    self.current_image = self.walking_frames_left[self.current_frame]
                elif self.state == 'moving right':
                    self.current_image = self.walking_frames_right[self.current_frame]
                elif self.state == 'jumping left':
                    self.current_frame = (self.current_frame + 1) % len(self.prepare_for_jump_left)
                    self.current_image = self.prepare_for_jump_left[self.current_frame]
                elif self.state == 'jumping right':
                    self.current_frame = (self.current_frame + 1) % len(self.prepare_for_jump_right)
                    self.current_image = self.prepare_for_jump_right[self.current_frame]
                elif self.state == 'falling left':
                    self.current_frame = (self.current_frame + 1) % len(self.fall_jump_left)
                    self.current_image = self.fall_jump_left[self.current_frame]
                elif self.state == 'falling right':
                    self.current_frame = (self.current_frame + 1) % len(self.fall_jump_right)
                    self.current_image = self.fall_jump_right[self.current_frame]

    def collision(self,object):
        pass

