cnt = 0
f = open('input.txt', 'r').read().split('\n')
op = f[-1].split()
f = f[:-1]
n = len(f)
m = len(f[0])

calc = []

curr = []
for i in range(m):
    check = True
    for j in range(n):
        if f[j][i] != ' ':
            check = False
    if check:
        calc.append(curr)
        curr = []
        continue
    val = 0
    for j in range(n):
        if f[j][i] != ' ':
            val = val*10 + int(f[j][i])
    curr.append(val)
calc.append(curr)        

for i in range(len(calc)):
    res = 0 if op[i] == '+' else 1
    for j in calc[i]:
        if op[i] == '+':
            res += j
        else:
            res *= j
    cnt += res
print(cnt)