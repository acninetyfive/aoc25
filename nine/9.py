import numpy as np

f = open("in.txt", "r")
points = []
for line in f:
    pos = (int(line.split(",")[0]), int(line.split(",")[1]))
    points.append(pos)
f.close()

def rectangular_area(p1, p2):
    return (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1])+1)

def is_inside_loop(p, grid):
    border_crossings = 0
    x = p[0]
    while x >= 0:
        crossed = False
        while grid[p[1]][x] == 1 or grid[p[1]][x] == 2:
            crossed = True
            x -= 1
        if crossed:
            border_crossings += 1
        else:
            x -= 1
    return border_crossings % 2 == 1
areas = []
max_area = 0
for i in range(len(points)):
    for j in range(len(points)):
        if i == j:
            continue
        area = rectangular_area(points[i], points[j])
        areas.append((area, points[i], points[j]))
        if area > max_area:
            max_area = area

print("Part one result: " + str(max_area))

print("smallest X: " + str(min(points, key=lambda x: x[0])[0]))
print("largest X: " + str(max(points, key=lambda x: x[0])[0]))
print("smallest Y: " + str(min(points, key=lambda x: x[1])[1]))
print("largest Y: " + str(max(points, key=lambda x: x[1])[1]))

grid = np.zeros((max(points, key=lambda x: x[1])[1] + 1,
                 max(points, key=lambda x: x[0])[0] + 1), dtype=int)
boundary_points = set()
for i in range(len(points)):
    grid[points[i][1]][points[i][0]] = 1
    if points[i][0] == points[(i-1)%len(points)][0]:
        for y in range(min(points[i][1], points[(i-1)%len(points)][1]) + 1, max(points[i][1], points[(i-1)%len(points)][1])):
            grid[y][points[i][0]] = 2
            boundary_points.add((points[i][0], y))
    elif points[i][1] == points[(i-1)%len(points)][1]:
        for x in range(min(points[i][0], points[(i-1)%len(points)][0]) + 1, max(points[i][0], points[(i-1)%len(points)][0])):
            grid[points[i][1]][x] = 2
            boundary_points.add((x, points[i][1]))

#for line in grid:
#    print(line)

areas.sort(key=lambda x: x[0], reverse=True)

print(areas[:3])
print(areas[-3:])
input()
max_area = 0

# Check if an inset of 1 unit touches the boundary
for i in range(len(areas)):
    if i % 10000 == 0:
        print("Checking area", i, "of", len(areas))
    # print("Checking area:", area[0])
    p1 = areas[i][1]
    p2 = areas[i][2]
    # check boundary of inset rectangle 
    inset_points = set()
    x_min = min(p1[0], p2[0]) + 1
    x_max = max(p1[0], p2[0]) - 1
    y_min = min(p1[1], p2[1]) + 1  
    y_max = max(p1[1], p2[1]) - 1
    #print(x_min, x_max, y_min, y_max)
    touches_boundary = False
    for y in range(y_min, y_max + 1):
        if (x_min, y) in boundary_points or (x_max, y) in boundary_points:
            touches_boundary = True
            break
    for x in range(x_min, x_max + 1):
        if (x, y_min) in boundary_points or (x, y_max) in boundary_points:
            touches_boundary = True
            break
    if not touches_boundary:
        max_area = areas[i][0]
        print("Found max area:", max_area, "with points", p1, p2)
        break

print("Part two result: " + str(max_area))