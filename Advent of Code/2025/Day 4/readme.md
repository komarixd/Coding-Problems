**Problem 1**

Given map of size n\*m. Find the position that on all block around that position has '@' less than 4 times.

Solution:

Loop all index i, j check all block around.

**Problem 2**

The problem statement changed. 

After find that position, remove it.

Let 'map' be the input map and 'new_map' = map

We will update the new_map for every position we can remove then try to remove '@' until there is no '@' to be remove.

```
While true:
	For each i, j of map:
		if number of '@' < 4:
			new_map[i][j] = '.'

	if map == new_map:
		break
	map = new_map
```