import sys
input = sys.stdin.readline


N, M = map(int, input().split())
dna = [input().strip() for _ in range(N)]
new = ['A', 'C', 'G', 'T']
ans = 0
ans_dna = []

# 각 자리에 대해서
for i in range(M):
    cnt = 10 ** 9
    # 일치하는 갯수가 가장 많은 문자 선택
    for j in range(4):
        tmp = 0
        now = new[j]
        for k in range(N):
            if dna[k][i] != now:
                tmp += 1
        if cnt > tmp:
            cnt = tmp
            cnt_new = now
    ans += cnt
    ans_dna.append(cnt_new)

print(''.join(ans_dna))
print(ans)