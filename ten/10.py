import numpy as np
import re

def bool_array_from_end_state(end_state):
    array = np.array([c == '#' for c in end_state], dtype=bool)
    return array

def bool_array_from_transition(transition, length):
    array = np.zeros(length, dtype=bool)
    numbers = transition.strip('()').split(',')
    for n in numbers:
        array[int(n)] = True
    return array

def bool_array_to_int_array(bool_array):
    int_array = np.array([1 if b else 0 for b in bool_array], dtype=int)
    return int_array

def part_one(end_state_array, transition_arrays):
    # Try all cominations of one transition, then two, etc.
    found = False
    num_transitions = 0
    while not found:
        num_transitions += 1
        from itertools import product
        for transition_sequence in product(transition_arrays, repeat=num_transitions):
            # Apply this sequence of transitions
            current_state = np.zeros_like(end_state_array, dtype=bool)
            for ta in transition_sequence:
                next_state = np.logical_xor(current_state, ta)
                current_state = next_state
            if np.all(current_state == end_state_array):
                found = True
                break
    return num_transitions

f = open("in.txt", "r")
pattern = re.compile(r"(\[.*\]) (\(.*\)) (\{.*\})")
fewest_transitions_one = []
fewest_transitions_two = []
for line in f:
    print(line.strip())
    match = pattern.match(line.strip())
    end_state = match.group(1).strip('[]')
    transitions = match.group(2).split(' ')
    joltage_end_state = np.array([int(x) for x in match.group(3).strip('{}').split(',')])

    # Part One
    end_state_array = bool_array_from_end_state(end_state)
    transition_arrays = []
    for t in transitions:
        transition_arrays.append(bool_array_from_transition(t, len(end_state)))
    
    fewest_transitions_one.append(part_one(end_state_array, transition_arrays))
    # End part one
    

f.close()

print("Part one result: " + str(sum(fewest_transitions_one)))