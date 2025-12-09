import math
import numpy as np

f = open("test.txt", "r")
points = {}
for line in f:
    pos = (int(line.split(",")[0]), int(line.split(",")[1]), int(line.split(",")[2]))
    points[pos] = {pos}
f.close()

def distance(p1, p2):
    print(p1)
    return math.dist(list(p1), list(p2))

def part_one(points):
    distances = []
    p_k = list(points.keys())
    for i in range(len(p_k) - 1):
        for j in range(i+1, len(p_k)):
            dist = distance(p_k[i], p_k[j])
            distances.append((dist, p_k[i], p_k[j]))
    distances = sorted(distances, key=lambda x: x[0])

    connections = 0
    i = 0
    while connections < 10:
        d = distances[i]
        if d[1] not in points[d[2]]:
            print(f"Connection {connections}", d[1], "and", d[2], "with distance", d[0])
            connections += 1
            for p in points:
                if d[1] in points[p] or d[2] in points[p]:
                    points[p] = points[p].union(points[d[2]]).union(points[d[1]])
            for p in points:
                print(p, points[p])
            input()
        i += 1
    
    for p in points:
        print(p, points[p])
    
    circuits = set()
    for p in points:
        if points[p] not in circuits:
            circuits.add(frozenset(points[p]))
    
    c = sorted(list(circuits), key=lambda x: len(x), reverse=True)
    print("circuits")
    for ct in circuits:
        print(ct)

    print(len(c[0]), len(c[1]), len(c[2]))
    return len(c[0])*len(c[1])*len(c[2])

print("Part one result: " + str(part_one(points)))


