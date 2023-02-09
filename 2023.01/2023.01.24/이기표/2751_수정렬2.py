import sys
T = int(sys.stdin.readline())

arr = []
for t in range(T):
    n = int(sys.stdin.readline())
    arr.append(n)

arr = sorted(arr)
for i in arr:
    print(i)
