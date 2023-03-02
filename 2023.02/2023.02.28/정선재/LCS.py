import sys
input = sys.stdin.readline

A = list(map(str,input()))
B = list(map(str,input()))
flag = 1
max_cnt = 0
while flag:
    i = 0
    j = 0
    cnt = 0

    if A[i] != B[j]:
        j +=1

print(max_cnt)
