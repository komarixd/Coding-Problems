import copy

res = 0
inp = open('input.txt', 'r').read().split()
f = [[i for i in j] for j in inp]
# print(f)
n = len(f)
m = len(f[0])

while True:
    newf = copy.deepcopy(f)
    for i in range(n):
        for j in range(m):
            if f[i][j] == '@':
                cnt = 0
                if i>0:
                    if f[i-1][j] == '@':
                        cnt+=1
                    if j>0 and f[i-1][j-1] == '@':
                        cnt += 1
                    if j+1<m and f[i-1][j+1] == '@':
                        cnt += 1
                if j>0:
                    if f[i][j-1] == '@':
                        cnt += 1
                    if i+1<n and f[i+1][j-1] == '@':
                        cnt += 1
                if i+1<n:
                    if f[i+1][j] == '@':
                        cnt += 1
                    if j+1 < m and f[i+1][j+1] == '@':
                        cnt += 1
                if j+1<m:
                    if f[i][j+1] == '@':
                        cnt += 1
                if cnt < 4:
                    res += 1
                    newf[i][j] = '.'
    if newf == f:
        break
    f = newf
            
print(res)