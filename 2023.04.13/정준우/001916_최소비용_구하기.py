# 다익스트라
from sys import stdin
from heapq import *


def gumi_bus_not_good(depart, arrive):

    queue_for_dijkstra = []
    queue_for_dijkstra.append((0, depart))

    cost = [1e9] * (num_of_cities + 1)
    cost[depart] = 0

    while queue_for_dijkstra:

        current_cost, current_city = heappop(queue_for_dijkstra)

        if cost[current_city] < current_cost:
            continue

        for next_city, cost_to_next in adj_matrix[current_city]:

            if cost[next_city] > current_cost + cost_to_next:
                cost[next_city] = current_cost + cost_to_next

                heappush(queue_for_dijkstra, (current_cost + cost_to_next, next_city))

    return cost[arrive]


num_of_cities = int(stdin.readline())
num_of_buses = int(stdin.readline())

adj_matrix = [[] for _ in range(num_of_cities + 1)]

for _ in range(num_of_buses):
    depart, arrive, cost = map(int, stdin.readline().split())

    adj_matrix[depart].append((arrive, cost))

depart_city, target_city = map(int, stdin.readline().split())

print(gumi_bus_not_good(depart_city, target_city))
