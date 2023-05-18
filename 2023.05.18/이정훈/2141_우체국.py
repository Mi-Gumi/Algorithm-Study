import sys
input = sys.stdin.readline

n = int(input().strip())

X = [(0, 0)]*(n)

total = 0
for i in range(n) :
    x, a = map(int,input().split())
    X[i] = (x, a)
    total += a

X.sort(key=lambda x:x[0])
# 양 옆으로 인구수가 비슷

people = 0
half = total/2
for i in range(0, n) :
    people += X[i][1]
    if people >= half :
        ans = X[i][0]
        break

print(ans)
