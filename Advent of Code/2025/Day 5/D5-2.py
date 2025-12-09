cnt = 0
ran = open('input.txt', 'r').read().split()
ran =  [list(map(int, a.split('-'))) for a in ran] 
ran.sort()

# merge interval

new_range = [ran[0]]
for i in range(1,len(ran)):
    prev = new_range[-1]
    curr = ran[i]
    if prev[1] < curr[0]:
        new_range.append(curr)
    else:
        new_range[-1][1] = max(new_range[-1][1], curr[1])
        
for i in new_range:
    cnt += i[1] - i[0] + 1

print(cnt)