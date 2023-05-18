N = int(input())


Xs = []
num = 0
for i in range(N):
    x, a = map(int,input().split())
    Xs.append([x,a])
    num += a

Xs.sort(key=lambda x:x[0])
cnt = 0
for a, b in Xs:
    cnt += b
    if cnt >= num/2:
        print(a)
        break