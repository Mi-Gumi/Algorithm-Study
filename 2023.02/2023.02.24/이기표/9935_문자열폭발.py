import sys
input = sys.stdin.readline

text = input().rstrip()
pattern = input().rstrip()
stack = []
for t in text:
    stack.append(t) # 스택에 push
    if len(stack) >= len(pattern): # 스택에 길이가 패턴 길이 이상이면 시작
        if ''.join(stack[-len(pattern):]) == pattern: # 글자수 일치
            for i in range(len(pattern)): # 패턴과 일치하면 패턴 길이만큼 pop
                stack.pop()
if stack: # 스택에 값이 남아있으면
    print(''.join(stack))
else: # 스택이 다 비워졌으면
    print('FRULA')