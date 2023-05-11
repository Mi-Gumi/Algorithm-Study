'''
각 칸은 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로
연결할 수 있고 각 칸의 중심끼리 연결
1. 오른쪽 아래 대각선, 오른쪽, 오른쪽 위 대각선 순으로 DFS 탐색 진행
2. 이미 방문한 파이프 경로를 true로 반환해 중복 탐색을 방지
3. 파이프가 빵집에 도달한 경우 탐색 종료
'''
def dfs(i, j):
    global cnt
    # 빵집 도착 / 횟수 증가 후 종료  
    if j == C-1:
        cnt += 1
        return True

    for di, dj in ((-1, 1), (0, 1), (1, 1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
            # 건물이 아닌 경우 탐색
            if arr[ni][nj] == '.':
                visited[ni][nj] = 1
                # 이미 탐색한 파이프 경로인 경우 종료
                if dfs(ni, nj):
                    return True

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
cnt = 0
visited = [[0]*C for _ in range(R)]

# 첫번째 열에서 건물이 아닌 경우 출발
for r in range(R):
    if arr[r][0] == '.':
        dfs(r, 0)
print(cnt)