def factor(num):
    res = []
    for i in range(1, num//2+1):
        if num%i==0:
            res.append(i)
    return res
    
res = 0
f = open('input.txt', 'r').read().split(',')
for i in f:
    left, right = map(int, i.strip().split('-'))
    for curr in range(left, right+1):
        curr = str(curr)
        for t in factor(len(curr)):
            seg = curr[:t]
            num = int(seg * (len(curr)//t))
            if num == int(curr) and num >= left and num <= right:
                res += num
                # print(num)
                break

print(res)