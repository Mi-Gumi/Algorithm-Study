'''
1. dfs 탐색을 통해 탐색할 수 있는 모든 경우를 탐색
2. 모든 도시를 방문한 경우 최소값 찾기
3. 현재 비용이 정답 후보 비용보다 큰 경우 종료(백트래킹)
'''

def dfs(idx, n_idx, cursum, visited):
    global ans

    if ans <= cursum: # 현재 비용 보다 큰 경우 종료
        return

    if len(visited) == N:
        # 최소값 찾기
        if arr[n_idx][idx]:
            ans = min(ans, cursum + arr[n_idx][idx])
        return

    for i in range(N):
        # 동일한 인덱스 도시 비용이 0이 아니거나와 방문한 적이 없으면 탐색
        if i != idx and arr[n_idx][i] != 0 and i not in visited:
            visited.append(i)
            dfs(idx, i, cursum+arr[n_idx][i], visited)
            visited.pop()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 10**9
for i in range(N):
    dfs(i, i, 0, [i])

print(ans)