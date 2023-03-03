import sys
input = sys.stdin.readline

while True:
    s = input()
    # .이 입력된다면 break
    if s == '.':
        break

    stack = []
    # (나 [보다 )나 ]가 먼저나오거나 ([)]처럼 섞여서 나온다면 no
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        # (나 [가 )나 ]보다 많다면 no
        if stack:
            print('no')
        # 나머지는 yes
        else:
            print('yes')
