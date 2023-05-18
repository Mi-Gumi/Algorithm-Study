from collections import deque
def find_gram():
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 2 :
                return [i,j,n*m]
def zelda(si, sj) :
    global is_gram_find
    Q = deque()
    Q.append((si, sj, 0))
    visited = [[0]*m for _ in range(n)]
    visited[si][sj] = 1
    
    while Q:
        ci, cj, time = Q.popleft()
        if time > t :
            return 'Fail'
        if not is_gram_find and arr[ci][cj] == 2:
            gram[2] = time
            is_gram_find = True
        if (ci, cj) == (n-1, m-1):
            return time

        for di, dj in d :
            ni , nj = ci+di, cj + dj 
            if ni <0 or ni >= n or nj < 0 or nj >= m :
                continue
            if visited[ni][nj] == 1 :
                continue
            if not arr[ni][nj] or arr[ni][nj] == 2:
                Q.append((ni,nj,time+1))
                visited[ni][nj] = 1
                continue
    return 'Fail'

n, m, t = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

d = ((0,1),(1,0),(0,-1),(-1,0))

gram = find_gram()
is_gram_find = False
ans = zelda(0,0)

use_gram_ans = gram[2] + n-1 - gram[0] + m-1 - gram[1]

if ans == 'Fail' :
    if not is_gram_find or use_gram_ans > t or use_gram_ans == n*m :
        print('Fail')
    else :
        print(use_gram_ans)
else :
    if not is_gram_find :
        print(ans)
    else :
        print(min(ans, use_gram_ans))