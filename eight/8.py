import math
import numpy as np

f = open("in.txt", "r")
points = {}
for line in f:
    pos = (int(line.split(",")[0]), int(line.split(",")[1]), int(line.split(",")[2]))
    points[pos] = {pos}
f.close()

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def part_one(points):
    distances = []
    p_k = list(points.keys())
    print("Points:", len(p_k))
    for i in range(len(p_k) - 1):
        for j in range(i+1, len(p_k)):
            dist = distance(p_k[i], p_k[j])
            distances.append((dist, p_k[i], p_k[j]))
    distances = sorted(distances, key=lambda x: x[0])
    print("Distances calculated:", len(distances))

    connections = 0
    i = 0
    while connections < 10:
        d = distances[i]

        print(f"Connection {connections}", d[1], "and", d[2], "with distance", d[0])
        connections += 1
        for p in points:
            if d[1] in points[p] or d[2] in points[p]:
                points[p] = points[p].union(points[d[2]]).union(points[d[1]])
        i += 1
    
    for p in points:
        print(p, points[p])
    
    circuits = set()
    for p in points:
        if points[p] not in circuits:
            circuits.add(frozenset(points[p]))
    
    c = sorted(list(circuits), key=lambda x: len(x), reverse=True)
    print("Circuits found:", len(c))

    print(len(c[0]), len(c[1]), len(c[2]))
    return len(c[0])*len(c[1])*len(c[2])

def part_two(points):
    distances = []
    p_k = list(points.keys())
    print("Points:", len(p_k))
    for i in range(len(p_k) - 1):
        for j in range(i+1, len(p_k)):
            dist = distance(p_k[i], p_k[j])
            distances.append((dist, p_k[i], p_k[j]))
    distances = sorted(distances, key=lambda x: x[0])
    print("Distances calculated:", len(distances))

    i = 0
    all_connected = False
    while not all_connected:
        d = distances[i]

        print(f"Connection {i}", d[1], "and", d[2], "with distance", d[0])
        for p in points:
            if d[1] in points[p] or d[2] in points[p]:
                points[p] = points[p].union(points[d[2]]).union(points[d[1]])
                if len(points[p]) == len(points):
                    print("All points connected.")
                    print("Final connection made between", d[1], "and", d[2])
                    all_connected = True
        i += 1
    return d[1][0] * d[2][0]


#print("Part one result: " + str(part_one(points)))
print(len(points))
print("Part two result: " + str(part_two(points)))


