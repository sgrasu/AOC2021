import re

def resize(grid, x, y):
    xIncrement = x - len(grid[0])
    yIncrement = y - len(grid)

    new_grid = grid
    new_grid = [row[0:x] + [0]*xIncrement for row in grid]
    new_grid = new_grid[0:y] + [[0]*x for _ in range(max(0,yIncrement))]
    
    return new_grid

def printGrid(grid: list[list]):
    print(f'{len(grid)} x {len(grid[0])} Grid')
    for row in grid:
        print(row)
    print('')


regex = r"(\d+),(\d+) -> (\d+),(\d+)"
grid = [[0]]
gridx = 1
gridy = 1

with open('day5.txt','r') as file:
    lines = map(lambda s: tuple(int(x) for x in re.search(regex, s).groups()), file.read().splitlines())
    for ax,ay,bx,by in list(lines):
        # print(ax,ay,bx,by)
        gridx = max(gridx, ax + 1, bx + 1)
        gridy = max(gridy, ay + 1, by + 1)
        grid = resize(grid, gridx, gridy)
        # printGrid(grid)

        if ax == bx:
            y1, y2 = (ay, by) if ay < ax else (by, ay)
            for y in range(y1, y2+1):
                # print(ax,y)
                grid[y][ax] += 1
        else:
            x1, x2, y1, y2 = (ax, bx, ay, by) if ax < bx else (bx, ax, by, ay)
            m = (y2-y1)/(x2-x1)
            b = y2 - m*x2

            for x in range(x1, x2+1):
                y = int(m*x+b)
                # print(x,y)
                grid[y][x] += 1
    
    # print(gridx, gridy)
    # printGrid(grid)
    count = 0
    for row in range(0,gridy):
        for col in range(0,gridx):
            count += grid[row][col] >= 2
    print(count)