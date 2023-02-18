import sys
from collections import deque
input = sys.stdin.readline

def bfs(y,x): 
    
    global land
    
    pueue = deque()
    
    pueue.append((y,x))
    # 새로운 구역으로 식별
    Map[y][x] = land
    while pueue :
        yy , xx = pueue.popleft()
        for dy, dx in d :
            ny, nx = yy + dy, xx+dx
            #인덱스 체크
            if 0<=nx<M and 0<=ny<N :
                if Map[ny][nx] == 1 :
                    pueue.append((ny,nx))
                    Map[ny][nx] = land
    land += 1


T = int(input())

for tc in range(T) :
    N,M ,K = map(int,input().split())
    
    vechu = [list(map(int,input().split())) for _ in range(K)]
    Map = [[0]*M for _ in range(N)]
    for y,x in vechu :
        Map[y][x] = 1
    # 배추 정보를 2차원 배열에 매핑
    
    land = 2   # 카운트와 구역 구별을 위한 변수

    d = [[0,1],[1,0],[0,-1],[-1,0]]  #델타검색을 위한 좌표증감
    
    # 모든 좌표에서 함수 호출
    for i in range(N) :      
        for j in range(M) :      
            if Map[i][j] == 1 :
                bfs(i,j)

    print(land - 2)