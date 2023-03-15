import sys


# 이진탐색으로 공유기 사이의 거리를 늘리거나 줄여가며 조건에 맞는 최적의 위치 탐색
def router_interval():
    # 공유기 사이 최소 거리는 1, 최대 거리는 양 끝 집 사이의 거리
    left = 1
    right = homes[-1] - homes[0]

    while left <= right:
        interval = (left + right) // 2

        # 첫 집에 놓고 시작
        current_home = homes[0]

        installed_router = 1

        # 현재 있는 집에서 지정한 공유기 사이 거리 이상에 집이 있다면 그 곳에 공유기 추가 설치
        for home in range(1, num_of_homes):
            if current_home + interval <= homes[home]:
                installed_router += 1
                current_home = homes[home]

        # 임의로 설치해본 공유기 수가 실제 공유기 수 이상이라면, 공유기 사이 거리를 늘려본다
        if installed_router >= num_of_routers:
            left = interval + 1
            # 지금까지 탐색해본 설치 가능한 거리 중에서는 최대기 때문에 일단 갱신
            max_interval = interval

        # 임의로 설치해본 공유기 수가 실제 공유기 수보다 적으면, 공유기 사이 거리를 좁혀본다
        else:
            right = interval - 1

    return max_interval


num_of_homes, num_of_routers = map(int, sys.stdin.readline().split())

homes = []

for _ in range(num_of_homes):
    homes.append(int(sys.stdin.readline()))

# 집 위치 입력값이 순서대로가 아니므로 정렬
homes.sort()

print(router_interval())
