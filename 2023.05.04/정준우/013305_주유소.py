from sys import stdin


num_of_cities = int(stdin.readline())

length_of_roads = list(map(int, stdin.readline().split()))

price_of_oil = list(map(int, stdin.readline().split()))

cost = 0

min_cost = price_of_oil[0]

# 처음에는 첫 번째 도시 가격으로 최소한 두 번째 도시까지 갈 기름은 넣고 출발
# 이후에는 다음 도시의 기름 가격을 보고,
# 현재 도시보다 싸다면 현재 도시에서 최소한의 기름만 넣고 출발
# 현재 도시의 기름값이 더 싸다면, 그 다음 도시까지의 거리만큼 기름 넣고 출발
# 반복
for city in range(num_of_cities - 1):

    if price_of_oil[city] < min_cost:
        min_cost = price_of_oil[city]

    cost += min_cost * length_of_roads[city]

print(cost)
