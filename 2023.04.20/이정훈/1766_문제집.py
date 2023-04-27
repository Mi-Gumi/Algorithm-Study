from heapq import heappop, heappush
import sys
input = sys.stdin.readline


n, m = map(int,input().split())

info = [[] for _ in range(n+1)]
D = [0]*(n+1)
for _ in range(m) :
    a, b = map(int,input().split())
    info[a].append(b)
    D[b] += 1

# 힙큐를 쓰되 진입차수가 0인 문제를 넣고 가중치는 문제번호

Q = []
for i in range(1, n+1) :
    # 선행문제가 없는 문제들
    if D[i] == 0 :
        heappush(Q,i)


while Q :
    # 알아서 문제번호가 낮은 번호가 pop 됨
    now = heappop(Q)
    print(now, end=' ')
    # 이 문제를 풀고 풀어야 하는 문제들
    for nxt in info[now] :
        D[nxt] -= 1
        # 선행 문제를 다 풀었다면 힙푸시
        if not D[nxt] :
            heappush(Q,nxt)
