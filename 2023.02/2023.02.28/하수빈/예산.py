import sys
input = sys.stdin.readline

N = int(input())
cost = list(map(int, input().split()))
max_cost = int(input())
ans = 0
start = 0
end = max(cost)

# 총 예산이 예산 한계보다 크다면
if sum(cost) > max_cost:
    # 이분탐색 시작점이 끝점보다 작다면 반복
    while start <= end:
        # 중간 지점은 시작점 + 끝점 // 2
        mid = (start + end) // 2
        # 예산 합산
        sum_cost = 0
        # 예산 합은 중간지점과 c중 작은 것으로 합산
        for c in cost:
            sum_cost += min(c, mid)
        
        # 예산 합에 따라 시작 지점과 끝 지점 조정
        if sum_cost > max_cost:
            end = mid - 1
        else:
            start = mid + 1

# 끝 지점 출력
print(end)