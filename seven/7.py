import numpy as np

f = open("in.txt", "r")
lines = f.readlines()
f.close()

rows = []
for line in lines[:-1]:
    rows.append(np.array(list(line.strip('\n')), dtype='U1'))
    grid = np.vstack(rows)

splits = 0

for line in range(1, len(grid)):
    for col in range(len(grid[line])):
        if grid[line][col] == '.':
            if grid[line-1][col] == 'S' or grid[line-1][col] == '|':
                grid[line][col] = '|'
        elif grid[line][col] == '^' and (grid[line-1][col] == 'S' or grid[line-1][col] == '|'):
            grid[line][col-1] = '|'
            grid[line][col+1] = '|'
            splits += 1

print("Part one result: " + str(splits))

paths = np.zeros_like(grid, dtype=int)

for i in range(len(paths[0])):
    if grid[0][i] == 'S':
        paths[0][i] = 1

for line in range(1, len(paths)):
    for col in range(len(paths[line])):
        node_paths = 0
        if grid[line][col] != "|":
            continue
        if grid[line-1][col] == '|' or grid[line-1][col] == 'S':
            node_paths += paths[line-1][col]
        if col > 0 and grid[line][col-1] == '^':
            node_paths += paths[line - 1][col - 1]
        if col < len(grid[line]) - 1 and grid[line][col+1] == '^':
            node_paths += paths[line - 1][col + 1]
        paths[line][col] = node_paths

#for line in paths:
#    print(line)

print("Part two result: " + str(np.sum(paths[-1])))
