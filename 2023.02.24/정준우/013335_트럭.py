from collections import deque

trucks, bridge_length, limit_load = map(int, input().split())

weights = list(map(int, input().split()))

# 다리 길이만큼 요소를 가진 데크를 만들어두고,
# 트럭이 위치한 곳이면 트럭의 무게, 트럭이 위치하지 않은 곳의 값은 0으로 둬 한칸씩 이동하는 느낌
now = deque(0 for _ in range(bridge_length))

# 처음은 무조건 트럭이 올라갈 수 있으니 시간을 1로 두고 데크의 앞부분 0 제거 후 트럭 무게 추가
now.popleft()
now.append(weights.pop(0))

time = 1

# 대기하는 트럭이 없을 때까지
while weights:

    # 다음 트럭이 다리 위에 올라와도 총 무게가 최대 하중보다 낮다면, 데크의 앞 부분을 제거하고 다음 트럭의 무게 추가
    if sum(now) + weights[0] <= limit_load:
        now.popleft()
        now.append(weights.pop(0))

    # 다음 트럭이 올라왔을 때 총 무게가 최대 하중을 넘어가버린다면, 일단 데크의 앞 부분 제거
    else:
        now.popleft()

        # 만약 트럭이 다리 끝부분에 있어서 무게가 제거되어 다음 트럭이 바로 올라와도 된다면 다음 트럭의 무게 추가
        if sum(now) + weights[0] <= limit_load:
            now.append(weights.pop(0))
        # 여전히 다음 트럭이 못 올라온다면 0 추가
        else:
            now.append(0)

    # 과정 하나 거치면 시간 + 1
    time += 1

# while weights 로 인해 마지막 트럭이 다리 위에 올라가면 반복이 중단되니,
# 마지막 트럭이 다리를 빠져나갈 때 필요한 시간을 더한 후 출력
time += bridge_length

print(time)