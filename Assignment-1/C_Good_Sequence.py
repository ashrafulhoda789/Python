n = int(input())
l = list(map(int,input().split()))

l.sort()

sz = 0
i = 0
while i < n :
    num = l[i]
    cnt = 0
    while i < n and l[i] == num:
        cnt += 1
        i += 1
    
    if cnt != num:
        if cnt > num:
            sz += (cnt - num)
        else: sz += cnt

print(sz)