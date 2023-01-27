import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())

A = set(map(int,input().strip().split()))

M = int(input())

B = list(map(int,input().strip().split()))

for i in B :
    if i in A :
        print(1)
    else :
        print(0)
