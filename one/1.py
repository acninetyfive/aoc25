
def part_one(moves):
    position = 50
    zero_count = 0

    def make_move(position, direction, distance):
        if direction == 'L':
            position = (position - distance) % 100
        elif direction == 'R':
            position = (position + distance) % 100
        return position

    for move in moves:
        position = make_move(position, move[0], move[1])
        if position == 0:
            zero_count += 1

    return zero_count


def part_two(moves):
    # Make the each of the moves, count how many times we pass through 0
    position = 50
    zero_count = 0  
    def make_move(position, direction, distance):
        nonlocal zero_count
        for _ in range(distance):
            if direction == 'L':
                position = (position - 1) % 100
            elif direction == 'R':
                position = (position + 1) % 100
            if position == 0:
                zero_count += 1
        return position
    
    for move in moves:
        position = make_move(position, move[0], move[1])
    return zero_count


f = open("in.txt", "r")
moves = []
for line in f:
    m = (line[0], int(line[1:]))
    moves.append(m)
f.close()


print("Part one result: " + str(part_one(moves)))
print("Part two result: " + str(part_two(moves)))
