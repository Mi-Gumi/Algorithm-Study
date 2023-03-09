import sys
input = sys.stdin.readline


N = int(input())
V = []
top =  list(map(int,input().split()))

for i in range(N-1,-1,-1):

    if top[i] > top[i-1]:
        V.append(0)

    else:
        V.append((i-1)+1)

V = V[::-1]

for j in range(len(V)-1):
    if V[j] != 0 and V[j+1] == 0:
        V[j+1] = V[j]

print(V)
