N = int(input())
pay = list(map(int,input().split()))
total = int(input())

if sum(pay) <= total: ## 예산이 pay에 가격에 들어 맞다면,
    print(max(pay)) ## 예산의 최댓값 출력
else:
    avg = total//N
## 알고리즘 분류 = 이분탐색 --> 이분탐색으로 문제풀기
    pay.sort()
    start = 0
    end = max(pay)
    while start <= end:
        mid = (start + end)//2 # 예산 분배금의 중간값 파악
        curr = 0 # 예산 분배금 
        
        ## 예산 분배금을 분배를 한 다음 다시 체크 -> 분배를 한다음 다시채크 --> ...
        for tax in pay:
            if tax >= mid:  # 만약에 우리가 원하는 분배금이 mid 보다 클 경우
                curr += mid # 예산 분배금을 mid 값으로 설정
            else:
                curr += tax # 그렇지 않을 경우 원하는 예산값으로 제공
                
        # 트라이 때 발생하는 예산 분배금
        if curr <= total:   # total 보다 작을 경우
            start = mid + 1 # 최저 예상 분배금을 조금더 높게 설정해 다시 탐색
        else:               # total 보다 클 경우 
            end = mid - 1   # 최고 분배금을 예상보다 조금 더 낮게 설정하여 다시 탐색
    print(end)
