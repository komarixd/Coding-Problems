import queue
f = open('input.txt', 'r').read().split('\n')

res = 0
coordinates = []
for i in f:
    x, y = map(int, i.split(','))
    coordinates.append([x,y])
coordinates.append(coordinates[0])

def calc(a,b,c,d):
    e = abs(a-c)+1
    f = abs(b-d)+1
    return e*f

n = len(coordinates)
lx = 100000000
hx = 0
ly = 100000000
hy = 0

num_list = []
for i in coordinates:
    x,y = i
    x = x
    y = y
    if x not in num_list:
        num_list.append(x)
    if y not in num_list:
        num_list.append(y)
        
num_list.sort()
new_coords = []
for i in coordinates:
    x,y = i
    newx = num_list.index(x)
    newy = num_list.index(y)
    new_coords.append([newx, newy])
    
sz = len(num_list) + 1
grid = [[2 for _ in range(sz)] for _ in range(sz)]

px, py = new_coords[0]

for i in range(1,n):
    cx, cy = new_coords[i]
    if cx == px:
        for j in range(min(cy,py), max(cy,py)+1):
            grid[j][cx] = 1
    else:
        for j in range(min(cx,px), max(cx,px)+1):
            grid[cy][j] = 1
    px = cx
    py = cy

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

def check(a,b):
    x1 = min(a[0], b[0])
    x2 = max(a[0], b[0])
    y1 = min(a[1], b[1])
    y2 = max(a[1], b[1])
    for j in range(x1, x2+1):
        for i in range(y1, y2+1):
            if grid[i][j] == 0:
                return False
    return True

print(1)

for i in range(len(new_coords)):
    for j in range(i+1, len(new_coords)):
        if (check(new_coords[i], new_coords[j])):
            res = max(res, calc(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]))

print(res)