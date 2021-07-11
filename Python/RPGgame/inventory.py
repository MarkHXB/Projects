import pygame
import os

from gameVector import PyVector
from storage import Storage

class Inventory():
    def __init__(self,**kwargs):
        self.primary = 1
        self.equipments = []
        self.max_slots = 4

        #loaded assets / items this will be moved to other class like a storage
        self.storage = Storage().storage

        #player
        self.player_inventory = []

    def give_sword(self):
        self.equipments.append(self.storage[0])

    def draw(self,display):
        item_bar = pygame.Surface((300, 150))
        item_bar.set_alpha(128)
        item_bar.fill((50,50,50))

        m_x = 0
        for slot in range(self.max_slots):
            slot = pygame.Surface((70, 70))
            slot.set_alpha(64)
            slot.fill((0,0,0))
            item_bar.blit(slot,(m_x,item_bar.get_height() // 2 - slot.get_height() / 2))
            m_x += 75

        display.blit(item_bar,(display.get_width() - item_bar.get_width() -10, display.get_height() - item_bar.get_height() - 10))

    def update(self,display):
        pass


