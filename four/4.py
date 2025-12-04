
def get_adj_count(grid, pos):
    count = 0
    check_up = pos[0] > 0
    check_down = pos[0] < len(grid) - 1
    check_left = pos[1] > 0
    check_right = pos[1] < len(grid[0]) - 1
    if check_up:
        if grid[pos[0]-1][pos[1]] == "@":
            count += 1
        if check_left and grid[pos[0]-1][pos[1]-1] == "@":
            count += 1
        if check_right and grid[pos[0]-1][pos[1]+1] == "@":
            count += 1
    if check_down:
        if grid[pos[0]+1][pos[1]] == "@":
            count += 1
        if check_left and grid[pos[0]+1][pos[1]-1] == "@":
            count += 1
        if check_right and grid[pos[0]+1][pos[1]+1] == "@":
            count += 1
    if check_left:
        if grid[pos[0]][pos[1] - 1] == "@":
            count += 1
    if check_right:
        if grid[pos[0]][pos[1] + 1] == "@":
            count += 1
    return count


f = open("in.txt", "r")
grid = [list(line.strip()) for line in f]
f.close()
total = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "@" and get_adj_count(grid, (r, c)) < 4:
            total += 1

print("Part One:", total)

total = 0
removed = True
while removed:
    removed = False
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@" and get_adj_count(grid, (r, c)) < 4:
                total += 1
                grid[r][c] = "."
                removed = True

print("Part two:", total)
