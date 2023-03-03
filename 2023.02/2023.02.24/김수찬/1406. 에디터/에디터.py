import sys

stack_l = list(input()) # 문자를 여기까지썻음
stack_r = [] # 이후에 적용할 괄호

## 문자 사이 간격의 커서를 괄호 두개로 표현을 하겠다.
# [Hellowor][ld]
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L" and stack_l:
        stack_r.append(stack_l.pop())
    elif command[0] == "D" and stack_r:
        stack_l.append(stack_r.pop())
    elif command[0] == "B" and stack_l:
        stack_l.pop()
    elif command[0] == "P":
        stack_l.append(command[1])

print("".join(stack_l + list(reversed(stack_r))))