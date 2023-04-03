from itertools import combinations

N = int(input())
people = list(range(N))
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
# 조합 : 인원수의 반을 길이로
combi_lst = list(combinations(people, N // 2))

_min = 9999
# 조합을 team1으로 사용
for team1 in combi_lst[:len(combi_lst) // 2]:   # 조합의 절반 이후는 team1의 여집합과 같음
    team2 = list(set(people) - set(team1))    # 상대팀 조합
    team1_synergy = 0
    team2_synergy = 0
    #
    for player in team1:
        for person in team1:
            team1_synergy += adj_matrix[player][person]  # 다른 팀원과의 시너지점수를 모두 더함
    for player in team2:         # 상대팀도 마찬가지로 더해줌
        for person in team2:
            team2_synergy += adj_matrix[player][person]
    # 둘의 차이값
    cal = abs(team1_synergy - team2_synergy)
    # min 값 계산
    if _min > cal:
        _min = cal
        # 더 이상 계산할 필요없음
        if _min == 0 :
            break
print(_min)
