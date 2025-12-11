f = open('input.txt', 'r').read().split('\n')

res = 0

edges = {}
cnt = {'you':1}

for line in f:
    line = line.split(': ')
    u = line[0]
    v = line[1].split(' ')
    for i in v:
        if i not in edges:
            edges[i] = []
        edges[i].append(u)


def dfs(curr):
    if curr in cnt:
        return cnt[curr]
    r = 0
    if curr not in edges:
        return 0
    for nxt in edges[curr]:
        r += dfs(nxt)
    cnt[curr] = r
    return r


print(dfs('out'))