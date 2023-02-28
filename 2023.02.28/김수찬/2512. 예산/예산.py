N = int(input())
pay = list(map(int,input().split()))
total = int(input())

if sum(pay) <= total: ## 예산이 초과되지 않는다면, 예산 중 최대값을 출력
    print(max(pay))
else:
    ## 필요한 것은 예산 분배금 중 최댓값.. 
    # 어떤 예산이 얼마 인지는 바뀐다. => ex) 150 못줘 127만 받아가
    # 따라서 탐색을 통해 최대한으로 분배할 수 있는 분배금을 찾아보자.
    start = 0
    end = max(pay)
    while start <= end:        # min 값이 max값 보다 더 커질 경우 끝
        mid = (start + end)//2 # mid 값은 중앙값으로 설정 (이분탐색) 
        curr = 0               # 예산 분배금 의 총 합
        for tax in pay:        # 각 지역마다 필요한 예산들이랑 현재 줄 값이랑 비교
            if tax >= mid:     # 예산이 분배금(mid) 보다 클 경우 분배금을 나눠줌
                curr += mid
            else:              # 예산이 분배금보다 작을 경우 예산을 주면 됨
                curr += tax
        
        if curr <= total:      # curr -> 현재 분배금이 total 분배금보다 작을 경우
            start = mid + 1    # 분배금 총량을 늘려본다
        else:                  # curr -> 현재 분배금이 total분배금 보다 클 경우
            end = mid - 1      # 분배금 총량을 낮춰본다
    print(end)
