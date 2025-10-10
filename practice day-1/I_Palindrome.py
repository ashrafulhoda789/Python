num = int(input())

sum = 0
tmp = num
while tmp != 0:
    r = tmp%10
    sum = sum*10 + r
    tmp = tmp // 10

print(sum)
if num == sum:
    print('YES\n')
else:
    print('NO\n')