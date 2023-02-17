'''
정렬 문제 / 우선순위 설정에 따라 정렬
'''

import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])

stack = []
arr.sort(key = lambda x: (x[1], x[0])) # 1st 끝나는 시간 2nd 시작시간 기준으로 정렬
for i in range(len(arr)):
    if stack: #스택에 값이 있으면 스택에 들어있는 끝나는 시간과 현재의 시작시간을 비교해 추가
        if stack[-1][1] <= arr[i][0]:
            stack.append(arr[i])
    else: # 스택이 비어있으면 회의를 추가
        stack.append(arr[i])

print(len(stack))
