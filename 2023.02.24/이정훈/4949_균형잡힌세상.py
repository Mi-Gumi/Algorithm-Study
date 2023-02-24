while True:
    s = input()
    if s == '.': # 종료 조건
        break
    stack = []
    ans = 'yes'         # 정상을 default 로 초기화
    for c in s:
        if c == '(' or c == '[':    # 여는 괄호
            stack.append(c)
        elif c == ')' or c == ']':
            if not stack:   # 닫는 괄호는 있는데 연 괄호가 없음
                ans = 'no'
                break
            elif c == ')' and stack[-1] != '(' or c == ']' and stack[-1] != '[':
                ans = 'no'    # 다른 괄호가 열음
                break
            stack.pop()    # 이상이 없으면 pop
    if stack:   # 닫는 괄호가 없는데 여는 괄호가 남음
        ans = 'no'

    print(ans)