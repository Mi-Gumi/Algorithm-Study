from collections import deque
# 0 : 북
# 1 : 동
# 2 : 남
# 3 : 서
# row 방향 서 -> 동
# col 방향 북 -> 남

# d = (0,3,2,1) # 반시계로 회전
d = (0,1,2,3) # 시계방향...
dxy = ((-1,0),(0,1),(1,0),(0,-1))

def clean(i,j,l):
    que = deque()
    que.append((i,j,l))
    cnt = 0
    while que:
        x,y,Look = que.popleft() 
        
        for k in range(Look-1 ,Look-4 - 1, -1): # 반시계로 돌기 때문에 range를 이렇게 설정해둠
            nx = x + dxy[k][0]
            ny = y + dxy[k][1]
            if room[nx][ny] == 1 or room[nx][ny] == 9:
                continue # 벽이거나 청소를 했을 경우 continue
            room[nx][ny] = 9 # 청소한 영역으로 확인
            que.append((nx,ny,(k+4)%4)) # 위치 정보 및 방향정보를 수집
            cnt += 1 # 방 청소 한 영역을 cnt
            break
        else: # 탐색을 했을 때 청소가능한 영역이 없을경우 뒤로 가야함
            nx = x + dxy[Look - 2][0]
            ny = y + dxy[Look - 2][1]
            if room[nx][ny] == 1: # 벽에 부딛혔을 경우 break
                break
            que.append((nx,ny,Look)) # 아닐경우 append

    return cnt

N, M = map(int,input().split())
a, b, diraction = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(N)]


room[a][b] = 9 # 청소한 영역을 9로 설정
ans = 1
ans += clean(a,b,diraction) # 위치정보 및 diraction 정보 제공
print(ans)