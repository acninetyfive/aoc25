
def get_next_digit(start, place, bank):
    best = start
    for i in range(best, len(bank) - place):
        if int(bank[i]) > int(bank[best]):
            best = i
    return best


def part_both(banks, place):
    total_jolts = 0
    for bank in banks:
        p = place
        digits = []
        start = 0
        while p >= 0:
            next_digit = get_next_digit(start, p, bank)
            digits.append(next_digit)
            start = next_digit + 1
            p -= 1
        jolts_string = "".join([bank[i] for i in digits])
        jolts = int(jolts_string)
        total_jolts += jolts
    return total_jolts


f = open("in.txt", "r")
banks = [line.strip() for line in f]
f.close()

print("ONE:", part_both(banks, 1))
print("TWO:", part_both(banks, 11))
