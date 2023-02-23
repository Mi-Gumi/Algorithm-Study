import sys
input = sys.stdin.readline

# 커서를 기준으로 앞부분을 stack1 뒷부분을 stack2에 저장
stack1 = list(input().strip())
stack2 = []

N = int(input())
for _ in range(N):
    cmd = list(input().split())
    # L 이라면 stack1의 맨 뒷자리를 stack2에 push
    if cmd[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    # D 라면 stack2의 맨 뒷자리를 stack1에 push
    elif cmd[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    # L 이라면 stack1의 맨 뒷자리를 pop
    elif cmd[0] == 'B':
        if stack1:
            stack1.pop()
    # L 이라면 stack1의 맨 뒷자리에 들어온 문자를 push
    elif cmd[0] == 'P':
        stack1.append(cmd[1])

stack2.reverse()
print(*stack1, sep='', end='')
print(*stack2, sep='')