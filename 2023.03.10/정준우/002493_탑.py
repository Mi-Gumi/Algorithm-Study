import sys

num_of_tower = int(sys.stdin.readline())

height = list(map(int, sys.stdin.readline().split()))

answer = [0] * num_of_tower

# 제일 왼쪽 탑은 볼 필요가 없으므로 1부터 시작
for i in range(1, num_of_tower):
    tower_check = i - 1

    # -1까지 내려가게 되면 왼쪽에 해당 탑보다 높은 것이 없다는 의미로, 결과로 0을 얻게 된다
    # 왼쪽에 높이가 더 높은 탑이 있다면, 정답 리스트의 해당 인덱스에 몇 번째 탑에서 수신하는지 기록
    while tower_check != -1:
        if height[tower_check] >= height[i]:
            answer[i] = tower_check + 1
            break

        # 아직 인덱스가 -1이 아니라면, 더 왼쪽에 있는 탑과 높이 비교
        # 시간 절약을 위해 이미 구한 답을 활용
        
        # 만약 탑의 높이가 [6 1 2 3 4 5 7]일 때 높이 7의 탑을 보는 경우라면, 
        # 현재 answer는   [0 1 1 1 1 1 0]일 것이고
        # else 조건문에 들어가면 이미 오른쪽보다 높이가 낮다고 판단된 중간 탑들과의 높이 비교를 생략하고 
        # 바로 높이 6인, height 리스트에서 인덱스가 0인 첫 번째 탑과 높이 비교
        else:
            tower_check = answer[tower_check] - 1

print(*answer)
