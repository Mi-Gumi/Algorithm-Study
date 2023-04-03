
# 이전에 풀었던 창고다각형과 똑같은 문제여서 똑같은 방식으로 접근했습니다
# [문제 링크](https://www.acmicpc.net/problem/2304) 
H, W = map(int,input().split())

column = list(map(int,input().split()))

idx = 0
max_H = 0
# 높이가 최대인 값 기둥의 위치를 찾아둡니다.
for i, col in enumerate(column):
    # 이 때, 기둥의 높이가 같을 수 있고, 
    # 기둥의 높이가 같을 경우 물이 차지 않기 때문에 
    # 그 부분을 파악하기 위해 같은경우 idx을 업데이트를 하려고
    # 이하 부등호를 사용했습니다.
    if max_H <= col:
        idx = i
        max_H = col

Hole = 0 # 물이 차는 곳
target = column[0] # 첫 시작
for i in range(idx):

    # 물이 찰 수 있는 기둥의 최대 높이가 현재 기둥보다 작을 경우
    if target < column[i]:
        target = column[i] # 기둥 업데이트
    # Target 기둥이 더 클경우
    elif target > column[i]:
        Hole += (target - column[i]) # 물을 담음

# 역순으로 진행
target = column[-1]
for i in range(W-1,idx,-1):
    if target < column[i]:
        target = column[i]
    elif target > column[i]:
        Hole += (target - column[i])

    # if column[idx] == target: 
    # # target으로 하는 높이가 idx에 해당하는 기둥에 도달했을 경우 break
    # # 인덱스로 작업하지 않은 이유는
    #     break


print(Hole)