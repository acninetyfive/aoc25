import numpy as np
import re
from collections import deque

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

def joltage_transition(current_state, joltage_transition):
    next_state = current_state + joltage_transition
    return next_state

def search(current_state, joltage_end_state, light_to_joltage, index_to_increment, sorted_joltage_indexes):
    # BFS: queue of (state_array, index_to_increment, transitions_so_far)
    queue = deque()
    start_state = current_state.copy()
    for t in light_to_joltage[sorted_joltage_indexes[index_to_increment]]:
        queue.append((start_state + t, index_to_increment, 1))
    visited = set()
    visited.add((tuple(int(x) for x in start_state)))

    #print(f"[search] start_state={tuple(int(x) for x in start_state)} index={sorted_joltage_indexes[index_to_increment]} transitions={1}")
    step = 0
    while queue:
        state, idx, trans = queue.popleft()
        step += 1
        state_tuple = tuple(int(x) for x in state)
        print(f"[search][step {step}] popped state={state_tuple} idx={sorted_joltage_indexes[idx]} trans={trans} queue_size={len(queue)}")
        visited.add(state_tuple)
        # global prune
        if np.any(state > joltage_end_state):
            print(f"[search][step {step}] prune: state {state_tuple} exceeds target {tuple(int(x) for x in joltage_end_state)}")
            continue
        if np.array_equal(state, joltage_end_state):
            print(f"[search][step {step}] found exact match with trans={trans}")
            return trans

        # Determine next index to increment
        if state[sorted_joltage_indexes[idx]] < joltage_end_state[sorted_joltage_indexes[idx]]:
            key = idx
        else:
            key = idx + 1
            while state[sorted_joltage_indexes[key]] == joltage_end_state[sorted_joltage_indexes[key]]:
                key += 1
            print(f"[search][step {step}] advancing to next index to increment: {sorted_joltage_indexes[key]}")
        print(f"[search][step {step}] processing key={key} (state[{sorted_joltage_indexes[key]}]={state[sorted_joltage_indexes[key]]} target={joltage_end_state[sorted_joltage_indexes[key]]})")
        for jt in light_to_joltage[sorted_joltage_indexes[key]]:
            next_state = joltage_transition(state, jt)
            state_key = (tuple(int(x) for x in next_state), key)
            if state_key in visited:
                #print(f"[search][step {step}] already visited state={state_key[0]} idx={key}")
                continue
            queue.append((next_state, key, trans + 1))

    print("[search] exhausted queue: no solution found")
    return None

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
    
    # fewest_transitions_one.append(part_one(end_state_array, transition_arrays))
    # End part one

    # Part Two
    joltage_transition_arrays = [bool_array_to_int_array(ta) for ta in transition_arrays]
    
    light_to_joltage = {i: [] for i in range(len(joltage_end_state))}
    for i in range(len(joltage_transition_arrays)):
        for j in range(len(joltage_end_state)):
            if joltage_transition_arrays[i][j] == 1:
                light_to_joltage[j].append(joltage_transition_arrays[i])
    
    # Search starting from lowest joltage
    visited = set()
    index = 0
    print("Joltage end state:", joltage_end_state)
    sorted_joltage_indexes = np.argsort(joltage_end_state)
    print("Sorted joltage indexes:", sorted_joltage_indexes)
    while joltage_end_state[sorted_joltage_indexes[index]] == 0:
        index += 1
    print("Starting index:", sorted_joltage_indexes[index])
    input()
    current_state = np.zeros_like(joltage_end_state, dtype=int)
    result = search(current_state, joltage_end_state, light_to_joltage, index, sorted_joltage_indexes)
    print("Fewest transitions (part two):", result)
    fewest_transitions_two.append(result)
    #input("Press Enter to continue...")

f.close()

#print("Part one result: " + str(sum(fewest_transitions_one)))
print("Part two result: " + str(sum(fewest_transitions_two)))