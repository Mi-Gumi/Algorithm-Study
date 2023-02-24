a = list(map(str,input()))
b = list(map(str,input()))
ans = []


for i in range(len(a)):
    ans.append(a[i])
    if a[i] == b[-1]:
        if ans[-len(b):] == b:
            for i in range(len(b)):
                ans.pop()


if len(ans) != 0:
    print(*ans, sep ='')
else:
    print('FRULA')