import pygame

class GameObject():
    def __init__(self, image, speed) -> None:
        self.image = image
        self.speed = speed
        self.movex = image.get_rect().right
        self.movey = image.get_rect().left
    def control(self):
        