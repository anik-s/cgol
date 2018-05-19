from __future__ import print_function
import copy


def get_new_grid_after_age(old_grid, age):
    for i in range(0, age):
        old_grid = get_new_grid(old_grid)
    return old_grid


def get_new_grid(grid):
    new_grid = copy.deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            adjacent_items = []
            item = grid[i][j]
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x <= len(grid) - 1 and x >= 0 and y <= len(grid[i]) - 1 and y >= 0:
                        if x == i and y == j:
                            pass
                        else:
                            adjacent_items.append(grid[x][y])

            alive_adjacent_count = 0
            for a_item in adjacent_items:
                if a_item == 1:
                    alive_adjacent_count = alive_adjacent_count + 1
            # print(str(item) + ':' + str(alive_adjacent_count))
            if item == 1:
                if alive_adjacent_count == 2 or alive_adjacent_count == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            elif item == 0:
                if alive_adjacent_count == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
    return new_grid



