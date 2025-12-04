**Problem 1**

Given a set of range L-R.

In the range L-R we need to find all value that can be form by some sequences of digit occur twice.

Ex. 998-1017 There is 1 number from the condition which is 1010 made by 10, 10.

To solve the problem, We start by looping through L-R and check each value.

```
for i in range(L, R):
	let left = first half of i.
	if concatenate(left, left) == i:
		result += i
```

**Problem 2**

The statement change to find the value that is made by sequences of number occur twice or more.

Ex. 998-1017 There are 2 number from the condition.

1. 999 made by 9, 3 times
2. 1010 made by 10, 2 times.

So on value in range L-R, let it be 'curr'.

We find the length of 'curr' (let it be n) then find all factor and for each factor, try to form the number by concatenate them n/factor times.

Example: curr = 123412341234

```
curr = 123412341234
length = 12, factor = [1, 2, 3, 4, 6]

factor = 1
segment = curr[:1] = 1
Number = segment * times = '1' * 12/1 = 111111111111

factor = 2
segment = 12
Number = segment * times = '12' * 12/2 = 121212121212

factor = 3
segment = 123
Number = '123' * 12/3 = 123123123123

factor = 4
segment = 1234
Number = '1234' * 12/4 = 12341213412341234
```

After found, add to result.
