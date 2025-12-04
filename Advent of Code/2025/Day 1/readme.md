**Problem 1**

We start at number 50.

The problem input has 2 type.

1. L{x}
2. R{x}

Where x is integer.

They want us to find how many time that the rotation is 0.

Let curr = 50 (start at 50)

For each input.

If input is L{x}, curr will decrease by x. curr = (curr - x) % 100

If input is R{x}, curr will increase by x. curr = (curr + x) % 100

Then count how many 0 occurs.

**Problem 2**

The statement changed to "how many times it pass 0"

For each input we take value {x} and check whether it is 'L'(sign = -1) or 'R'(sign = -1)

Then loop for {x} times and curr += sign.