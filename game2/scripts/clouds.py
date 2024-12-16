import random #підключення модуля що дозволяє генерувати випадкові числа

class Cloud: #створення класу хмари, що визначає такі параметри як: 
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos) #позиція хмари
        self.img = img #зображення хмари
        self.speed = speed #швидкість хмари
        self.depth = depth # наскільки далеко хмара знаходиться
    
    def update(self):
        self.pos[0] += self.speed #швидкість хмари
        
    def render(self, surf, offset=(0, 0)):
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))
        
class Clouds: #цей клас створює список об'єктів Cloud як свій атрибут і приймає список зображень хмар і кількость для визначення кількостi створених хмар.
    def __init__(self, cloud_images, count=16):# у цьому методі створюються декiлька екземплярiв Cloud з випадковими позицiями, швидкостями, глибинами
        self.clouds = []
        
        for i in range(count):
            self.clouds.append(Cloud((random.random() * 99999, random.random() * 99999), random.choice(cloud_images), random.random() * 0.05 + 0.05, random.random() * 0.6 + 0.2))
        
        self.clouds.sort(key=lambda x: x.depth)
    
    def update(self): #метод що оновлює позицію кожної хмари
        for cloud in self.clouds:
            cloud.update()
    
    def render(self, surf, offset=(0, 0)): #цей метод наносить хмари на дану поверхню
        for cloud in self.clouds:
            cloud.render(surf, offset=offset)