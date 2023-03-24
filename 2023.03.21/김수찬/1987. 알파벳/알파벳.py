N, M = map(int,input().split())

## 그냥 알파벳을 탐색할 경우 탐색하는 조건이 복잡해짐
## X in list 구문을 사용하지 않고 visited를 사용하기 위해 
## 알파벳을 숫자로 바꿈
texts = [input() for _ in range(N)]
is_used = [False]*26

ans = 0

dx = (1,-1,0,0)
dy = (0,0,1,-1)

def dfs(start, length):
    global ans

    for k in (0,1,2,3):
        nx = start[0] + dx[k]
        ny = start[1] + dy[k]
        if nx<0 or ny<0 or nx>=N or ny>=M: continue
        if is_used[texts[nx][ny]]: continue
        is_used[texts[nx][ny] - ord('A')] = True
        length += 1
        dfs((nx,ny), length)
        is_used[texts[nx][ny] - ord('A')] = False
        length -= 1
    
    ans = max(ans,length)

# 해당 조건에 대해서 dfs 를 진행해서 나아갈 수 있는 max 값 파악 
is_used[texts[0][0]] = True
dfs((0,0), 1)
print(ans)