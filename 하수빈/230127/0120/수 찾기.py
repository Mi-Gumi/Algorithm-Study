import sys

N = int(sys.stdin.readline())
num_N = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
num_M = list(map(int, sys.stdin.readline().split()))

for num in num_M:
    for i in num_N:
        if num == 1:
            print(1)
            break
    else:
        print(0)