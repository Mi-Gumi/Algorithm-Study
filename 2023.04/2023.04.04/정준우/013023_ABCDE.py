from sys import stdin


def find_relationship(current_member, friend_count):

    global satisfied

    # 조건을 만족하는 경우를 찾으면 남은 과정 다 중단
    if satisfied:
        return

    # 친구로 이어진 수가 4개가 되면 조건이 만족되었음을 표시하고 중단
    if friend_count == 4:
        satisfied = True
        return

    # 백트래킹
    visited[current_member] = 'visited'

    for linked in relationships[current_member]:
        if visited[linked] == 'not visited':
            find_relationship(linked, friend_count + 1)

    visited[current_member] = 'not visited'


num_of_members, num_of_relationships = map(int, stdin.readline().split())

relationships = {i: [] for i in range(num_of_members)}

for _ in range(num_of_relationships):
    fri, end = map(int, stdin.readline().split())
    relationships[fri].append(end)
    relationships[end].append(fri)

visited = ['not visited'] * num_of_members

satisfied = False

# 모든 멤버를 한 번씩 시작점으로 두며 탐색하다가 조건을 만족하는 경우가 있다면 반복 중단
for start_member in range(num_of_members):
    find_relationship(start_member, 0)

    if satisfied:
        break

if satisfied:
    print(1)

else:
    print(0)
