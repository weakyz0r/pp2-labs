import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("$$$nake")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
    
    def move(self):
        global score,speed,level
        head = self.body[0]
        x = (head[0] + self.direction[0]) % GRID_WIDTH
        y = (head[1] + self.direction[1]) % GRID_HEIGHT
        new_head = (x, y)
        if new_head in self.body[1:] or new_head in walls:
            return False
        self.body.insert(0, new_head)
        if new_head == food.position:
            if score % 2 == 0:  # Увеличение уровня каждые 3 еды
                level += 1
                speed += 1  # Увеличение скорости
            score += 1
            food.spawn()
        else:
            self.body.pop()
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.timer = 0 #Начальное значени таймера
        self.weights = [30, 40]  #Промежуток веса еды
        self.weight = 0  
        self.spawn()

    def spawn(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake.body and (x, y) not in walls:
                self.position = (x, y)
                self.timer = 120 #Сброс таймера при появлении новой еды
                self.weight = random.choice(self.weights) 
                break

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        if self.timer == 0 :
            self.spawn()  


walls = [(0, i) for i in range(GRID_HEIGHT)] + [(GRID_WIDTH - 1, i) for i in range(GRID_HEIGHT)] + \
        [(i, 0) for i in range(GRID_WIDTH)] + [(i, GRID_HEIGHT - 1) for i in range(GRID_WIDTH)]

snake = Snake()
food = Food()
score = 0
level = 0
speed = 10


clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))


    if not snake.move():
        running = False


    for segment in snake.body:
        pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def draw_food():
        x, y = food.position
        size = food.weight  
        pygame.draw.rect(screen, RED, pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, size, size))
        
        #Поедание еды
        head_x, head_y = snake.body[0]
        food_x, food_y = food.position
        if food_x < head_x < food_x + food.weight and food_y < head_y < food_y + food.weight:
            snake.body.append(snake.body[-1])  #Увеличение длины змеи
            food.spawn()



    
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Счет: {score}   Уровень: {level}", True, WHITE)
    screen.blit(text, (10, 10))
    draw_food()
    food.update()
    pygame.display.update()


    pygame.display.flip()

    clock.tick(10)
pygame.quit()
