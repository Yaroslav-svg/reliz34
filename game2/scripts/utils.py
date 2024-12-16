#підключення модуля що дозволяє працювати з файловою системою
import os

import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):#функція що завантажує зображення за заданим шляхом і повертає його в форматі Pygame Surface
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))#встановлює колор ключ для прозорості (чорний колiр)
    return img

#функцiя load_images завантажує набiр зображень з папки за заданим шляхом
#вона повертає список Pygame Surface, як i результат роботи функцii load_image()
def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images
#цей клас являє собою анімацію на основі списку зображень
#сюди передається список зображень
class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images #сюди передається список зображень
        self.loop = loop #сюди скупченність
        self.img_duration = img_dur #а сюди швидкість переключання кадрів
        self.done = False
        self.frame = 0
    
    def copy(self):#метод copy створює новий екземпляp клacy Animation 
        return Animation(self.images, self.img_duration, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
    
    def img(self):#метод img повepтає поточне зображення
        return self.images[int(self.frame / self.img_duration)]