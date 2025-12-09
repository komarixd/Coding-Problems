**Problem 1**

Problem statement : Find the number of split.

Just normal BFS and search for '^' under the '|' and update the result value

**Problem 2**

Problem statement : How many ways that the beam can go?

We let the number of way the the beam can be the bottom be 1 for each column in the last row.

Then we can count the number of ways by using dynamic programming by this condition.

```
let map be the input

for i in range(bottom->top):
	for j in range(width):
		
		# impossible case
		if map[i][j] == '^':
			skip the loop
		
		# splitting case
		if map[i+1][j] == '^': // count the number of way that can split to left and right
			dp[i][j] = dp[i+1][j-1] + dp[i+1][j+1]
			
		# normal case
		if map[i+1][j] == '.':
			dp[i][j] = dp[i+1][j]
```

Result is dp at position under 'S'
