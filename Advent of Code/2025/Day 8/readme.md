**Problem 1**

Problem statement : Connect the shortest box and find product of the size of component.

Find distance between all box and sort it in ascending order (let the variable name be *dist*).

Connect first 1000 pair. (This can be done by using *DSU* Data structure)

Return product of 3 largest component.

**Problem 2**

Problem statement : What is the last component to be connect to make all box connected.

We do connect all pair in *dist* and change some part of *DSU*

On the merge component function of DSU, we check that we need to merge or it is already merge.

```
def unite(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return 0 # return 0 if it is the same component
    parent[y] = x
    size[x] += size[y]
    return 1 # return 1 if is is different component
```

Then on the loop to connect all pair we update the result.

```
res = 0
for i in range(len(arr)):
    d,a,b = arr[i]
    
    m = unite(a,b)
    if m == 1:
        res = X[a] * X[b]
```

Since the merge will occur if it is on different component so the result we be the last 2 component connected.

