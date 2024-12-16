import math #підключення модуля що забезпечує доступ до математичних функцій

import pygame

class Spark: #клас Spark, що створю та оновлює спалахи у грі та має атрибути - швидкість, кут нахилу та позиція
    def __init__(self, pos, angle, speed):#метод __init__ класу Spark інiцiалiзуються початковою позицією, кутом та швидкістю.
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed
        
    def update(self):#цей метод оновлює позицію спалаху за формулою відносно координат х та у
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed
        
        self.speed = max(0, self.speed - 0.1)
        return not self.speed
    
    def render(self, surf, offset=(0, 0)):#метод render отpимyє точне зображення самoго об'єктa за допомогою команди pygame.draw.polygon()
        render_points = [
            (self.pos[0] + math.cos(self.angle) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle + math.pi * 0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle + math.pi * 0.5) * self.speed * 0.5 - offset[1]),
            (self.pos[0] + math.cos(self.angle + math.pi) * self.speed * 3 - offset[0], self.pos[1] + math.sin(self.angle + math.pi) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle - math.pi * 0.5) * self.speed * 0.5 - offset[0], self.pos[1] + math.sin(self.angle - math.pi * 0.5) * self.speed * 0.5 - offset[1]),
        ]
        
        pygame.draw.polygon(surf, (255, 255, 255), render_points)