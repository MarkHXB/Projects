import pygame
import os
import random

WIDTH = 40
HEIGHT = 40
APPLE_SIZE = (WIDTH,HEIGHT)

FOOD_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets','food.png')),APPLE_SIZE)

class Food():
    def __init__(self,screen):
        self.img = FOOD_IMG
        self.rect = self.get_random_position()
        self.live = False

    def get_random_position(self):
        new_x = random.randrange(20, 780, 2)
        new_y = random.randrange(20, 780, 2)
        rect = pygame.Rect((new_x,new_y),APPLE_SIZE)
        return rect

    def update(self,screen):
        screen.blit(self.img,self.rect)

    def generate_new_food(self):
        self.rect = self.get_random_position()

    def collision(self,snake,screen):
        if snake.head.colliderect(self.rect):
            self.generate_new_food()
            snake.extend(screen)