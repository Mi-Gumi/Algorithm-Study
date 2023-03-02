import sys
input = sys.stdin.readline

T = int(input())

def sum_123(n): # 점화식 -> 재귀로 구현
    if n == 1: # 1일때의 합
        return 1
    elif n == 2: # 2일때의 합
        return 2
    elif n == 3: # 3일때의 합
        return 4
    else: # 재귀 진행
        return sum_123(n-1) + sum_123(n-2) + sum_123(n-3)

for _ in range(T):
    n = int(input())
    print(sum_123(n))
