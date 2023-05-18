from itertools import permutations
import sys
input = sys.stdin.readline
N = int(input()) # 도시 수
W = [list(map(int, input().split())) for _ in range(N)]
'''
1-2-3-4-1
1-2-4-3-1
1-3-4-2-1
1-3-2-4-1
1-4-2-3-1
1-4-3-2-1
2-1-3-4-2
...

'''
# 일단 ! permutaions으로 [1~N] 경우의 수 다 구하기
# 각 비용들 중에 최소 비용 구하기
# 주의 ! 길이 없는 경우에는 못 감

arr = [i for i in range(N)]
mn = 1e9

for p in permutations(arr, N):
    flag = True
    hap = 0
    if W[p[-1]][p[0]] == 0: # 복귀하는 길이 없으면 다른 경우의 수로 넘어가
        continue
    
    for n in range(N-1):
        if W[p[n]][p[n+1]] == 0: # 가는 길이 없으면 for문 멈추고
            flag = False
            break
        else: # 가는 길 있으면 합하기
            hap += W[p[n]][p[n+1]]
            
    if flag == False: # 가는 길 없으면 다른 경우의 수로 넘어가
        continue
    
    hap += W[p[-1]][p[0]] # 복귀하는 길도 합하기 

    if mn > hap:
        mn = hap

print(mn)
