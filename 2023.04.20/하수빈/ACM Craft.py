import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    # 각 건물의 건설 순서 배열
    order = [[] for _ in range(N + 1)]
    # 진입 차수 배열
    cnt = [0] * (N + 1)
    ans = [0] * (N + 1)
    for i in range(K):
        X, Y = map(int, input().split())
        # 건설 순서 추가
        order[X].append(Y)
        # 진입 차수 + 1
        cnt[Y] += 1
    target = int(input())

    q = deque()
    # 큐 초기화
    for i in range(1, N + 1):
        # 진입차수가 0이라면
        if not cnt[i]:
            # 건물의 최종 완성 시간은 건물의 완성시간
            ans[i] = D[i]
            # 큐에 추가
            q.append(i)

    while q:
        now = q.popleft()
        for next in order[now]:
            # 현재 건물의 최종 완성시간과 이전 건물 순서의 완성 시간에서 현재 건물의 완성 시간을 더한 값 중 최대값 선택
            ans[next] = max(ans[now] + D[next], ans[next])
            # 진입 차수 감소
            cnt[next] -= 1
            # 진입 차수가 0이라면 큐에 추가
            if not cnt[next]:
                q.append(next)
    
    print(ans[target])