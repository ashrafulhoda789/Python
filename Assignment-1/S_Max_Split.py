s = input()

cnt = 0
l = []
st = ''

for ch in s:
    st += ch
    if ch == 'L':
        cnt += 1
    else: cnt -= 1

    if cnt == 0:
        l.append(st)
        st = ''

print(len(l))
for st in l:
    print(st)