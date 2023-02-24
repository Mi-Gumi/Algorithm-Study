import sys
from collections import deque

# 커서를 기준으로 왼쪽, 오른쪽 문자열을 담을 스택 두 개 생성
# 처음에는 커서가 맨 뒤에 있으므로, 주어진 문자열을 모두 커서 왼쪽을 의미하는 스택에 추가
# 테스트 케이스에 \n 있으니 strip으로 제거
cursor_left = deque(list(sys.stdin.readline().strip()))
cursor_right = deque()

num_of_command = int(sys.stdin.readline())

for _ in range(num_of_command):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        if not cursor_left:
            continue
        else:
            cursor_right.appendleft(cursor_left.pop())

    elif command[0] == 'D':
        if not cursor_right:
            continue
        else:
            cursor_left.append(cursor_right.popleft())

    elif command[0] == 'B':
        if not cursor_left:
            continue
        else:
            cursor_left.pop()

    elif command[0] == 'P':
        cursor_left.append(command[1])

cursor_left.extend(cursor_right)

print(''.join(cursor_left))