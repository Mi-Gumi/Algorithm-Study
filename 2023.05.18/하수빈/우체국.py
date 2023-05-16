import sys
input = sys.stdin.readline


N = int(input())
v = []
v_sum = 0
p_sum = 0

for _ in range(N):
    v.append(list(map(int, input().split())))
    # 전체 사람 수 계산
    v_sum += v[-1][1]

# 마을 순서 별로 정렬
v.sort()

for i in range(N):
    # 누적 사람 수 계산
    p_sum += v[i][1]
    # 사람 수가 전체 사람 수의 절반을 넘으면 우체국 설치 후 종료
    if p_sum >= (v_sum + 1) // 2:
        print(v[i][0])
        break