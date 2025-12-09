f = open('input.txt', 'r').read().split('\n')

X = []
Y = []
Z = []

for line in f:
    x,y,z = map(int, line.split(','))
    X.append(x)
    Y.append(y)
    Z.append(z)
    
n = len(f)
arr = []
from math import sqrt
def dist(a,b,c,d,e,f):
    return sqrt((a-d)**2 + (b-e)**2 + (c-f)**2)
    
for i in range(n):
    for j in range(i+1, n):
        d = dist(X[i],Y[i],Z[i], X[j],Y[j],Z[j])
        arr.append([d,i,j])

arr.sort()

# DSU

parent = [i for i in range(n)]
size = [1]*n

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    return x
    
def unite(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    parent[y] = x
    size[x] += size[y]

for i in range(1000):
    d,a,b = arr[i]
    unite(a,b)

vis = [0] * n
comp_size = []
for i in range(1000):
    p = find(i)
    if vis[p]:
        continue
    vis[p] = 1
    comp_size.append(size[p])

comp_size.sort()
print(comp_size[-1] * comp_size[-2] * comp_size[-3])