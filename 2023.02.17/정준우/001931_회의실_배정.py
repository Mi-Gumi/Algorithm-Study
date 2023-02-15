# 문제 힌트 참고함 - 직접 해봤을 때,
# 시작 시간이 빠른걸 먼저 넣고, 시작 시간이 같으면 끝나는 시간이 가장 빠른 회의를 넣는 것이 가장 많은 회의를 할 수 있는 경우

num_of_meeting = int(input())

# 회의 시작 시간과 끝나는 시간을 담을 리스트
schedule = []

for _ in range(num_of_meeting):
    meeting_start, meeting_end = map(int, input().split())
    schedule += [[meeting_start, meeting_end]]

# 시작 시간으로 먼저 스케줄 오름차순 정렬 후, 끝나는 시간으로 다시 오름차순 정렬
schedule.sort(key = lambda x: x[0])
schedule.sort(key = lambda x: x[1])

# 한 회의가 끝난 현재 시간
current_time = 0
# 할 수 있는 회의의 수
possible_meeting = 0

# 현재 시간이 어떤 회의의 시작 시간보다 전이거나 같을 때, 그 회의의 끝나는 시간을 현재 시간으로 저장 후 회의 수 +1
for [start, end] in schedule:
    if current_time <= start:
        current_time = end
        possible_meeting += 1

print(possible_meeting)
