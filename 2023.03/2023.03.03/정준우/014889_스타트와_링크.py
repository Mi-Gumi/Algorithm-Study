from itertools import combinations


def make_balanced_team():

    team_cha_ee = 1e9

    # 참석자의 반만큼 스타트 팀에서 구성할 수 있는 팀원 조합
    for start_team in list(combinations(entire, num_of_participants // 2)):
        start_team_stat = link_team_stat = 0

        # 링크 팀은 스타트 팀에서 팀을 구성하고 남은 인원으로 구성
        link_team = list(set(entire) - set(start_team))

        # 구성된 각 팀에서 두 명씩 짝지었을 때의 능력치 더해주기
        for syn, ergy in list(combinations(start_team, 2)):
            start_team_stat += entire_stat[syn][ergy]
            start_team_stat += entire_stat[ergy][syn]

        for syn, ergy in list(combinations(link_team, 2)):
            link_team_stat += entire_stat[syn][ergy]
            link_team_stat += entire_stat[ergy][syn]

        # 지금까지 나온 팀 전력 차이의 최소값 갱신
        team_cha_ee = min(team_cha_ee, abs(start_team_stat - link_team_stat))

    return team_cha_ee


num_of_participants = int(input())

# 참여자 수만큼 번호로 구성원 구분
entire = list(range(num_of_participants))
entire_stat = [list(map(int, input().split())) for _ in range(num_of_participants)]

print(make_balanced_team())
