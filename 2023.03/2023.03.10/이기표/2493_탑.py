import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
check = []
result = [0] * N # 탑의 수신 인덱스를 저장하는 정답 리스트

for i in range(N):
    while check:
        if lst[check[-1][0]] < lst[i]: # 조건에 맞는 탑이 없는 경우
            check.pop() # 탑의 위치를 삭제
        else:
            result[i] = check[-1][0] + 1 # 조건에 맞는 탑을 찾은 경우
            break # 종료
    check.append([i, lst[i]]) # 현재의 인덱스와 탑의 높이를 저장
print(*result)




