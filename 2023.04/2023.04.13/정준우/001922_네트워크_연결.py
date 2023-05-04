# 크루스칼을 이용한 최소 신장 트리 생성
from sys import stdin


def find_parent(parent, x):

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


num_of_computers = int(stdin.readline())
num_of_cables = int(stdin.readline())

parent = [i for i in range(num_of_computers + 1)]

total_cost = 0

link_list = []

for _ in range(num_of_cables):
    linked_1, linked_2, cost = map(int, stdin.readline().split())

    link_list.append((cost, linked_1, linked_2))

link_list.sort()

for cost, linked_1, linked_2 in link_list:

    if find_parent(parent, linked_1) != find_parent(parent, linked_2):
        union(parent, linked_1, linked_2)
        total_cost += cost

print(total_cost)
