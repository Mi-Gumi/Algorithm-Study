N = int(input())
tower = list(map(int,input().split()))
gett = [0 for _ in range(N)] # 신호 받는 타워의 신호 탐색

## 이전에 시간초과가 뜬 코드
# target = 0
# for i in range(1,N):
#     if tower[target] <= tower[i]: # 가장 높은 타워 업데이트
#         target = i
#     else:                         # 특정 타워가 다른타워보다 작다면 신호를 받을 수 있음
#         for j in range(i-1, target - 1, -1):
#             if tower[j] >= tower[i]:
#                 gett[i] = j+1
#                 break
# print(*gett)

stack = [] # 수신지 타워 정보 확인용
gett1 = [0 for _ in range(N)]
stack.append((tower[0],1)) # 타워를 담음 (타워의 높이,idx)
for i in range(1,N):
    if tower[i] < stack[-1][0]: # 담긴 타워보다 탐색하는 타워가 더 작다면
        gett1[i] = stack[-1][1] # i 번째 타워는 stack[-1]의 타워를 받을 것
    else:
        while stack: # 담긴 타워보다 탐색하는 타워가 더 크다면
                     # 탐색하는 타워보다 큰 타워가 나올때까지 pop
            if tower[i] < stack[-1][0]: 
                gett1[i] = stack[-1][1]
                break
            else:
                stack.pop()

    stack.append((tower[i],i+1))
print(*gett1)