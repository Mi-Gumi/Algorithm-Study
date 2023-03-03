num_of_province = int(input())

requests = list(map(int, input().split()))
total_budget = int(input())

left = 0
right = max(requests)

current_max = 0

while left <= right:
    mid = (left + right) // 2
    is_max = 0

    # 요청받은 예산을 하나씩 보며 임의로 정한 상한액보다 작으면 요청 예산을 그대로,
    # 요청 예산이 임의 상한액보다 크면 상한액만큼만 더해줘 임시 최대 예산 값을 얻음
    for request in requests:
        if request <= mid:
            is_max += request

        else:
            is_max += mid

    # 예산을 최대한 써야 하므로, 이전 최대 예산과 새로 얻은 최대 예산 값을 비교해 더 큰 것 선택
    current_max = max(is_max, current_max)

    # 임시 최대 얘산이 총 예산을 넘어선다면, 임의 상한액의 최대값을 줄이고
    # 넘어서지 않는다면 임의 상한액의 최소값을 올려 다시 탐색해 예산을 넘어서지 않는 범위 내에서의 최대 상한액을 구함
    if is_max > total_budget:
        right = mid - 1
    else:
        left = mid + 1

print(right)