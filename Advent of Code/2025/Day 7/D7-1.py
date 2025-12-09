cnt = 0
f = open('input.txt', 'r').read().split('\n')

n = len(f)
m = len(f[0])

start = f[0].index('S')
f = [list(i) for i in f]
f[1][start] = '|'
q = '|'

for i in range(n-1):
    for j in range(m):
        if f[i][j]==q:
            if f[i+1][j] == '^':
                cnt += 1
                if j>0:
                    f[i+1][j-1] = q;
                if j<m-1:
                    f[i+1][j+1] = q;
            else:
                f[i+1][j] = q;
        

print(cnt)