import sys
input = sys.stdin.readline

N = int(input())

# 회의의 시작시간과 끝시간 배열 생성
meeting = []
for _ in range(N):
    meeting.append(list(map(int, input().split())))

# 회의를 시작시간순으로 정렬한 후 다시 끝시간 순으로 정렬
meeting.sort()
meeting.sort(key=lambda x:x[1])

#회의 갯수와 현재시간 선언
count = 0
now = 0
# 회의를 끝시간 순으로 정렬해 놨음으로 제일 앞회의의 끝시간이 가장 빠르다.
for i in range(N):
    # 회의의 시작시간이 현재 시간보다 크거나 같다면
    # 현재시간을 회의의 끝시간으로 변경
    if meeting[i][0] >= now:
        now = meeting[i][1]
        # 회의 갯수 증가
        count += 1

print(count)