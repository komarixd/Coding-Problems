res = 0
from math import ceil,floor
f = open('input.txt', 'r').read().split(',')
for i in f:
    left, right = i.strip().split('-')
    start = 10**ceil(len(left)/2)
    start //= 10
    left = int(left)
    right = int(right)
    while True:
        curr = int(str(start) + str(start))
        if curr >= left and curr <= right:
            res += curr
        if curr > right:
            break
        start += 1
    
    
print(res)