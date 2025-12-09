f = open('input.txt', 'r').read().split('\n')

res = 0
coordinates = []
for i in f:
    x, y = map(int, i.split(','))
    coordinates.append([x,y])

def calc(a,b,c,d):
    e = abs(a-c)+1
    f = abs(b-d)+1
    return e*f

n = len(coordinates)
for i in range(n):
    x1,y1 = coordinates[i]
    for j in range(i+1,n):
        x2, y2 = coordinates[j]
        res = max(res, calc(x1,y1,x2,y2))
        
print(res)