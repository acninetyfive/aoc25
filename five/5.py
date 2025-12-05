import numpy as np

f = open("in.txt", "r")
line = f.readline().strip()
ranges = []
max_number = 0
while line:
    # ranges
    start, end = int(line.split('-')[0]), int(line.split('-')[1])
    ranges.append((start, end))
    max_number = max(max_number, end)
    line = f.readline().strip()
line = f.readline().strip()
numbers = []
while line:
    # numbers
    numbers.append(int(line))
    line = f.readline().strip()
f.close()


def merge_ranges(ranges):
    # Merge overlapping ranges
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    for current in sorted_ranges:
        if not merged or merged[-1][1] < current[0] - 1:
            merged.append(current)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
    return merged

merged_ranges = merge_ranges(ranges)
print(len(merged_ranges))
count = 0
for number in numbers:
    for r in merged_ranges:
        if r[0] <= number <= r[1]:
            count += 1
print("Part one result: " + str(count))

part_two_count = 0
for r in merged_ranges:
    part_two_count += (r[1] - r[0] + 1)

print("Part two result: " + str(part_two_count))