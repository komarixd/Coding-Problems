**Problem 1**

Problem statement : Find the fewest total press to match the value.

Given the final value and the array of machine index.

We minimize the problem into binary, since we can easily see that pressing button will toggle the number which means we do xor gate on the number. 

Example

```
Final = "...#." = 00010
Button = [
	(0,2,3,4)  = 10111
	(2,3)      = 00110
	(0,4)      = 10001
	(0,1,2)    = 11100
	(1,2,3,4)  = 01111
]
```

Then we can use BFS to solve the problem remembering visited state (binary).

**Problem 2**

The problem change to make the sum of each index match the joltage level of all machine.

For example.

```
Initial Joltage = [0,0,0,0]
Final Joltage = [3,5,4,7]
Button = [
	(3), (1,3), (2), (2,3), (0,2), (0,1)
]
if we press button (0,2)
The joltage at position 0, 2 will up by 1 = [1,0,1,0]

So, to make initial joltage match final joltage, we can press
(3) 1 times
(1,3) 3 times
(2,3) 3 times
(0,2) 1 time
(0,1) 2 times
```

If we think the problem to be mathematical equation what will it be?

```
Transform our input to match the form.
(3)    ->   [0,0,0,1]
(1,3)  ->   [0,1,0,1]
(2)    ->   [0,0,1,0]
(2,3)  ->   [0,0,1,1]
(0,2)  ->   [1,0,1,0]
(0,1)  ->   [1,1,0,0]

So [3,5,4,7] = (1 * [0,0,0,1]) + (3 * [0,1,0,1]) + (3 * [0,0,1,1]) + (1 * [1,0,1,0]) + (2 * [1,1,0,0])

What if we think of them as variable?

Let 
[3,5,4,7] = y
[0,0,0,1] = x1
[0,1,0,1] = x2
[0,0,1,0] = x3
[0,0,1,1] = x4
[1,0,1,0] = x5
[1,1,0,0] = x6

The equation will be 
y = (c1 * x1) + (c2 * x2) + (c3 * x3) + (c4 * x4) + (c5 * x5) + (c6 * x6)
Where ci is coefficient.

Then our answer will be sum of ci.
```

Then we can solve by using some libraries in python.

In my case I use pulp


