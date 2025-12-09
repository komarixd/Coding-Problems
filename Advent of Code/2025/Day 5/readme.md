**Problem 1**

Problem want to : Find all id that is in the range.

Sort the ingredients id array and create array fresh.

fresh[i] = 1 if it is fresh, else 0

Then for each range, use binary search to find the left, right boundary then set all item in boundary to be 1

Answer is sum of all value in fresh

**Problem 2**

The problem statement : Fresh ingredients are all id in the range.

Let each range be start-stop

We sort the range in ascending order by first position (start)

Then iterate through all range and merge the range that overlap.

```
ranges = [[1,5], [4,8], [8,10], [13,16]]

new_range = [[1,5]] # include first range in to the new range

for i in range(1, 4): # start from second range

	if range[i][0] <= new_range[-1][1]: # if it is overlap
		update the end position of new_range[-1]
	
	else :
		add the range into new_range
		
# now new_range = [[1,10], [13,16]]
Then result = Total sum of size of each range
```