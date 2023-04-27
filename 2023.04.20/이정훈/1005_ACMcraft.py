from collections import deque
import sys
input = sys.stdin.readline
    
def bfs() :
    craft = deque()
    for i in range(1,n+1) :
        if not D[i] :
            craft.append(i)
            D[i] = -1

    for build in craft :
        max_take_time[build] = take_time[build]
    
    while craft :
        now = craft.popleft()
        if now == w :
            return
        for next in build_order[now] :
            max_take_time[next] = max(max_take_time[next], max_take_time[now] + take_time[next])
            D[next] -= 1

        for i in range(1, n+1) :
            if not D[i] :
                D[i] = -1
                craft.append(i)



T = int(input())
anss = []
for tc in range(1, T+1) :
    n, k = map(int,input().split())

    take_time = [0]+list(map(int,input().split()))
    # 방향 그래프
    build_order = [[] for _ in range(n+1)]
    # 위상
    D = [0]*(n+1)
    for _ in range(k) :
        before, after = map(int,input().split())
        build_order[before].append(after)
        D[after] += 1
    w = int(input())
    # 건물별 선행건물 시간중 가장 오래걸리는 시간
    max_take_time = [0] * (n+1)

    # print(take_time)
    # print(build_order)
    bfs()
    anss.append(max_take_time[w])
print(*anss, sep='\n')