import pygame
import random

pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake properties
snake_block = 20
snake_speed = 15

# Snake function
def our_snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])

# Main function to run the game
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    snake_list = []
    snake_length = 1
    snake_x, snake_y = screen_width // 2, screen_height // 2
    snake_change_x, snake_change_y = 0, 0

    # Food position
    food_x, food_y = round(random.randrange(0, screen_width - snake_block) / 20) * 20, round(random.randrange(0, screen_height - snake_block) / 20) * 20

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(white)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            screen.blit(message, (screen_width // 6, screen_height // 3))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_change_x = -snake_block
                    snake_change_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake_change_x = snake_block
                    snake_change_y = 0
                elif event.key == pygame.K_UP:
                    snake_change_y = -snake_block
                    snake_change_x = 0
                elif event.key == pygame.K_DOWN:
                    snake_change_y = snake_block
                    snake_change_x = 0

        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_close = True

        snake_x += snake_change_x
        snake_y += snake_change_y
        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = round(random.randrange(0, screen_width - snake_block) / 20) * 20, round(random.randrange(0, screen_height - snake_block) / 20) * 20
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
