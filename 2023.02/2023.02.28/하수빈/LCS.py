import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
max_len = 0
lcs = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        # 문자열의 글자가 같다면 문자열 길이 + 1
        if s1[i - 1] == s2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        # 두 문자열의 글자가 같지 않다면 전 최장 부분 문자열의 길이로 설정
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

# 마지막 가중치 출력
print(lcs[-1][-1])