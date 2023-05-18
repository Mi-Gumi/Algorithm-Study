'''
'누적 인구수가 절반을 넘어가는 지점'
이유는 가산이 들어가기 때문.
거리를 중심으로 구하지만 인구가 많으면 많을수록 거리값이 가산
그래서 인구가산이 가장 적은 지역을 구하면 된다라는 것이 이 문제의 의도
'''
import sys
input = sys.stdin.readline

N = int(input())

lst = []
people = 0
for _ in range(N):
    u, p = map(int, input().split())
    lst.append([u, p])
    people += p

lst.sort()
ans, rst = 0, 0
for i in range(N):
    ans += lst[i][1]
    # 거리를 누적하며 누적 인구수가 절반을 넘어가는 지점이 정답
    # -> 인덱스가 작은 경우가 정답인 케이스도 만족
    if ans >= people / 2:
        rst = lst[i][0]
        break

print(rst)