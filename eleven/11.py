import numpy as np

def find_all_paths(adjacency_list, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in adjacency_list:
        return []
    paths = []
    for node in adjacency_list[start]:
        if node not in path:
            new_paths = find_all_paths(adjacency_list, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths


def topological_sort(adjacency_list):
    visited = set()
    stack = []

    def visit(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in adjacency_list.get(node, []):
            visit(neighbor)
        stack.append(node)

    for vertex in adjacency_list:
        visit(vertex)

    stack.reverse()
    return stack


def paths_between(adjacency_list, start, end):
    sorted_nodes = topological_sort(adjacency_list)
    count = np.zeros(len(sorted_nodes), dtype=int)
    count[sorted_nodes.index(start)] = 1  # Start node
    for node in sorted_nodes[sorted_nodes.index(start):]:
        for neighbor in adjacency_list.get(node, []):
            count[sorted_nodes.index(neighbor)] += count[sorted_nodes.index(node)]
    return count[sorted_nodes.index(end)]
    

adjacency_list = {}
f = open("in.txt", "r")
for line in f:
    a, b = line.strip().split(": ")
    adjacency_list[a] = set(b.split(" "))
f.close()

print("Part 1:", len(find_all_paths(adjacency_list, "you", "out")))
#print("Topological Sort:", topological_sort(adjacency_list))
# No paths from dac to fft
segment_one = paths_between(adjacency_list, "svr", "fft")
segment_two = paths_between(adjacency_list, "fft", "dac")
segment_three = paths_between(adjacency_list, "dac", "out")
print("Part 2:", segment_one * segment_two * segment_three)