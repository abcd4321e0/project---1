import pygame
import random

pygame.init()

# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width = 900
screen_height = 600

#creating windows
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Game Title
pygame.display.set_caption("snake game")
pygame.display.update()

#game specific variavles
exit_game = False
game_over = False

#snake size and direction
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

#make food of snake
food_x = random.randint(20, 700)
food_y = random.randint(20, 400)
#score
score = 0
#snake ki speed ko slow kaise kare
init_velocity = 5
snake_size = 30
fps = 60

#snake speed per second
clock = pygame.time.Clock()

#Score ko windows par kaisse laye
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

#snake length increase

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

snk_list = []
snk_length = 1




#game loop
while not exit_game:
    for event in pygame.event.get():
    

# Cut a Game
        if event.type == pygame.QUIT:
            exit_game = True

#Move snake  to keyboards
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                #not move diognol
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                #not move daigonal
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                #not move daigonal
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                #not move daigonal
                velocity_x = 0

# Do not stop snake
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    #snake ko food kaise khilaye and score kaisse print kare
    if abs(snake_x - food_x)<29 and abs(snake_y - food_y)<29:
            score +=1
            food_x = random.randint(0, 700)
            food_y = random.randint(0, 400)
            #snake length
            snk_length +=5




#Color fill in Windows
    gameWindow.fill(white)

    #food for snake gamewindow ke uper banao food varana food white window ke niche chala jayega
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

    #snake lingth increase
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    #snake ki size lagatal badhane se kaise roke
    if len(snk_list)>snk_length:
        del snk_list[0]

    # Score in game window
    text_screen("Score: "+ str(score * 10), red, 5, 5)

    #drow snake
    #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    plot_snake(gameWindow, black, snk_list,  snake_size)
    pygame.display.update()


    #speed of snake frame per second
    clock.tick(fps)

pygame.quit()
quit()



