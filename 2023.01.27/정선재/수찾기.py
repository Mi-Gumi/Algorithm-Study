import sys

input = sys.stdin.readline

N = int(input())

C = set(map(int, input().split()))

M = int(input())

K = list(map(int, input().split()))

for i in K:
    if i in C :
        print(1)
    else:
        print(0)
