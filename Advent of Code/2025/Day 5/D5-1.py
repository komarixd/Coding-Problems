from bisect import *

# input 2 = ingredient id
# input 1 = range

ingre = list(map(int, open('input2.txt', 'r').read().split()))
ingre.sort()

n = len(ingre)
fresh = [0 for _ in range(n)]

cnt = 0
ran = open('input.txt', 'r').read().split()
for iiii in ran:
    l,r = map(int, iiii.split('-'))
    i1 = bisect_left(ingre, l)
    i2 = bisect_left(ingre, r+1)
    for i in range(i1,i2):
        fresh[i] = 1

print(sum(fresh))
