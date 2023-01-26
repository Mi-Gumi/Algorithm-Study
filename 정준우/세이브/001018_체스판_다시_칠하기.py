N, M = map(int, input().split())

# 원래 체스판을 담을 리스트와 색칠 횟수를 담을 리스트 생성
original_plate = []
work = []

for _ in range(N):
    original_plate.append(input())
# 시작점에 8칸을 더했을 때, 원래 체스판의 크기를 넘어가지 않도록 반복 범위 조절
for n in range(N-7):
    for m in range(M-7):
        # 시작점이 검은색일 때, 흰색일 때 각 색칠 횟수 모두 고려하기 위해 두 개의 변수 초기화
        work_when_start_is_black = 0
        work_when_start_is_white = 0
        # 시작점에서 +8 된 부분까지 반복
        for o in range(n, n+8):
            for p in range(m, m+8):
                # 좌표의 합이 짝수인 부분은 시작점과 색이 같아야 한다
                # 조건에 부합하는 색이 아닐 경우, 색칠 횟수 1씩 증가
                if (o + p) % 2 == 0:
                    if original_plate[o][p] != 'B':
                        work_when_start_is_black += 1
                    elif original_plate[o][p] != 'W':
                        work_when_start_is_white += 1
                else:
                    if original_plate[o][p] != 'W':
                        work_when_start_is_black += 1
                    elif original_plate[o][p] != 'B':
                        work_when_start_is_white += 1
        # 두 경우 중 횟수가 작은 것으로 리스트에 추가
        work.append(min(work_when_start_is_black, work_when_start_is_white))
# 리스트에 추가된 것들 중에서도 제일 작은 숫자 출력        
print(min(work))