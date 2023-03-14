N = int(input())

yeahsan = list(map(int, input().split()))

budget = int(input())

ans = max(yeahsan)

if sum(yeahsan) >= budget:
    # 이분탐색해보자
    top = ans
    bottom = 0

    while top >= bottom:
        limit = (top + bottom) // 2
        total = 0
        for b in yeahsan:
            total += min(limit, b)

        if total <= budget:
            bottom = limit + 1
        else:
            top = limit - 1

print(top)
