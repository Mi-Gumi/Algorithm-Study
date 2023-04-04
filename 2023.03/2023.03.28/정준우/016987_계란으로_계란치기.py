import sys


def for_zzim(current_egg):
    global broken_eggs
    # 가장 최근에 오른쪽 끝의 계란을 들었다면 깨진 계란 수 확인 후 종료
    if current_egg == num_of_eggs:
        a_case = 0
        for i in range(num_of_eggs):
            if eggs[i][0] <= 0:
                a_case += 1
        broken_eggs = max(broken_eggs, a_case)
        return

    # 들고 있는 계란이 깨졌다면 다음 계란으로
    if eggs[current_egg][0] <= 0:
        for_zzim(current_egg + 1)
        return

    # 들고 있는 계란 제외하고 모두 깨져있을 때
    all_broken = True
    for target_egg in range(num_of_eggs):
        if target_egg == current_egg:
            continue
        # 깨지지 않은 계란이 있다면 all_broken False로 변경 후 반복 중단
        if eggs[target_egg][0] > 0:
            all_broken = False
            break
    # 모두 깨졌다면, 깨진 계란의 수는 전체 수 - 1
    if all_broken:
        broken_eggs = max(broken_eggs, num_of_eggs - 1)
        return

    # 계란으로 계란 쳐보기
    for target_egg in range(num_of_eggs):
        if target_egg == current_egg:
            continue
        if eggs[target_egg][0] <= 0:
            continue
        # 깨지지 않은 계란 중 하나 골라서 쳐보기
        eggs[current_egg][0] -= eggs[target_egg][1]
        eggs[target_egg][0] -= eggs[current_egg][1]
        for_zzim(current_egg + 1)
        # 과정이 종료되고 나면 다른 계란을 쳐봐야 하기 때문에 재귀 종료 후 내구도 복구
        eggs[current_egg][0] += eggs[target_egg][1]
        eggs[target_egg][0] += eggs[current_egg][1]


num_of_eggs = int(sys.stdin.readline())
eggs = []
broken_eggs = 0

for _ in range(num_of_eggs):
    eggs.append(list(map(int, sys.stdin.readline().split())))

for_zzim(0)

print(broken_eggs)