from sys import stdin, maxsize


def calculate(start_city, current_city, cost, visited):

    global min_cost

    if len(visited) == N:
        if costs[current_city][start_city]:
            min_cost = min(min_cost, cost + costs[current_city][start_city])
            return

    for next_city in range(N):

        if costs[current_city][next_city] and next_city != start_city and next_city not in visited:
            visited.append(next_city)
            calculate(start_city, next_city, cost + costs[current_city][next_city], visited)
            visited.pop()


N = int(stdin.readline())

costs = [list(map(int, stdin.readline().split())) for _ in range(N)]

min_cost = maxsize

for start in range(N):
    calculate(start, start, 0, [start])

print(min_cost)
