num_of_pillar = int(input())

pillar_heights = [0 for _ in range(1001)]

# 기둥의 위치를 인덱스, 높이를 값으로 추가
for _ in range(num_of_pillar):
    pillar_x, pillar_y = map(int, input().split())

    pillar_heights[pillar_x] = pillar_y

# 뒤에서부터 탐색하며 높이가 0이 아닌 지점을 찾아 마지막 기둥의 위치르 지정
for i in range(len(pillar_heights) - 1, -1, -1):
    if pillar_heights[i] != 0:
        last_pillar_idx = i
        break

# 기둥 높이 배열을 오름차순으로 정렬 후 제일 뒤의 값을 기둥의 최고 높이로 지정
the_highest = sorted(pillar_heights)[-1]

# 최고 높이의 기둥이 위치하는 지점 찾기
for i in range(len(pillar_heights) - 1):
    if pillar_heights[i] == the_highest:
        the_highest_idx = i

area = 0

# 왼쪽 끝부터 제일 높은 기둥이 있는 곳까지 탐색하며 높이를 더해주다가, 더 높은 기둥이 나오면 그때부터는 해당 높이만큼 더해주기
current_height = 0
for i in range(1, the_highest_idx + 1):
    current_height = max(pillar_heights[i], current_height)
    area += current_height

# 오른쪽 끝에서부터 위 과정 반복, 이미 위 과정에서 최고 높이의 기둥은 넓이에 들어갔으니 범위에서 제외
current_height = 0
for i in range(last_pillar_idx, the_highest_idx, -1):
    current_height = max(pillar_heights[i], current_height)
    area += current_height

print(area)
