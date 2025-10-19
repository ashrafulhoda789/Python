def ok(num):
    cnt = 0
    while num%2 != 1:
        num //= 2
        cnt += 1
    return cnt

n = int(input())
l = list(map(int, input().split()))

i = 0
mn = 10 ** 100
for i in range(0,n):
    num = l[i]
    cnt = ok(num)
    mn = min(mn,cnt)

print(mn)
