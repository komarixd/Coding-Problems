cnt = 0
f = open('input.txt', 'r').read().split('\n')
op = f[-1].split()
f = f[:-1]
f = [[int(b) for b in a.split()] for a in f]
n = len(f)
m = len(f[0])

# for i in f:
#     print(i)
# print(op)

for i in range(m):
    o = op[i]
    res = 0 if o=='+' else 1
    for j in range(n):
        if o=='+':
            res += f[j][i]
        else:
            res *= f[j][i]
    cnt += res

print(cnt)