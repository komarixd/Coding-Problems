**Problem 1**

Problem statement : Find the largest rectangle can be formed.

Just check all pair of coordinates.

Rectangle size = (x2-x1+1) * (y2-y1+1)  For x1<x2 and y1<y2

**Problem 2**

Problem statement is same, but rectangle need to be in the closed area.

The idea is to draw line aroud area and fill its inside then check for each pair of rectangle is in the area or not.

Here is the *key idea*.

Since the number is *very large*, we need to minimize the number so we can solve the problem with lower time complexity and memory space.

```
Example of input
93150,72594
92813,72594
92813,73464
91858,73464
91858,74283
90857,74283
```

The input is around 500 line and all coordinate are connected to each other. (Every x, y value occur 2 times so there are 500 distinct number)

We collect all distinct number and sort it in ascending order.

For example,

```
126547,442
1234,442
1234,598887
126547,598887

Will be minimized into

3,1
2,1
2,4
3,4
```

Now we only have 500 values, so size of the map will only be 500x500.

We observe that the input was already arranged to be connected. So we can draw the line by iterate through the new coordinates array.

```
px, py = new_coords[0]

for i in range(1,n):
    cx, cy = new_coords[i]
    if cx == px: # if it is connected vertically
        for j in range(min(cy,py), max(cy,py)+1):
            grid[j][cx] = 1
    else: # horizontally
        for j in range(min(cx,px), max(cx,px)+1):
            grid[cy][j] = 1
    px = cx
    py = cy
```

Then instead of filling the inside area, we fill the outside area of the grid with 0 to indicate that it is outside.

```
# My solution use BFS
movex = [0,0,1,-1]
movey = [1,-1,0,0]

q = queue.deque([[0,0]])
grid[0][0] = 0

while q:
    i, j = q.popleft()
    for k in range(4):
        ni = i + movey[k]
        nj = j + movex[k]
        if 0 <= ni < sz and 0 <= nj < sz:
            if grid[ni][nj] == 2: 
                grid[ni][nj] = 0
                q.append([ni, nj])
```

After that, we can try to match all pair of coordinates and find the maximum value.

*Note* that the coordinate that contain 0 inside the rectangle means that rectangle can't be formed.

```
for i in range(len(new_coords)):
    for j in range(i+1, len(new_coords)):
        if (check(new_coords[i], new_coords[j])): # check function check that there is 0 inside rectangle or not.
			x1,y1 = coordinates[i]
			x2,y2 = coordinates[j]
            res = max(res, calc(x1,y1,x2,y2))
```

The time complexity will be 500^4. 

Takes 1 min to run on python(my code). You can try to make better solution.


