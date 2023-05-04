import sys
input = sys.stdin.readline

def subset():
    global ans
    f = []

    for i in range(1 << N):
        s_p = s_f = s_s = s_v = tmp = 0
        r = []
        for j in range(N):
            # 비트 부분집합
            if i & (1 << j):
                s_p += foods[j][0]
                s_f += foods[j][1]
                s_s += foods[j][2]
                s_v += foods[j][3]
                tmp += foods[j][4]
                r.append(j + 1)
                if tmp > ans:
                    break
        else:
            if s_p >= mp and s_f >= mf and s_s >= ms and s_v >= mv:
                # ans가 tmp보다 크다면 ans와 f교체
                if ans > tmp:
                    ans = tmp
                    f = r[:]
                # ans가 tmp와 같다면
                elif ans == tmp:
                    # 사전 순 정렬
                    f = sorted([f, r[:]])[0]
    
    return f


N = int(input())
mp, mf, ms, mv = map(int, input().split())
foods = [list(map(int, input().split())) for _ in range(N)]
ans = 10 ** 9
result = subset()
# ans가 변했다면 ans와 result 출력
if ans != 10 ** 9:
    print(ans)
    print(*result)
else:
    print(-1)