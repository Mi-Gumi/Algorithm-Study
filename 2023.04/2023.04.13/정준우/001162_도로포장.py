from sys import stdin, maxsize
from heapq import *


num_of_cities, num_of_roads, num_of_pavable_roads = map(int, stdin.readline().split())

adj_matrix = [[] for _ in range(num_of_cities + 1)]

for _ in range(num_of_roads):
    depart, arrive, time = map(int, stdin.readline().split())

    adj_matrix[depart].append((arrive, time))
    adj_matrix[arrive].append((depart, time))

# 도로를 포장한 횟수까지 다루기 위해 2차원 리스트로 생성
# 테케 마지막에 10억 넘는거 넣어놨네
time = [[maxsize] * (num_of_pavable_roads + 1) for _ in range(num_of_cities + 1)]

queue_for_dijkstra = []

# 포장 횟수와 관계없이 시작지점의 시간은 모두 0
for i in range(num_of_pavable_roads + 1):
    time[1][i] = 0

heappush(queue_for_dijkstra, (0, 1, 0))

while queue_for_dijkstra:

    current_time, current_city, paved_roads = heappop(queue_for_dijkstra)

    if time[current_city][paved_roads] < current_time:
        continue

    # 포장 횟수가 남아있다면 해보기
    # 포장하면 다음 도시까지 시간은 0이므로 current_time 으로만 비교
    if paved_roads + 1 <= num_of_pavable_roads:
        for next_city, time_to_next in adj_matrix[current_city]:
            if time[next_city][paved_roads + 1] > current_time:
                time[next_city][paved_roads + 1] = current_time

                heappush(queue_for_dijkstra, (current_time, next_city, paved_roads + 1))

    for next_city, time_to_next in adj_matrix[current_city]:
        if time[next_city][paved_roads] > current_time + time_to_next:
            time[next_city][paved_roads] = current_time + time_to_next

            heappush(queue_for_dijkstra, (current_time + time_to_next, next_city, paved_roads))

# 포천이 N번 도시
print(min(time[-1]))
