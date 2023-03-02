word = input()
trigger = input()

stack = []

for i in word:
    stack.append(i)

    # 적어도 스택의 길이가 폭발 문자열의 길이만큼 되어야 판단 가능
    if len(stack) >= len(trigger):
        # 스택 내 요소를 폭발 문자열 길이만큼 뒤에서 봤을 때, 폭발 문자열과 같으면 그 길이만큼 제거
        if ''.join(stack[- len(trigger):]) == trigger:
            for _ in range(len(trigger)):
                stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))