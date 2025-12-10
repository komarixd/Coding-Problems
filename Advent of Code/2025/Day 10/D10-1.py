f = open('input.txt', 'r').read().split('\n')

res = 0

import ast, collections

def solve(w, switches):
    
    vis = [0 for _ in range(2**12)]
    q = collections.deque([0])
    vis[0] = 1
    
    step = 0
    while (q):
        t = len(q)
        for i in range(t):
            curr = q.popleft();
            if curr == w:
                return step
            
            for switch in switches:
                nxt = curr ^ switch
                if not vis[nxt]:
                    vis[nxt] = 1
                    q.append(nxt)
        step += 1

for line in f:
    line = line.split()
    
    want = line[0][1:-1]
    switch = [ast.literal_eval(i) for i in line[1:-1]]
    
    new_switch = []
    for s in switch:
        if type(s)==int:
            s = [s]
        n= 0
        for k in s:
            n ^= (1<<k)
        new_switch.append(n)

    new_want = 0
    for i in range(len(want)):
        if want[i] == '#':
            new_want ^= (1<<i)
    
    # print(want, new_want)
    # print(new_switch)
    res += solve(new_want, new_switch)

print(res)