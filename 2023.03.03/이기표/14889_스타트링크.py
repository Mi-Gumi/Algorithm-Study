from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

combi = list(combinations(list(range(N)), N // 2)) # N까지의 조합 찾기
ans = 99999999999 # 최소값 비교
for i in range(len(combi)): # 무조건 짝수이기때문에 시작, 끝을 기준으로 팀 구성
    start = list(combinations(combi[i], 2)) # 찾은 조합을 토대로 팀 구성
    link = list(combinations(combi[len(combi) - 1 - i], 2))

    start_cnt = link_cnt = 0
    for s in start: # 스타트팀에 대한 계산
        start_cnt += arr[s[0]][s[1]] + arr[s[1]][s[0]]
    for l in link: # 링크팀에 대한 계산
        link_cnt += arr[l[0]][l[1]] + arr[l[1]][l[0]]

    ans = min(ans, abs(start_cnt - link_cnt)) # 차이의 최소값 도출
print(ans)