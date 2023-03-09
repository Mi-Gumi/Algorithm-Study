'''
뱀은 0,0 에서 오른쪽 이동 and 뱀의 길이는 1
L 왼쪽으로 90도 전환, D 오른쪽으로 90도 전환
for while
패딩
'''
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
K = int(input())
arr = [[-1] + [0] * N + [-1] for _ in range(N)] # 벽을 -1로 패딩
arr = [[-1] * (N+2)] + arr + [[-1] * (N+2)]
for _ in range(K):
    i, j = map(int, input().split())
    arr[i][j] = 1 # 사과 위치
L = int(input())
command = []
for _ in range(L):
    num, com = input().split()
    num = int(num)
    command.append([num, com])

di = 0
dj = 1
si = sj = 1
arr[si][sj] = -1 # 꼬리 -1로 표현
tail = deque([(si, sj)]) # 꼬리 체크
ans = 0
tmp = 0
flag = 0
for i in range(len(command)):
    cnt = 0
    flag = 0
    while cnt != command[i][0] - tmp:
        ans += 1 # 이동 횟수만큼 정답 카운트
        cnt += 1 # 반복문 종료 체크 카운트
        si += di # 이동
        sj += dj
        tail.append((si, sj))  # 꼬리 추가
        if arr[si][sj] == 1: # 사과 있을때
            arr[si][sj] = -1 # 뱀의 머리 위치
        elif arr[si][sj] == 0: # 사과 없을때
            ci, cj = tail.popleft() # 꼬리 반환
            arr[ci][cj] = 0 # 꼬리위치를 다시 0
            arr[si][sj] = -1 # 뱀의 머리 위치
        elif arr[si][sj] == -1: # 꼬리나 벽에 부딪히면 종료
            flag = 1
            break
    if flag: # 종료
        break
    else: # 커맨드에 따라 위치 변경
        if command[i][1] == 'L':
            di, dj = -dj, di
        else:
            di, dj = dj, -di
    tmp = command[i][0] # 동작 시간 관리

if flag == 0: # 커맨드는 끝났지만 아직 벽이나 꼬리를 만나지 못한 경우
    while 1:
        ans += 1  # 이동 횟수만큼 정답 카운트
        si += di
        sj += dj
        tail.append((si, sj))
        if arr[si][sj] == 1:
            arr[si][sj] = -1
        elif arr[si][sj] == 0:
            ci, cj = tail.popleft()
            arr[ci][cj] = 0
            arr[si][sj] = -1
        elif arr[si][sj] == -1:
            flag = 1
            break

print(ans)

