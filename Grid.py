import random
from ColourBlock import ColourBlock
from click import on_click
class Grid():

    def __init__(self, x, y, screen, group):
        self.array = [
            ['red', 'red', 'red', 'red', 'white'],
            ['green', 'green', 'green', 'green', 'white'],
            ['yellow', 'yellow', 'yellow', 'yellow', 'white'],
            ['blue', 'blue', 'blue', 'blue', 'white'],
            ['orange', 'orange', 'orange', 'orange']
        ]

        self.colour_dict = {
            'blue': (84, 173, 211),
            'green': (137, 195, 110),
            'red': (211, 84, 84),
            'yellow': (228, 192, 64),
            'orange': (216, 133, 73),
            'white': (251, 248, 248)
        }

        self.grid = [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]

        self.x = x
        self.y = y
        self.screen = screen
        self.group = group

        self.populate(self.group, self.array, self.colour_dict, self.screen, self.grid)


    def populate(self, group, array, colour_dict, screen, grid):
        x = 10
        y = 10
        for i in range(len(array)):
            for j in range(len(array[i])):
                cb = ColourBlock(colour=colour_dict[array[i][j]], x=x, y=y, callback=on_click, screen=screen, grid=self)
                group.add(cb)
                grid[i][j] = cb
                x += 100
            x = 10
            y += 100
    def update_positions(self):
        x = 10
        y = 10
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] is not None:
                    self.grid[i][j].updatePoints(x, y)
                else:
                    x += 100
                    continue
                x += 100
            x = 10
            y += 100

    def shuffle_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                # Get random neighbor
                rand_i = random.randint(max(0, i - 1), min(len(self.grid) - 1, i + 1))
                rand_j = random.randint(max(0, j - 1), min(len(self.grid[i]) - 1, j + 1))

                # Swap color blocks
                self.grid[i][j], self.grid[rand_i][rand_j] = self.grid[rand_i][rand_j], self.grid[i][j]


