**Porblem 1**

Given an integer. Find the largest number that can be form by picking exactly 2 digit.

For example,

```
Given : 156121931128436
Largest number = 98. (156121 9 3112 8 436)
```

To solve the problem, loop from the back and find the largest number occured and add it to current number.

```
input = 3916
length = 4
let suffix = input[length] = 6
result = 0

for i in range 3 -> 1:
	result = max( result, input[i] * 10 + suffix )
	suffix = max( suffix, input[i] )
```

**Problem 2**

Change from picking 2 digits to 12 digits.

The solution is the same, find the largest suffix but optimize with dynamic programming.

Let input number be 'input' and legnth of it be 'n'

Let dp[i][j] be the highest possible number can be formed by pick exactly i digits by only using value from j-n

Then update dp[i][j] = max( dp[i][j+1] , input[j]\*(number of digit) + dp[i-1][j+1] )

