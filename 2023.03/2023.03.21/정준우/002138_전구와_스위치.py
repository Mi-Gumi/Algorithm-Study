import sys


def onoffonoffonoffonoff(init_state, target_state):

    # 첫 전구의 스위치를 누르는 / 안 누르는 두 가지 경우를 봐야하기 때문에 초기 상태를 복사해서 사용
    multiverse = init_state[:]

    press_count = 0

    # 같은 스위치를 여러 번 누른다 해도 횟수만 늘어나지 불가능한 경우가 가능해지지는 않음
    # 스위치를 최소로 누르는 경우는 목표 상태를 만들기 위해 각 스위치를 최대 한 번 누르는 것

    # 현재 탐색중인 전구보다 두 칸 이상 앞에 있는 것은 이미 이전 반복문에서 판단
    # 이후 탐색할 전구는 이후 반복문에서 판단
    # 반복문 하나에서 목표 상태와 같은지 판단해야 할 전구는 바로 앞의 전구
    for bulb in range(1, num_of_bulbs):
        # 바로 앞 전구가 목표 상태와 같다면 다음 반복 진행
        if multiverse[bulb - 1] == target_state[bulb - 1]:
            continue
        # 바로 앞 전구가 목표 상태와 다르다면 조건에 맞게 주변 전구 바꿔주고 누른 횟수 + 1
        else:
            press_count += 1

            for near_bulb in range(bulb - 1, bulb + 2):
                if near_bulb < num_of_bulbs:
                    multiverse[near_bulb] = not multiverse[near_bulb]
    # 반복 결과 목표 상태와 같다졌다면 누른 횟수 반환
    if multiverse == target_state:
        return press_count
    # 아니라면 최대 횟수보다 큰 수 반환
    else:
        return 1e7


num_of_bulbs = int(sys.stdin.readline())

init_state = list(map(int, sys.stdin.readline().strip()))
target_state = list(map(int, sys.stdin.readline().strip()))

# 첫 전구의 스위치를 누르지 않고 탐색
answer = onoffonoffonoffonoff(init_state, target_state)

# 첫 전구의 스위치를 누르면 변하는 전구 적용
init_state[0] = not init_state[0]
init_state[1] = not init_state[1]

# 첫 전구의 스위치를 누르고 나서 탐색
answer = min(answer, onoffonoffonoffonoff(init_state, target_state) + 1)

# 불가능한 경우라 answer가 여전히 큰 수라면 -1 출력
if answer == 1e7:
    print(-1)
else:
    print(answer)
