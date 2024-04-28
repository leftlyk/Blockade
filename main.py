import pygame
import time

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

array = [
    ['red', 'red', 'red', 'red', 'white'],
    ['green', 'green', 'green', 'green' , 'white'],
    ['yellow', 'yellow', 'yellow', 'yellow', 'white'],
    ['blue', 'blue', 'blue', 'blue', 'white'],
    ['orange', 'orange', 'orange', 'orange']
]

colour_dict = {
    'blue': (84,173,211),
    'green': (137, 195, 110),
    'red': (211, 84, 84),
    'yellow': (228, 192, 64),
    'orange': (216, 133, 73),
    'white': (251, 248, 248)
}

class smallColourBlock(pygame.sprite.Sprite):
    def __init__(self, colour, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width = 20
        self.height = 20
        self.area = screen.get_rect()
        self.colour = colour
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class colourBlock(pygame.sprite.Sprite):
    def __init__(self, colour, x, y, callback):
        pygame.sprite.Sprite.__init__(self)
        self.width = 90
        self.height = 90
        self.area = screen.get_rect()
        self.colour = colour
        self.callback = callback
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback(self, 'clicked')


    def updatePoints(self, x, y):
        print("points updated.")
        self.rect.x = x
        self.rect.y = y
    def getColour(self):
        return self.colour

group = pygame.sprite.RenderPlain()

grid = [
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None]
]

solutionGrid = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

def on_click(thingy, action):
    print("clicked")
    if action == 'clicked':
        clicked = find_location(grid, thingy)
        blank = find_location(grid, None)
        if nextTo(clicked, blank):
            swap(clicked, blank)

x = 10
y = 10
for i in range(len(array)):
    for j in range(len(array[i])):
        cb = colourBlock(colour=colour_dict[array[i][j]], x=x, y=y, callback=on_click)
        group.add(cb)
        grid[i][j] = cb
        x += 100
    x = 10
    y += 100

def nextTo(l1, l2):
    l1_row = l1[0]
    l1_col = l1[1]
    l2_row = l2[0]
    l2_col = l2[1]
    if (((l1_row == l2_row) and ((l1_col == (l2_col + 1)) or (l1_col == (l2_col - 1)))) or
            ((l1_col == l2_col) and ((l1_row == (l2_row + 1)) or (l1_row == (l2_row - 1))))):
        return True
    return False

def find_location(grid, item):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == item:
                return (i,j)

def swap(l1, l2):
    print(grid)
    l1_row = l1[0]
    l1_col = l1[1]
    l2_row = l2[0]
    l2_col = l2[1]
    grid[l1_row][l1_col], grid[l2_row][l2_col] = grid[l2_row][l2_col], grid[l1_row][l1_col]
    print(grid)
    update_positions(grid)

def check_win():
    middle_grid = [row[1:4] for row in grid[1:4]]
    for i in range(len(solutionGrid)):
        for j in range(len(solutionGrid[i])):
            if middle_grid[i][j] is None:
                return False
            elif not (middle_grid[i][j].colour == solutionGrid[i][j].colour):
                return False
    print("you won!")
    return True

def update_positions(grid):
    x = 10
    y = 10
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is not None:
                grid[i][j].updatePoints(x, y)
            else:
                x += 100
                continue
            x += 100
        x = 10
        y += 100


print(grid)

import random


def shuffle_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Get random neighbor
            rand_i = random.randint(max(0, i - 1), min(len(grid) - 1, i + 1))
            rand_j = random.randint(max(0, j - 1), min(len(grid[i]) - 1, j + 1))

            # Swap color blocks
            grid[i][j], grid[rand_i][rand_j] = grid[rand_i][rand_j], grid[i][j]


# Shuffle the grid
shuffle_grid(grid)

# Update the positions of the color blocks
update_positions(grid)


def populate_solutions():
    x = 700
    y = 10
    list_choices = ['blue', 'green', 'red', 'white', 'yellow', 'orange']
    counts = {'blue': 0, 'green': 0, 'red': 0, 'white': 0, 'yellow': 0, 'orange': 0}
    for i in range(len(solutionGrid)):
        for j in range(len(solutionGrid[i])):
            colour = random.choice(list_choices)
            counts[colour] += 1
            if counts[colour] == 4:
                list_choices.remove(colour)
            scb = smallColourBlock(colour = colour_dict[colour], x=x, y=y)
            group.add(scb)
            solutionGrid[i][j] = scb
            x += 30
        x = 700
        y += 30

populate_solutions()

def moveCB(action):
    blank = find_location(grid, None)
    dict = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if nextTo((i, j), blank):
                if j == blank[1] and i == blank[0] - 1:
                    dict['down'] = (i,j)
                elif j == blank[1] and i == blank[0] + 1:
                    dict['up'] = (i,j)
                elif i == blank[0] and j == blank[1] - 1:
                    dict['right'] = (i,j)
                elif i == blank[0] and j == blank[1] + 1:
                    dict['left'] = (i,j)

    if action == 'left' and 'left' in dict.keys():
        swap(dict['left'], blank)
    elif action == 'right' and 'right' in dict.keys():
        swap(dict['right'], blank)
    elif action == 'up' and 'up' in dict.keys():
        swap(dict['up'], blank)
    elif action == 'down' and 'down' in dict.keys():
        swap(dict['down'], blank)

    update_positions(grid)


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
            moveCB('left')
        if keys[pygame.K_RIGHT]:
            moveCB('right')
        if keys[pygame.K_UP]:
            moveCB('up')
        if keys[pygame.K_DOWN]:
            moveCB('down')

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
