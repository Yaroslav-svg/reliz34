class Particle: #клас для створення та оновлення частинок у грі що має такі атрибути
    def __init__(self, game, p_type, pos, velocity=[0, 0], frame=0):
        self.game = game #посилання на об'єкт у грі
        self.type = p_type #вид частинки
        self.pos = list(pos) #позиція частинок
        self.velocity = list(velocity) #швидкість частинок
        self.animation = self.game.assets['particle/' + p_type].copy()
        self.animation.frame = frame
    
    def update(self):#метод update оновлює позицію чaстинки шляхом додавань self.velocity до поточного значення координат x i y.
        kill = False
        if self.animation.done:
            kill = True
        
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        
        self.animation.update()
        
        return kill
    
    def render(self, surf, offset=(0, 0)):#метод render отpимyє точне зображення self.animation.img() і наносить його на поверхню
        img = self.animation.img()
        surf.blit(img, (self.pos[0] - offset[0] - img.get_width() // 2, self.pos[1] - offset[1] - img.get_height() // 2))
    