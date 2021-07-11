import abc

import pygame
import os

class Storage():
    def __init__(self):
        self.storage = []

    def load_assets(self):
        for frame in range(1):
            img = pygame.transform.scale(
                pygame.image.load(os.path.join('assets', f'sword-level-0{str(frame+1)}.png')), (80, 80))
            self.storage.append(img)