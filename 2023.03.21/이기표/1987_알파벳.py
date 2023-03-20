import sys
input = sys.stdin.readline
R, C = map(int, input().split())
# input 알파벳을 정수로 변환해 처리
arr = [list(map(lambda x: (ord(x) - 65), input().rstrip())) for _ in range(R)]
# 알파벳의 개수만큼 방문처리
visited = [0] * 26
visited[arr[0][0]] = 1
cnt = 0
def dfs(i, j, depth):
    global cnt
    cnt = max(cnt, depth) # 정답 비교
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni = i + di
        nj = j + dj
        if ni < 0 or nj < 0 or ni >= R or nj >= C:
            continue
        if visited[arr[ni][nj]]:
            continue
        # 방문처리를 해주며 해당하는 알파벳에 대해 중복 처리
        visited[arr[ni][nj]] = 1
        dfs(ni, nj, depth+1)
        visited[arr[ni][nj]] = 0 # 동일 선상에서 중복 제거 후 다시 탐색
    return cnt
print(dfs(0, 0, 1))

