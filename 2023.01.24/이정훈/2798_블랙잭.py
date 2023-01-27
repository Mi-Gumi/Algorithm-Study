import sys
input = sys.stdin.readline
N, M = map(int,input().split())
cards = list(map(int,input().split()))
arr = set()
for i in range(len(cards)) :
    for j in range(len(cards)) :
        for k in range(len(cards)) :
            if i != j and j != k and k != i :
                sum_n = cards[i] + cards[j] + cards[k]
                if sum_n <= M :
                    arr.add(sum_n)
ans = max(arr)
print(ans)