import pygame
import time
from Grid import Grid
from moves import next_to, find_location, swap, move_cb
from SolutionGrid import SolutionGrid

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (in pixels)
WIDTH, HEIGHT = 800, 510

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


s1 = SolutionGrid(0,0,screen,group)
s1.populate_solutions()
solution_grid = s1.grid


def check_win():
    middle_grid = [row[1:4] for row in g1.grid[1:4]]
    for i in range(len(solution_grid)):
        for j in range(len(solution_grid[i])):
            if middle_grid[i][j] is None:
                return False
            elif not (middle_grid[i][j].colour == solution_grid[i][j].colour):
                return False
    print("you won!")
    return True


# Main loop
running = True
while running:
    not_won = True
    events = pygame.event.get()
    # Check for events
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            start = time.time()
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            move_cb('left', g1)
        if keys[pygame.K_RIGHT]:
            move_cb('right', g1)
        if keys[pygame.K_UP]:
            move_cb('up', g1)
        if keys[pygame.K_DOWN]:
            move_cb('down', g1)

        if check_win():
            end = time.time()
            not_won = False

    # Clear the screen
    screen.fill(color=(30, 30, 30))

    # Update the display
    group.update(events)
    group.draw(screen)
    pygame.display.update()

# Quit Pygame
pygame.quit()

# feedback: drag, arrows, click; splitscreen multiplayer
