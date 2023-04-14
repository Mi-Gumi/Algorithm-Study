# [Gold V] 최소비용 구하기 - 1916 

[문제 링크](https://www.acmicpc.net/problem/1916) 

### 성능 요약

메모리: 126264 KB, 시간: 288 ms

### 분류

그래프 이론, 데이크스트라

### 문제 설명

<p>N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.</p>

### 입력 

 <p>첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.</p>

<p>그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.</p>

### 출력 

 <p>첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.</p>

---
### Solution
```python
import sys
import heapq
input = sys.stdin.readline



def dijkstra(start):
    # 갈 도시 의 수, 최소 비용을 위해 가장 큰 값으로
    heap_q = []
    # 비용과 도시
    heapq.heappush(heap_q, (0, start))
    visited[start] = 0

    # 모든 도시를 방문하면 종료
    while heap_q:
        e, s = heapq.heappop(heap_q)
        
        # 방문 한 곳에 드는 비용이 더 현재가 더 낮으면 스킵
        if visited[s] < e:
            continue
        
        for ns, ne in bus[s]:
            nd = e + ne

            if visited[ns] > nd:
                heapq.heappush(heap_q, (nd, ns))
                visited[ns] = nd

# 도시의 개수
N = int(input().strip())
# 버스의 개수
M = int(input().strip())
# 이차원 배열로 이동 간 금액 찾기
bus = [[] for _ in range(N+1)]
# 방문체크, 도시의 개수가 1000개. set은 시간초과 날거 같음
visited = [1e9] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    
    bus[a].append((b, c))

start, end = map(int, input().split())

dijkstra(start)

print(visited[end])
