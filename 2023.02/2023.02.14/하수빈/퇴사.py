import sys
input = sys.stdin.readline

# 보수 확인 함수
def check(schedule, start, N):
    max_ssum = 0
    # 시작점 부터 끝까지
    for i in range(start, N):
        ssum = 0
        # 현재일에서 상담을 실행해도 N을 넘지 않는다면
        if N >= i + schedule[i][0]:
            # ssum은 현재일 상담보수 + 상담이 끝난날에서 다시 확인
            ssum = schedule[i][1] + check(schedule, i + schedule[i][0], N)

        if max_ssum < ssum:
            max_ssum = ssum

    return max_ssum


N = int(input())
schedule = []
for i in range(N):
    schedule.append(list(map(int, input().split())))

print(check(schedule, 0, N))
