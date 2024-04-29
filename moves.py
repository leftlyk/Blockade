
def next_to(l1, l2):
    l1_row = l1[0]
    l1_col = l1[1]
    l2_row = l2[0]
    l2_col = l2[1]
    if (((l1_row == l2_row) and ((l1_col == (l2_col + 1)) or (l1_col == (l2_col - 1)))) or
            ((l1_col == l2_col) and ((l1_row == (l2_row + 1)) or (l1_row == (l2_row - 1))))):
        return True
    return False

def find_location(gr, item):
    print("Find location: ", gr.grid)
    grid = gr.grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == item:
                return (i,j)

def swap(l1, l2, gr):
    grid = gr.grid
    print(grid)
    l1_row = l1[0]
    l1_col = l1[1]
    l2_row = l2[0]
    l2_col = l2[1]
    grid[l1_row][l1_col], grid[l2_row][l2_col] = grid[l2_row][l2_col], grid[l1_row][l1_col]
    print(grid)
    gr.update_positions()


def move_cb(action, gr):
    grid = gr.grid
    blank = find_location(gr, None)
    print("Blank:", blank)
    dict = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if next_to((i, j), blank):
                if j == blank[1] and i == blank[0] - 1:
                    dict['down'] = (i,j)
                elif j == blank[1] and i == blank[0] + 1:
                    dict['up'] = (i,j)
                elif i == blank[0] and j == blank[1] - 1:
                    dict['right'] = (i,j)
                elif i == blank[0] and j == blank[1] + 1:
                    dict['left'] = (i,j)

    if action == 'left' and 'left' in dict.keys():
        swap(dict['left'], blank, gr)
    elif action == 'right' and 'right' in dict.keys():
        swap(dict['right'], blank, gr)
    elif action == 'up' and 'up' in dict.keys():
        swap(dict['up'], blank, gr)
    elif action == 'down' and 'down' in dict.keys():
        swap(dict['down'], blank, gr)

    gr.update_positions()


