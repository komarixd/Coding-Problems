res = 0
f = open('input.txt', 'r').read().split()
for num in f:
    vector = [int(i) for i in num]
    # print(vector)
    n = len(vector)
    dp = [[0 for _ in range(n)] for _ in range(12)]
    for i in range(12):
        for j in range(n-i-1,-1,-1):
            if i==0:
                dp[0][j] = vector[j]
                
            if i>0 and j+1<n:
                dp[i][j] = vector[j]*pow(10,i) + dp[i-1][j+1]
        for j in range(n-2,-1,-1):
            dp[i][j] = max(dp[i][j], dp[i][j+1])
            
        # print(dp[i])

    res += dp[11][0]

    
print(res)



