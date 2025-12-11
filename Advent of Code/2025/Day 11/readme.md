**Problem 1**

Problem want: Find number of path from 'you' to 'out'

We can solve by using dfs to search for all path from 'you' to 'out'.

To count how many path, we create dictionary 'cnt' while cnt[i] means how many way you can travel to node 'i'.

In my case, I reverse the edge and search from 'out' to 'you

**Problem 2**

The problem statement changed to find the number of path that pass from 'svr' to 'out' and also pass through 'dac' and 'fft'.

At first, I was thinking about checking that I passed 'fft' and 'dac' or not, but that's make waste my time about finding the suitable algorithm.

So, I start thinking the opposite way of the problem.

```
What's about how many ways to go to 'out' without passing 'dac' and how many ways for 'fft'?
```

From 'svr' there are n ways to go to 'out'.

From 'svr' to 'out' without passing 'dac' there are x ways and for 'fft' there are y ways.

So, from 'svr' -> 'out' there are n-x-y ways.

Then we can use dfs for 4 times and stop when find 'dac' or 'fft'.

1. All from 'svr' to 'out'
2. Without 'fft'
3. Without 'dac'
4. Without both of them

Then result x = (1) - (2) - (3) + (4) since on case (2), and (3) there add path that doesn't pass both 'fft' and 'dac' for 2 times so we add (4) to cancel it.




