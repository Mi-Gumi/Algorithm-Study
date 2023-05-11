'''
가스관은 첫 째열에서 시작해서 마지막 열에서 끝나야 한다. 각 칸은 오른쪽, 오른쪽 위, 오른쪽 아래로 연결할 수 있으며, 경로는 겹칠수도 서로 접할 수도 없다. 설치할 수 있는 파이프라인의 최대 개수는?
'''

def dfs(ci, cj) :
    if cj == c-1 :
        return 1
    # 한 번 탐색한 길은 다시 탐색할 필요가 없다. 
    # 이미 사용했거나 사용할 수 없는 길
    arr[ci][cj] = 'x'
    for di, dj in d :
        ni, nj = ci + di, cj + dj
        if arr[ni][nj] == '.' :
            if dfs(ni,nj) :
                return 1
    return 0

r, c = map(int,input().split())

# 경계값을 체크하지 않기 위해 padding
arr = [list('x'*c)]+[list(input()) for _ in range(r)]+[list('x'*c)]

# 오른쪽 위부터 탐색
d = ((-1,1), (0,1), ( 1, 1))

ans = 0
for i in range(1, r+1):
    ans += dfs(i, 0)
        
print(ans)


''' 스택을 사용한 풀이
r, c = map(int,input().split())

arr = [list('x'*c)]+[list(input()) for _ in range(r)]+[list('x'*c)]

# 오른쪽 아래부터 push 함
d = ((1,1), (0,1), ( -1, 1))

ans = 0
for i in range(1, r+1):
    stack = []
    if arr[i][0] == 'x' :
        continue
    stack.append((i, 0))
    while stack :
        si, sj = stack.pop()
        arr[si][sj] = 'x'
        # 도착
        if sj == c-1 :
            ans += 1
            break
        for di, dj in d :
            ni, nj = si + di, sj + dj
            if arr[ni][nj] == '.' :
                stack.append((ni,nj))
print(ans)
'''