import pygame, random

pygame.init()
width = 1024
height = 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hungry Lion')
clock = pygame.time.Clock()
points = 0
run = True


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center=(random.randint(100, 924), random.randint(100, 668)))
        self.image = pygame.image.load('icons/blue.png')

    def sliding(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.rect.centerx > 50:
            self.rect.move_ip(-5, 0)
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.rect.centerx < 974:
            self.rect.move_ip(5, 0)
        if pygame.key.get_pressed()[pygame.K_UP] and self.rect.centery > 50:
            self.rect.move_ip(0, -5)
        if pygame.key.get_pressed()[pygame.K_DOWN] and self.rect.centery < 718:
            self.rect.move_ip(0, 5)


class BadFood(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center=(random.randint(100, 924), 0))
        self.image = pygame.image.load('icons/red.png')
        self.speed = random.randint(2, 5)

    def sliding(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > height:
            self.rect = self.surf.get_rect(center=(random.randint(100, 924), 0))


class GoodFood(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center=(random.randint(100, 924), 718))
        self.image = pygame.image.load('icons/green.png')
        self.speed = random.randint(2, 5)

    def sliding(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < 0:
            self.rect = self.surf.get_rect(center=(random.randint(100, 924), 668))


player = Player()
red_list = list()
green_list = list()

B1 = BadFood()
B2 = BadFood()
B3 = BadFood()
B4 = BadFood()
B5 = BadFood()

red_list.append(B1)
red_list.append(B2)
red_list.append(B3)
red_list.append(B4)
red_list.append(B5)

G1 = GoodFood()
G2 = GoodFood()
G3 = GoodFood()
G4 = GoodFood()
G5 = GoodFood()

green_list.append(G1)
green_list.append(G2)
green_list.append(G3)
green_list.append(G4)
green_list.append(G5)

entities = pygame.sprite.Group()
bad_foods = pygame.sprite.Group()
good_foods = pygame.sprite.Group()
entities.add(player)

for i in red_list:
    entities.add(i)
    bad_foods.add(i)
for i in green_list:
    entities.add(i)
    good_foods.add(i)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    for entity in entities:
        entity.sliding()
        screen.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollide(player, bad_foods, dokill=True):
        points -= 1
    if pygame.sprite.spritecollide(player, good_foods, dokill=True):
        points += 1
    screen.blit(pygame.font.SysFont('times-new-roman', 24).render('Score:', True, (0, 0, 0)), (10, 15))
    screen.blit(pygame.font.SysFont('times-new-roman', 24).render(f'{points}', True, (0, 0, 0)), (70, 15))
    if B1 not in bad_foods:
        B1 = BadFood()
        bad_foods.add(B1)
        entities.add(B1)
    if B2 not in bad_foods:
        B2 = BadFood()
        bad_foods.add(B2)
        entities.add(B2)
    if B3 not in bad_foods:
        B3 = BadFood()
        bad_foods.add(B3)
        entities.add(B3)
    if B4 not in bad_foods:
        B4 = BadFood()
        bad_foods.add(B4)
        entities.add(B4)
    if B5 not in bad_foods:
        B5 = BadFood()
        bad_foods.add(B5)
        entities.add(B5)
    if G1 not in good_foods:
        G1 = GoodFood()
        good_foods.add(G1)
        entities.add(G1)
    if G2 not in good_foods:
        G2 = GoodFood()
        good_foods.add(G2)
        entities.add(G2)
    if G3 not in good_foods:
        G3 = GoodFood()
        good_foods.add(G3)
        entities.add(G3)
    if G4 not in good_foods:
        G4 = GoodFood()
        good_foods.add(G4)
        entities.add(G4)
    if G5 not in good_foods:
        G5 = GoodFood()
        good_foods.add(G5)
        entities.add(G5)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
