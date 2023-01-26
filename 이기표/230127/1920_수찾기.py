import sys
input = sys.stdin.readline

N = int(input())
N_li = list(map(int, input().split()))
M = int(input())
M_li = list(map(int, input().split()))

N_li = set(N_li) # 시간복잡도가 낮은 set 사용

for i in range(M):
    if M_li[i] in N_li: # 값이 존재하면 1 출력
        print(1)
    else:               # 값이 없으면 0 출력
        print(0)

# N = int(input())
# N_li = sorted(map(int, input().split()))
# M = int(input())
# M_li = list(map(int, input().split()))

# for num in M_li: # 시간복잡도 logN -> 이분탐색
#     ans = 0
#     start, end = 0, len(N_li) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#         if N_li[mid] < num:
#             start = mid + 1
#         elif N_li[mid] > num:
#             end = mid - 1
#         else:
#             ans = 1
#             break
#     print(ans)
