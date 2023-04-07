import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def melting(): # 빙산 녹는 것
    new_board = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: continue
            melt_cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if board[nx][ny] == 0:
                    melt_cnt += 1
            new_board[i][j] = max(0, board[i][j]-melt_cnt)
    return new_board

N,M = map(int,input().split())
board =[list(map(int,input().split())) for _ in range(N)]
answer = 0
while True:
    answer += 1
    board = melting()
    cnt = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    # bfs가 2번 돌면 정답출력, 1번이면 다음 년도까지 진행, 0이면 0출력
    for i in range(N): 
        for j in range(M):
            if board[i][j] != 0 and visited[i][j] == 0:
                if cnt == 1:
                    print(answer)
                    exit()
                visited[i][j] = -1
                queue = deque()
                queue.append([i,j])
                while queue:
                    x,y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and board[nx][ny] != 0:
                            queue.append([nx,ay])
                            visited[ax][ay] = -1
                cnt += 1
    if cnt == 0:
        print(0)
        exit()