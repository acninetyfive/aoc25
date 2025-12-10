import numpy as np
import re

f = open("test.txt", "r")
pattern = re.compile(r"(\[.*\]) (\(.*\)) (\{.*\})")
max_len = 0
first_ten_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for line in f:
    print(line.strip())
    match = pattern.match(line.strip())
    end_state = match.group(1).strip('[]')
    transitions = match.group(2).split(' ')
    joltage = {i: int(x) for i, x in enumerate(match.group(3).strip('{}').split(','))}
    l = len(end_state)
    if l > max_len:
        max_len = l
    #print(end_state, transitions, joltage)
    #input()

    machine = {}
    on_lights = set()
    off_lights = set()
    for i in range(len(match.group(1).strip('[]'))):
        machine[i] = {'end': end_state[i] == '#', 'joltage': joltage[i]}
        if end_state[i] == '#':
            on_lights.add(i)
        else:
            off_lights.add(i)

    transition_numbers = set()
    for t in transitions:
        numbers = t.strip('()').split(',')
        tn = 1
        for n in numbers:
            tn *= first_ten_primes[int(n)]
        transition_numbers.add(tn)
        #print("Transition number:", tn, "for", numbers)
    print("Machine:", machine)
    print("Transition numbers:", transition_numbers)
    print()

    # Try all cominations of one transition, then two, etc.
    found = False
    num_transitions = 0
    while not found:
        num_transitions += 1
        print("Trying", num_transitions, "transitions")
        from itertools import product
        for transition_sequence in product(transition_numbers, repeat=num_transitions):
            # Apply this sequence of transitions
            current_on = on_lights.copy()
            current_off = off_lights.copy()
            for tn in transition_sequence:
                next_on = set()
                next_off = set()
                for light in current_on:
                    if tn % machine[light]['joltage'] == 0:
                        next_on.add(light)
                    else:
                        next_off.add(light)
                for light in current_off:
                    if tn % machine[light]['joltage'] == 0:
                        next_on.add(light)
                    else:
                        next_off.add(light)
                current_on = next_on
                current_off = next_off
            # Check if we reached the end state
            success = True
            for light in machine:
                if machine[light]['end']:
                    if light not in current_on:
                        success = False
                        break
                else:
                    if light not in current_off:
                        success = False
                        break
            if success:
                print("Found solution with transitions:", transition_sequence)
                found = True
                break


    input()


f.close()

print(max_len)