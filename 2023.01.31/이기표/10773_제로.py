import sys
input = sys.stdin.readline

T =  int(input())

arr = []
for t in range(T):
    n = int(input())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)
print(sum(arr))