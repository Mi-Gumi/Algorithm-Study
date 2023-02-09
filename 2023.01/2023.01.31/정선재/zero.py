import sys
input = sys.stdin.readline
N = int(input())
_list = []
for i in range(N):
    M = int(input())
    if M != 0:
        _list.append(M)
    elif M == 0:
        _list.pop()


print(sum(_list))

