import pygame
class ColourBlock(pygame.sprite.Sprite):
    def __init__(self, colour, x, y, callback, screen, grid):
        pygame.sprite.Sprite.__init__(self)
        self.width = 90
        self.height = 90
        self.area = screen.get_rect()
        self.colour = colour
        self.callback = callback
        self.grid = grid
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
                    self.callback(self, 'clicked', self.grid)


    def updatePoints(self, x, y):
        print("points updated.")
        self.rect.x = x
        self.rect.y = y
    def getColour(self):
        return self.colour