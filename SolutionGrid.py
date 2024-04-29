from SmallColourBlock import SmallColourBlock
import random
from moves import next_to, find_location, swap, move_cb
class SolutionGrid():

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
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        self.x = x
        self.y = y
        self.screen = screen
        self.group = group
    def populate_solutions(self):
        x = self.x
        y = self.y
        list_choices = ['blue', 'green', 'red', 'white', 'yellow', 'orange']
        counts = {'blue': 0, 'green': 0, 'red': 0, 'white': 0, 'yellow': 0, 'orange': 0}
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                colour = random.choice(list_choices)
                counts[colour] += 1
                if counts[colour] == 4:
                    list_choices.remove(colour)
                scb = SmallColourBlock(colour=self.colour_dict[colour], x=x, y=y, screen=self.screen)
                self.group.add(scb)
                self.grid[i][j] = scb
                x += 30
            x = self.x
            y += 30