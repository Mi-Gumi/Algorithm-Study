import sys
input = sys.stdin.readline
N = int(input())
height = list(map(int, input().split()))
num = []
left = []
for i in range(N):
    a = height[i]
    left.append(a)
    b = left[-1]
    for j in range(len(left)-1, -1, -1):
        if left[j] > b:
            num.append(j+1)
            break
    else:
        num.append(0)
print(*num)
