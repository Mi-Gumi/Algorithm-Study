from sys import stdin
from heapq import *


# 다익스트라
def party_timeeeeeeeee(depart, arrive):

    queue_for_dijkstra = []
    queue_for_dijkstra.append((0, depart))

    distance = [1e9] * (num_of_villages + 1)
    distance[depart] = 0

    while queue_for_dijkstra:

        current_distance, current_village = heappop(queue_for_dijkstra)

        if distance[current_village] < current_distance:
            continue

        for next_village, distance_to_next in adj_matrix[current_village]:

            if distance[next_village] > current_distance + distance_to_next:
                distance[next_village] = current_distance + distance_to_next

                heappush(queue_for_dijkstra, (current_distance + distance_to_next, next_village))

    return distance[arrive]


num_of_villages, num_of_roads, party_spot = map(int, stdin.readline().split())

adj_matrix = [[] for _ in range(num_of_villages + 1)]

for _ in range(num_of_roads):
    depart, arrive, distance = map(int, stdin.readline().split())

    adj_matrix[depart].append((arrive, distance))

son_hae = 0

for student in range(1, num_of_villages + 1):

    # 파티 장소까지 최단거리, 돌아올 때의 최단거리를 더해 총 이동 거리를 비교
    moved_distance = party_timeeeeeeeee(student, party_spot) + party_timeeeeeeeee(party_spot, student)

    if son_hae < moved_distance:
        son_hae = moved_distance

print(son_hae)
