from pulp import LpProblem, LpVariable, LpMinimize, LpStatus, LpInteger
import re
import numpy as np

objective_values = []
regex = re.compile(r"(?:\[.*\]) (\(.*\)) (\{.*\})")
f = open("in.txt", "r")
for line in f:
    match = regex.match(line.strip())
    transitions = match.group(1).split(' ')
    joltage_end_state = np.array([int(x) for x in match.group(2).strip('{}').split(',')])
    print("Transitions:", transitions)
    print("Joltage end state:", joltage_end_state)
    

    # Build the coefficient matrix
    arrays = []
    for t in transitions:
        base = np.zeros(len(joltage_end_state), dtype=int)
        for n in t.strip('()').split(','):
            base[int(n)] = 1
        arrays.append(base)
    coefficient_matrix = np.array(arrays).T
    print("Coefficient matrix:\n", coefficient_matrix)
    constant_vector = np.array(joltage_end_state)
    #input()
    # Solve the system using linear programming
    prob = LpProblem("TransitionProblem", LpMinimize)
    vars = [LpVariable(str(i), lowBound=0, cat=LpInteger) for i in range(len(transitions))]
    prob += sum(vars), "Minimize_Transitions"

    for i in range(len(joltage_end_state)):
        prob += (sum(coefficient_matrix[i][j] * vars[j] for j in range(len(transitions))) == constant_vector[i])
    prob.solve()
    print("Status:", LpStatus[prob.status])
    print("Objective value:", prob.objective.value())
    objective_values.append(prob.objective.value())
    print("Variable values:")
    for v in prob.variables():
        print(f"{v.name} = {v.varValue}")
    #input()
f.close()

print("Sum of objective values:", sum(objective_values))