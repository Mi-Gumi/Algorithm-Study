import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(N)]
history = [['']*M for _ in range(N)] # 루트를 저장해 놓을 배열 ( 의미없는 계산을 줄이기 위함 )

# dfs stack으로 구현
stack = []
stack.append((0,0,1,arr[0][0]))  # i, j, depth, route
max_cnt = 0
while stack :
    ci, cj, depth, route = stack.pop()
    max_cnt = max(max_cnt,depth)
    for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
        ni, nj = ci + di, cj + dj
        if 0<= ni < N and 0<= nj < M and arr[ni][nj] not in route :
            new = route + arr[ni][nj]
            # 같은 루트를 밟아온 경우 다시 탐색할 필요가 없으므로 
            if new != history[ni][nj] :
                history[ni][nj] = new   # 루트 저장
                stack.append((ni,nj,depth+1,route + arr[ni][nj])) # 현재 루트에 다음 위치를 추가하여 append
print(max_cnt)


# def dfs(si,sj,k) :
#     global max_cnt
#     if k > max_cnt: 
#         max_cnt = k

#     for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
#         ni, nj = si + di, sj + dj
#         if 0<= ni < N and 0<= nj < M :
#             alpha_idx = ord(arr[ni][nj])-65
#             if  alpha_visited[alpha_idx] == 0 :
#                 alpha_visited[alpha_idx] = 1
#                 dfs(ni,nj,k+1)
#                 alpha_visited[alpha_idx] = 0

# N, M = map(int,input().split())

# arr = [list(input()) for _ in range(N)]
# alpha_visited = [0]*26
# alpha_visited[ord(arr[0][0])-65] = 1
# max_cnt = 1
# dfs(0,0,1)

# print(max_cnt)