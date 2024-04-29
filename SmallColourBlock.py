import pygame
from moves import next_to, find_location, swap, move_cb
class SmallColourBlock(pygame.sprite.Sprite):
    def __init__(self, colour, x, y, screen):
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