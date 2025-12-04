res = 0
f = open('input.txt', 'r').read().split()
for num in f:
    n = len(num)
    if n <= 2:
        res += int(num)
        continue
    
    best = int(num[n-2:])
    suf = int(num[n-1])
    for i in range(n-2, -1, -1):
        d = num[i]
        best = max(best, int(d)*10+suf)
        suf = max(suf, int(d))
    res += best
print(res)