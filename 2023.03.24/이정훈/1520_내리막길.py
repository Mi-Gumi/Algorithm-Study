import sys 
input = sys.stdin.readline

def dfs(si, sj) :
    if si == N-1 and sj == M-1 :
        return 1
    possible_cnt = 0
    for di, dj in d :
        ni, nj = si + di, sj + dj
        if 0<= ni < N and 0<= nj < M :
            if target <= road[ni][nj] < road[si][sj] :
                if possible[ni][nj] >= 0 :
                    possible_cnt += possible[ni][nj]
                else :
                    possible_cnt += dfs(ni, nj)
    possible[si][sj] = possible_cnt
    return possible_cnt

N, M = map(int,input().split())

road = [list(map(int,input().split())) for _ in range(N)]
possible = [[-1]*M for _ in range(N)]
d = ((0,1),(1,0),(0,-1),(-1,0))
target = road[N-1][M-1]


print(dfs(0,0))





# N, M = map(int,input().split())

# road = [list(map(int,input().split())) for _ in range(N)]
# possible = [[True]*M for _ in range(N)]
# stack = []
# stack.append((0,0,road[0][0]))
# cnt = 0
# while stack :
#     i, j , last = stack.pop()
#     if i == N-1 and j == M-1 :
#         cnt += 1
    
#     for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
#         ni, nj = i + di, j + dj
#         if 0<= ni < N and 0<= nj < M and possible[ni][nj]:
#             if road[ni][nj] < last :
#                 stack.append((ni,nj,road[ni][nj]))
# print(cnt)