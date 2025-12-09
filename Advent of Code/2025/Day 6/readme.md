**Problem 1**

Problem statement : Calculate value by the column.

for each column, find the operator ( add or multiply )

Solve for each column by iterate

```
for j in range(h):
	for i in range(w):
		res = res [op] value[i][j] 
```

**Problem 2**

The problem statement : Calcute, but the number is order in vertical.

We split each column into box then get value i by the column of the box.

The example input.

```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

Split into 

```
index   012 | 012 | 012 | 012
		123 | 328 |  51 | 64 
		 45 | 64  | 387 | 23 
		  6 | 98  | 215 | 314
```

For each box, get the value of the index and append into array then calculate it later.

```
all_box = []

for box in boxes:
	this_box = []
	for i in range(w):
		v = 0
		for j in range(h):
			v = v*10 + val[h][w]
		this_box.add(v)
	add_box.add(this_box)
```