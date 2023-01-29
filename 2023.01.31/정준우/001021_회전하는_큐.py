import sys
from collections import deque

queue_size, number_of_nums = map(int, sys.stdin.readline().split())

# 위에서 입력받은 원소의 수만큼 0 으로 이루어진 덱 생성
deck = deque(0 for _ in range(queue_size))

# 목표 원소가 위치한 인덱스를 리스트 형태로 받기
target_index = list(map(int, sys.stdin.readline().split()))

# 목표 원소를 다른 원소와 구분하기 위해, 해당 인덱스에 위치한 원소를 다른 것으로 변경
# 주어진 위치대로 원소를 순서대로 뽑아야 하기 때문에, 목표 원소끼리도 구분하려고 target{i} 로 지정
for i in target_index:
    deck[i-1] = f'target{i}'

# 2, 3번 연산이 이루어진 횟수를 셀 count 변수 지정
count = 0

# 목표 원소의 인덱스 중,
for i in target_index:
    # 목표 원소를 뽑아낼 때까지 반복하기 위한 while True
    while True:
        # 덱의 첫 원소가 목표 원소라면, 그것을 제거하고 반복 중단 후 for 반복문의 다음 순서 진행
        if deck[0] == f'target{i}':
            deck.popleft()
            break

        # 덱의 첫 원소가 목표 원소가 아니라면,
        else:
            # 목표 원소의 인덱스가 전체 길이의 반보다 작다면, 덱을 왼쪽으로 회전 (또는 왼쪽으로 한칸씩 밀어냄) 후 작업 횟수에 1 더하기
            if deck.index(f'target{i}') < (len(que) / 2):
                deck.rotate(-1)
                count += 1
            # 목표 원소의 인덱스가 전체 길이의 반보다 크다면, 덱을 오른쪽으로 회전
            else:
                deck.rotate(1)
                count += 1

# 목표 원소를 모두 뽑아내 반복문이 끝났다면, 쌓인 작업 횟수 출력
print(count)