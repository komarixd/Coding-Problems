f = open('input.txt', 'r').read().split('\n')

res = 0

edges = {}

for line in f:
    line = line.split(': ')
    u = line[0]
    v = line[1].split(' ')
    for i in v:
        if i not in edges:
            edges[i] = []
        edges[i].append(u)

def dfs(curr, mode):
    global cnt
    if mode == 1:
        if curr == 'fft':
            return 0
    elif mode == 2:
        if curr == 'dac':
            return 0
    elif mode == 3:
        if curr in ['fft', 'dac']:
            return 0
        
    if curr in cnt:
        return cnt[curr]
    r = 0
    if curr not in edges:
        return 0
    for nxt in edges[curr]:
        r += dfs(nxt, mode)
    cnt[curr] = r
    return r

cnt = {'svr':1}
allcase = dfs('out', 0)
cnt = {'svr':1}
withoutfft = dfs('out', 1)
cnt = {'svr':1}
withoutdac = dfs('out', 2)
cnt = {'svr':1}
withoutboth = dfs('out', 3)

print(allcase - withoutdac - withoutfft + withoutboth)