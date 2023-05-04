from collections import deque

T = int(input()) # tc
for tc in range(T):
    N, K = map(int, input().split()) # 건물의 개수 N, 건물간의 건설순서 규칙의 총 개수 K
    time = [0] + list(map(int, input().split())) # 각 건물당 건설에 걸리는 시간
    graph = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    for _ in range(K): 
        X, Y = map(int, input().split()) # X, Y => 건물 X 지은 다음 Y 짓기
        graph[X].append(Y) 
        indegree[Y] += 1
    W = int(input()) # 승리하기 위해 건설해야 할 건물 번호
    sm = 0

    # print(graph)
    # print(indegree)

    def topology_sort(): # 위상정렬 중 순서대로 나열하지 않고 최소 시간이 드는 곳으로 
        global sm
        result = []
        q = deque() 

        for i in range(1, N+1): # 진입차수 0인 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        
        while q: 
            # print('start: ', q)
            mn = 1000000000
            for qq in range(len(q)):
                # print(qq, q[qq], time[q[qq]])
                if mn > time[q[qq]]:
                    mn = time[q[qq]]
                    now = q[qq]
            # now = q.popleft()
            q.remove(now)
            result.append(now)

            for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

            if now == W: # 승리 건물이면 종료
                break

            # print(now)
            # print(result)

        for i in result:
            # print(i, time[i])
            sm += time[i]

    topology_sort()

    print(sm) # 건물 W를 건설 완료하는데 드는 최소 시간 출력

