import pygame.sprite
import os
import random

from gameVector import PyVector


class Sky(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.clouds = []

        #position
        self.stat_pos_x = [0,950]
        self.stat_pos_y = [0,200]

        #size
        self.stat_size_max_x = 200
        self.stat_size_max_y = 100
        self.stat_size_min_x = 100
        self.stat_size_min_y = 50

        #count
        self.stat_max_clouds = 5

        #initialize the clouds when the game starts
        self.load_asset()
        self.initialize_position()


    def new_pos_x(self):
        new_x = random.randint(self.stat_pos_x[0],self.stat_pos_x[1])
        return new_x

    def new_pos_y(self):
        new_y = random.randint(self.stat_pos_y[0],self.stat_pos_y[1])
        return new_y

    def new_size(self):
        new_x = random.randint(self.stat_size_min_x,self.stat_size_max_x)
        new_y = random.randint(self.stat_size_min_y,self.stat_size_max_y)
        size = (new_x, new_y)
        return size

    def load_asset(self):
        for frame in range(3):
            img = pygame.transform.scale(pygame.image.load(os.path.join('assets',f'cloud-0{str(frame + 1)}.png')),(self.new_size()))
            self.images.append(img)

    def initialize_position(self):
        for image in self.images:
            cloud = PyVector(img=image,x=self.new_pos_x(),y=self.new_pos_y())
            self.clouds.append(cloud)

    def draw(self,display):
        for cloud in self.clouds:
            display.blit(cloud.surface,(cloud.x,cloud.y))

class Ground(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 50
        self.x = 0
        self.y = 0
        self.img = None
        self.load_asset()

    def load_asset(self):
        self.img = pygame.transform.scale(pygame.image.load(os.path.join('assets','wall.png')),(self.width,self.height))

    def draw(self, display):
        s_width = display.get_width()
        ground_count = s_width // self.width
        ground_pos = 0
        for ground_piece in range(ground_count):
            display.blit(self.img, (ground_pos, display.get_height() - 50))
            ground_pos += self.width