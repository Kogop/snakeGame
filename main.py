import pygame
import sys
import random

# Game constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10
FOOD_SPAWN_RATE = 100

# Game variables
snake = [(200, 200), (220, 200), (240, 200)]  # initial snake position # snake's head is last one, snake starts from end of tuple
direction = 'RIGHT'  # initial direction
food = (400, 300)  # initial food position
score = 0


def draw_game():
    """Draws the game state on the screen"""
    screen.fill((0, 0, 0))  # clear screen
    for x, y in snake:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()


def move_snake():
    """Moves the snake based on the current direction"""

    head = snake[-1]  #take last element(it's head)
    if direction == 'UP':
        new_head = (head[0], head[1] - BLOCK_SIZE) # (x,y-1) less on top so less y = going top
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == 'LEFT':
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + BLOCK_SIZE, head[1])
    #first new head is added
    snake.append(new_head)
    global food
    #then if new_head did touch the food
    if snake[-1] == food:
        global score
        score += 1 #score gets up
        #and new food randomly spawns
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop(0) #if new head didn't touch the food then snakes tail gets cut off


def check_collision():
    """Checks if the snake has collided with the edge or itself"""
    head = snake[-1]
    if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake[:-1]):
        return True
    return False


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        move_snake()
        if check_collision():
            print(f'Game Over! Final Score: {score}')
            pygame.quit()
            sys.exit()
        draw_game()
        clock.tick(SPEED)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
