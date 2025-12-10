f = open('input.txt', 'r').read().split('\n')

res = 0

import ast, collections
from pulp import *

def solve(w, switches):
    
    prob = LpProblem('asd', LpMinimize)
    
    var = [LpVariable(f"a{i}", lowBound=0, cat="Integer") for i in range(len(switches))]
    
    prob += lpSum(var)
    
    for pos in range(len(w)):
        prob += (
            lpSum(var[btn] * switches[btn][pos] for btn in range(len(switches))) == w[pos], f"b{pos}"
        )
    
    prob.solve(PULP_CBC_CMD(msg=0))
    
    return sum([int(v.varValue) for v in var])


l = 1
for line in f:
    line = line.split()
    
    want = ast.literal_eval(line[-1][1:-1])
        
    switch = [ast.literal_eval(i) for i in line[1:-1]]
    switch = [tuple([i]) if type(i)==int else i for i in switch]
    
    new_switches = []
    for i in switch:
        n = []
        for j in range(len(want)):
            n.append(1 if j in i else 0)
        new_switches.append(n)

    res += solve(want, new_switches)

print(res)
