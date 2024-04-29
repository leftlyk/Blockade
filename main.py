import pygame
import time
from Grid import Grid
from moves import next_to, find_location, swap, move_cb
from SolutionGrid import SolutionGrid

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (in pixels)
#WIDTH, HEIGHT = 800, 510
WIDTH, HEIGHT = 1500, 510

# Set the number of rows and columns in the grid
ROWS, COLS = 5, 5

# Set the size of each cell in the grid
CELL_SIZE = WIDTH // COLS

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")

group = pygame.sprite.RenderPlain()

g1 = Grid(0, 0, screen, group)
print("Grid:",g1.grid)
# Shuffle the grid
g1.shuffle_grid()
# Update the positions of the color blocks
g1.update_positions()

g2 = Grid(800, 0, screen, group)
print("Grid:",g1.grid)
# Shuffle the grid
g2.shuffle_grid()
# Update the positions of the color blocks
g2.update_positions()


s1 = SolutionGrid(610,100,screen,group)
s1.populate_solutions()
solution_grid = s1.grid

def draw_game_over_screen(time_elapsed):
   screen.fill((30, 30, 30))
   win_string = 'Game over, Player ' + str(winner) + ' wins! \n Time to solve: ' + str(time_elapsed)
   font = pygame.font.SysFont('Oxygen-Regular.ttf', 80)
   title = font.render(win_string, True, (255, 255, 255))
   restart_button = font.render('R - Restart', True, (255, 255, 255))
   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/3))
   screen.blit(restart_button, (WIDTH/2 - restart_button.get_width()/2, HEIGHT/1.9 + restart_button.get_height()))
   screen.blit(quit_button, (WIDTH/2 - quit_button.get_width()/2, HEIGHT/2 + quit_button.get_height()/2))
   pygame.display.update()

def string_representation(grid):
    str_rep = [[0 for x in range(len(grid))] for y in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is None:
                return None
            str_rep[i][j] = grid[i][j].colour
    return str_rep

winner = None
def check_win():
    global winner
    middle_grid_p1 = string_representation([row[1:4] for row in g1.grid[1:4]])
    middle_grid_p2 = string_representation([row[1:4] for row in g2.grid[1:4]])
    solution = string_representation(solution_grid)

    if middle_grid_p1 is not None and middle_grid_p1 == solution:
        winner = 1
        print("P1 wins!")
        return True
    if middle_grid_p2 is not None and middle_grid_p2 == solution:
        print("P2 wins!")
        winner = 2
        return True

    return False

global start
global end
start = None
end = None

# Main loop
running = True
won = False
while running:

    events = pygame.event.get()
    # Check for events
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            if start is None:
                start = time.time()
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        list_keys_arrows = [pygame.K_LEFT, pygame.K_RIGHT,
                            pygame.K_UP, pygame.K_DOWN]
        list_keys_wasd = [ord('a'), ord('d'),
                          ord('w'), ord('s')]
        num_pressed_wasd = [keys[i] for i in list_keys_wasd]
        num_pressed_wasd = len([ i for i in num_pressed_wasd if i != False])
        num_pressed_arrows = [keys[i] for i in list_keys_arrows]
        num_pressed_arrows = len([i for i in num_pressed_arrows if i != False])
        print(num_pressed_wasd)
        '''
        if event.type == pygame.KEYDOWN and num_pressed_arrows == 1:
            if keys[pygame.K_LEFT]:
                move_cb('left', g2)
            elif keys[pygame.K_RIGHT]:
                move_cb('right', g2)
            elif keys[pygame.K_UP]:
                move_cb('up', g2)
            elif keys[pygame.K_DOWN]:
                move_cb('down', g2)

        if event.type == pygame.KEYDOWN and num_pressed_wasd == 1:
            if keys[ord('a')]:
                move_cb('left', g1)
            elif keys[ord('d')]:
                move_cb('right', g1)
            elif keys[ord('w')]:
                move_cb('up', g1)
            elif keys[ord('s')]:
                move_cb('down', g1)
        '''
        if event.type == pygame.KEYDOWN:
            if num_pressed_arrows ==1:
                if event.key == pygame.K_LEFT:
                    move_cb('left', g2)
                elif event.key == pygame.K_RIGHT:
                    move_cb('right', g2)
                elif event.key == pygame.K_UP:
                    move_cb('up', g2)
                elif event.key == pygame.K_DOWN:
                    move_cb('down', g2)
            if num_pressed_wasd ==1:
                if event.key == ord('a'):
                    move_cb('left', g1)
                elif event.key == ord('d'):
                    move_cb('right', g1)
                elif event.key == ord('w'):
                    move_cb('up', g1)
                elif event.key == ord('s'):
                    move_cb('down', g1)

        if check_win():
            if end is None:
                end = time.time()
            won = True

    # Clear the screen
    screen.fill(color=(30, 30, 30))

    # Update the display
    group.update(events)
    group.draw(screen)

    if won:
        draw_game_over_screen(end - start)

    pygame.display.update()

# Quit Pygame
pygame.quit()

# feedback: drag, arrows, click; splitscreen multiplayer
