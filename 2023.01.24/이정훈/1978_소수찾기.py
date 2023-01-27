N = int(input())
numbers = list(map(int,input().split()))
cnt = 0
for number in numbers :
    for i in range(2,number) :
        if number%i == 0 :
            break
    else :
        if number != 1 :
            cnt += 1
print(cnt)