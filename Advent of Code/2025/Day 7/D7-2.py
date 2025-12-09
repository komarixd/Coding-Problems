cnt = 0
f = open('input.txt', 'r').read().split('\n')

n = len(f)
m = len(f[0])

f = [str(i) for i in f]

start = f[0].index('S')

dp = [[0 for _ in range(m)] for _ in range(n)]

for j in range(m):
    dp[n-1][j] = 1

for i in range(n - 2, -1, -1):     
    for j in range(m):
        if f[i][j] == 'S':
            continue

        if f[i][j] != '.':
            continue

        below = f[i+1][j]

        if below == '^':
            val = 0
            if j - 1 >= 0:
                val += dp[i+1][j-1]
            if j + 1 < m:
                val += dp[i+1][j+1]
            dp[i][j] = val

        elif below == '.':
            dp[i][j] += dp[i+1][j]

        else:
            dp[i][j] = 1

print(dp[1][start])
