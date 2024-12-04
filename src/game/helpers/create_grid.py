def create_grid(locked_possitions={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_possitions:
                c = locked_possitions[(j, i)]
                grid[i][j] = c
    return grid
