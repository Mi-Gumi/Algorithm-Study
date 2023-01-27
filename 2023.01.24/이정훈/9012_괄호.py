T = int(input())

for test_case in range(1,T+1) :
    PS = input()
    cnt = 0
    isValid = True
    for c in PS :
        if c == '(' :
            cnt += 1
        elif c == ')' :
            cnt -= 1
        if cnt < 0 :
            isValid = False
    if cnt != 0 :
        isValid = False
    if isValid :
        print('YES')
    else :
        print('NO')
        