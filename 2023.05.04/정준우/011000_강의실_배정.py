from sys import stdin
from heapq import *


num_of_lectures = int(stdin.readline())

lectures = []

for _ in range(num_of_lectures):
    lecture_start_time, lecture_end_time = map(int, stdin.readline().split())

    lectures.append((lecture_start_time, lecture_end_time))

used_lecture_room = []

# 가장 빨리 시작하는 강의부터 넣기 위해
lectures.sort()

# 강의가 끝나는 시간만 사용
heappush(used_lecture_room, lectures[0][1])

for start_time, end_time in lectures[1:]:

    # 새 강의의 시작 시간에 사용이 종료되는 강의실이 없다면 새 강의실 사용
    if start_time < used_lecture_room[0]:
        heappush(used_lecture_room, end_time)

    # 아니라면 사용 종료된 강의실을 사용하며 해당 강의실의 사용 종료 시간 갱신
    else:
        heappop(used_lecture_room)
        heappush(used_lecture_room, end_time)

print(len(used_lecture_room))
