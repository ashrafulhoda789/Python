def ok(num):
    tmp = num
    while tmp != 0:
        r = tmp%10
        if r != 4 and r != 7:
            return False
        tmp = tmp//10
    
    return True

a, b = map(int, input().split())

found = False

for i in range(a,b+1):
    if ok(i) == True:
        print(i,end = ' ')
        found = True
    

if found == False:
    print('-1')