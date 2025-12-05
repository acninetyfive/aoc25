
def part_one(ranges):
    running_sum = 0

    for r in ranges:
        for i in range(r[0], r[1] + 1):
            if str(i)[:len(str(i)) // 2] == str(i)[len(str(i)) // 2:]:
                running_sum += i
    return running_sum


def part_two(ranges):
    running_sum = 0

    for r in ranges:
        for i in range(r[0], r[1] + 1):
            seq_length = len(str(i)) // 2
            while seq_length > 0:
                if len(str(i)) % seq_length != 0:
                    seq_length -= 1
                    continue
                j = seq_length
                while j + seq_length <= len(str(i)):
                    if str(i)[j:j+seq_length] != str(i)[:seq_length]:
                        break
                    j += seq_length
                if j == len(str(i)):
                    running_sum += i
                    break
                seq_length -= 1
    return running_sum

f = open("in.txt", "r")
l = f.readline().strip().split(',')
ranges = [(int(a), int(b)) for a, b in (x.split('-') for x in l)]
f.close()

print("Part one result: " + str(part_one(ranges)))
print("Part two result: " + str(part_two(ranges)))