import sys
from collections import deque

# 전체 인원과 몇 번째마다 제거되는지 변수로 지정
num_of_potatos, gamzajeon = map(int, sys.stdin.readline().split())

# 인원수만큼의 크기를 가지며, 숫자가 차례대로 들어간 round_table 큐 생성
# 1부터 시작되어야 하니 range 범위 조정
round_table = deque(potato for potato in range(1, num_of_potatos + 1))

# 제거된 인원의 숫자를 차례대로 넣을 빈 리스트 생성
answer_list = []

# 모든 인원이 제거되어 round_table 큐의 길이가 0이 될때까지 반복
while len(round_table) != 0:
    # 만약 세번째 인원을 제거한다면, 2번 왼쪽으로 회전시켰을 때 해당 인원이 큐의 제일 왼쪽에 위치한다
    round_table.rotate(-(gamzajeon - 1))
    # round_table 큐에서 제일 왼쪽 요소를 빼 answer_list에 추가
    answer_list.append(round_table.popleft())

# 완성된 리스트에서 [ ]를 빼고 요소 사이에 ,  를 넣기 위해 join 메서드 사용
print(f'<{", ".join(map(str, answer_list))}>')