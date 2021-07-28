import pygame
import random
import json
import os
  
pygame.init()
screen = pygame.display.set_mode((800, 600))

#rand choose level 
f = open(f'wall{random.randint(1,2)}.txt', 'r')
lines = f.readlines()
print(lines)
wx = 0
wy = 0
walls_list = []
 
for i in lines:
    for j in i:
        if(j == '#'):
            walls_list.append([wx*10,wy*10])
        wx+=1
    wx = 0
    wy += 1

#walls 
class Wall:
    def __init__(self, walls):
        self.walls = walls
    def draw(self):
        for i in self.walls:
            px = i[0]
            py = i[1]
            pygame.draw.rect(screen, (255, 105, 255), (px, py, 5, 5))
 
#food
class Food:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
    def gen(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
    def draw(self):
        pygame.draw.rect(screen, (105, 255, 105), (self.x, self.y, 15, 15))
 
#snake 
class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 10
        self.dx = 5  # right
        self.dy = 0
        self.is_add = False
        self.speed = 30
    def load(self, data):
        self.size = data["size"]
        self.elements = data['elements']
        self.radius = data['radius']
        self.dx = data['dx']
        self.dy = data['dy']
        self.is_add = data['is_add']
        self.speed = data['speed']
 
    # [x1, y1], [x2, y2], [x3, y3], [x3, y3], [x4, y4] i -> i - 1
 
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 255, 0), element, self.radius)
    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 3 == 0:
            self.speed += 10
    def move(self):
        if self.is_add:
            self.add_to_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
            return True
        return False
    def collision(self, walls):
        x = self.elements[0][0]
        y = self.elements[0][1]
 
        for i in walls:
            if i[0] <= x <= i[0] + 10 and i[1] <= y <= i[1] + 10:
                return True
        return False
 
is_saved = False
try:
    saved = open('save.json','r')
    is_saved = True
except:
    is_saved = False
 
snake1 = None
#snake2 = None
if is_saved:
    ssn1 = open('save.json', 'r')
    ssn1data = ssn1.read()
    ssn1data = json.loads(ssn1data)
    snake1 = Snake(30, 30)
    snake1.load(ssn1data["snake1"])
    #snake2 = Snake(30, 30)
    #snake2.load(ssn1data["snake2"])
else:
    snake1 = Snake(100, 100)
    #snake2 = Snake(150, 100)

food = Food()
walls = Wall(walls_list)
running = True
d = 5
FPS = 30
 
clock = pygame.time.Clock()
 
while running:
    clock.tick(snake1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            """if event.key == pygame.K_d and snake2.dx != -d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a and snake2.dx != d:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w and snake2.dy != d:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s and snake2.dy != -d:
                snake2.dx = 0
                snake2.dy = d"""
 
            if event.key == pygame.K_SPACE:
                saved_game = {}
                saved_game["snake1"] = {
                    'size' : snake1.size,
                    'elements' : snake1.elements,
                    'radius' : snake1.radius,
                    'dx' : snake1.dx,
                    'dy' : snake1.dy,
                    'is_add' : snake1.is_add,
                    'speed' : snake1.speed
                }
                """saved_game["snake2"] = {
                    'size': snake2.size,
                    'elements': snake2.elements,
                    'radius': snake2.radius,
                    'dx': snake2.dx,
                    'dy': snake2.dy,
                    'is_add': snake2.is_add,
                    'speed': snake2.speed
                }"""
                data = json.dumps(saved_game)
                f = open('save.json', 'w')
                f.write(data)
                f.close()
                running = False
 
    if snake1.eat(food.x, food.y):
        snake1.is_add = True
        food.gen()
    """if snake2.eat(food.x, food.y):
        snake2.is_add = True
        food.gen()"""
    
    if snake1.collision(walls_list):
        running = False
 
    snake1.move()
    #snake2.move()
    screen.fill((0, 0, 0))
    snake1.draw()
    #snake2.draw()
    food.draw()
    walls.draw()
    pygame.display.flip()
 
pygame.quit()