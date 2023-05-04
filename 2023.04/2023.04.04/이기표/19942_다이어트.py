'''
첫 번째 줄에 최소 비용을 출력하고,
두 번째 줄에 조건을 만족하는 최소 비용 식재료의 번호를 공백으로 구분해 오름차순으로 한 줄에 출력한다.
같은 비용의 집합이 하나 이상이면 사전 순으로 가장 빠른 것을 출력한다.
'''
def dfs(n, p, f, s, v, cost, check):
    global min_ans, min_check
    if n == N:
        if not(p >= P and f >= F and s >= S and v >= V):
            return
        if min_ans >= cost:
            if min_ans == cost:
                min_check = sorted((min_check, check))[0]
                return
            min_ans = cost
            min_check = check
        return

    dfs(n+1, p+arr[n][0], f+arr[n][1], s+arr[n][2], v+arr[n][3], cost+arr[n][4], check+[n+1])
    dfs(n + 1, p, f, s, v, cost, check)


N = int(input())
# 단백질 지방 탄수화물 비타민
P, F, S, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
min_ans=10**9
min_check = []
dfs(0, 0, 0, 0, 0, 0, [])
if min_ans == 10**9:
    print(-1)
else:
    print(min_ans)
    print(*min_check)
