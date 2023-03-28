N = int(input())

eggs = [list(map(int,input().split())) for _ in range(N)]

ans = 0

def check(): # 부서진 계란을 파악한다
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    
    return cnt

def dfs(now):
    global ans
    if now == N: # 마지막 계란을 잡을 경우 stop
        ans = max(ans, check()) # 부서진 계란의 max값을 찾아본다
        return
    
    
    # 아래는 계란을 부수는 작업을 진행
    stiff, weight = eggs[now]
    if stiff<=0:
        dfs(now+1) # 현재 계란이 부셔져있을경우 다음계란으로
    else:
        is_all_broken = True
        for i in range(N):
            if now != i and eggs[i][0] > 0:
                is_all_broken = False
                eggs[now][0] = stiff - eggs[i][1]
                eggs[i][0] = eggs[i][0] - weight
                dfs(now + 1) # 계란을 계속 부수기
                eggs[now][0] = stiff
                eggs[i][0] = eggs[i][0] + weight
        if is_all_broken:
            dfs(N)
    pass


dfs(0)
print(ans)