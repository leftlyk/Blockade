from moves import next_to, find_location, swap

def on_click(thingy, action, grid):
    print("clicked")
    if action == 'clicked':
        clicked = find_location(grid, thingy)
        blank = find_location(grid, None)
        if next_to(clicked, blank):
            swap(clicked, blank, grid)