import sys
sys.setrecursionlimit(10 ** 9)


def who_is_your_mom(someone):

    visited[someone] = 'v'

    # 자식 노드가 방문하지 않은 노드일 경우,
    # 부모 리스트에 해당 자식 노드의 번호를 인덱스로 현재 탐색중인 노드를 부모로 지정
    for children in graph[someone]:
        if visited[children] != 'v':
            parents[children] = someone
            who_is_your_mom(children)


num_of_people = int(input())

graph = {i: [] for i in range(1, num_of_people + 1)}

for _ in range(num_of_people - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (num_of_people + 1)
parents = [0] * (num_of_people + 1)

who_is_your_mom(1)

print(*parents[2:], sep = '\n')
