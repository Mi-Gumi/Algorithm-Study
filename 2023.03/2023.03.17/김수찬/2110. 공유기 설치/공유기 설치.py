N,C = map(int,input().split())

'''
공유기 설치를 할 때 가장 짧은 길이 중 가장 큰 길이를 찾아야하는 문제
가능한 최대 거리인 평균 거리에서 부터 시작하여, 모든 집을 방문하여 거리에 대한 정보를 받아온다 
'''
arr = [int(input()) for _ in range(N)]
arr.sort()

length = arr[N - 1] - arr[0]

if C == 2:
    print(length) # 만약 2개만 설치할 경우 길이이다.
else:
    ans = length

    start = 0                   # start는 0
    end = length //(C-1)        ## 가능한 최대 거리는 평균거리이다.
    while start <= end:         # 공유기 설치 가능한 길이를 이분탐색으로 찾을 예정

        mid = (start + end) // 2  ## 왜 사람들이 거리차이를 start하고 end로 뒀을까 (초기에는 건물들과의 거리 탐색을 위해 idx로 탐색했었음)
        curr = arr[0]             # 처음 시작하는 집에 대해서
        count = 1                 # 처음 시작했으니까 cnt를 1로 시작

        for i in range(N):
            if (arr[i] - curr) >= mid: # 가장 큰 거리라 생각했던 것 보다 더 큰 것이 있을경우 count 시작
                count += 1             # 카운팅 진행
                curr = arr[i]          # 현재 위치를 업데이트

        if count >= C:                 # 카운팅이 많으면 공유기를 많이 설치한 것
            start = mid + 1            # mid 값을 더 크게 줘도 상관이 없다.
            ans = mid
        else: # count < C             # 카운팅이 적으면 공유기를 적게 설치한 것
            end = mid - 1             # mid 값을 더 작게 줘야한다.
    print(ans)