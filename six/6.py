import numpy as np

def part_one(file_path="in.txt"):
    f = open(file_path, "r")
    columns = []
    for line in f:
        items = line.strip().split()
        if items[0] == '*' or items[0] == '+':
            operations = items
            continue
        columns.append([int(x) for x in items]) 
    f.close()
    columns = np.array(columns)
    total = 0
    for i in range(len(operations)):
        op = operations[i]
        col = columns[:, i]
        if op == '*':
            total += np.prod(col)
        elif op == '+':
            total += np.sum(col)
    return total

def part_two(file_path="in.txt"):
    f = open(file_path, "r")

    lines = f.readlines()
    f.close()

    operation_line = lines[-1].strip()

    operations = []

    for i in range(len(operation_line)):
        if operation_line[i] in ['*', '+']:
            operations.append((i, operation_line[i]))
    
    rows = []
    for line in lines[:-1]:
        rows.append(np.array(list(line.strip('\n')), dtype='U1'))
        grid = np.vstack(rows)
    
    total = 0
    op = 0
    numbers = []
    for i in range(len(grid[0])):
        number_str = ''.join(grid[:, i]).strip()
        if number_str == '':
            if operations[op][1] == '*':
                total += np.prod(numbers)
            elif operations[op][1] == '+':
                total += np.sum(numbers)
            numbers = []
            op += 1
        else:
            numbers.append(int(number_str))
    
    if operations[op][1] == '*':
        total += np.prod(numbers)
    elif operations[op][1] == '+':
        total += np.sum(numbers)

    return total
        


path = "in.txt"

print("Part one result: " + str(part_one(path)))
print("Part two result: " + str(part_two(path)))