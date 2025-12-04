curr = 50
res = 0

f = open('input.txt', 'r').read().split()
for i in f:
    mult = -1
    if i[0] == 'R':
        mult = 1
    for j in range(int(i[1:])):
        curr = (curr + 100 + mult) % 100
        if curr == 0:
            res += 1
print(res)