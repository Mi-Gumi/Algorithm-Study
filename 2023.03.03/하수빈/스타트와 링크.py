import sys
input = sys.stdin.readline


def check(n, k, m):
    global min_sub
    # 팀을 다 나눴다면
    if n == k:
        start = 0
        link = 0
        sub_sum = 0
        for i in range(n * 2):
            # 만약 i번 팀원이 start팀 안에 있다면
            if i in subset:
                # start팀 안에 있는 다른 팀원들과의 능력치 +
                for j in subset:
                    start += arr[i][j]
            # i번 팀원이 start팀 안에 없다면 link팀
            else:
                for j in range(n * 2):
                    # i, j번 팀원이 모두 start팀 안에 없다면
                    if j not in subset:
                        # i, j팀원의 능력치 link에 +
                        link += arr[i][j]
        # 능력치 차이 계싼
        sub_sum = abs(start - link)
        # 최소 능력치 차이 교환
        min_sub = min(min_sub, sub_sum)
    # 팀을 덜 나눴다면
    else:
        # 팀원 추가 후 다시 확인
        for i in range(m, n * 2):
            subset.append(i)
            check(n, k + 1, i + 1)
            subset.pop()  


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_sub = 1000000000
# start팀 선언
subset = [0]

check(N // 2, 1, 1)

print(min_sub)
