# import sys 후,
# input()을 sys.stdin.readline() 으로 대체
# input()보다 컴퓨터 언어에 더 가까워 시간 절약

import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

# 정렬된 리스트를 하나씩 출력
for j in nums:
    print(j)