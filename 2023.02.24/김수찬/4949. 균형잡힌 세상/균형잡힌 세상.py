
import sys
texts = sys.stdin.readlines()


gal = '()[]' # 괄호 찾기
for i in range(len(texts) - 1):
    stack = []  #stack 에괄호를 넣을 준비를 함.
    text = list(texts[i].rstrip())
    result = None
    target = False
    for item in text:
        if item == '.': # End 일 경우 true
            target = True

        if item not in gal : continue  #괄호가 아닐경우 아래의 연산을 할 필요가 없음

        if (len(stack) == 0) and (item == ']' or item ==')'):
            result = 'no'
            break # 빈 stack일 때는 닫는 괄호가 올 수 없다.

        if item == '[' or item == '(': # 여는괄호를 stack
            stack.append(item)
        elif item ==']' or item ==')': # 닫는 괄호와 여는 괄호 쌍이 맞는지 비교
            if stack[-1] == '[' and item == ']' : 
                stack.pop()
            elif stack[-1] == '(' and item == ')' :
                stack.pop()
            else : # 쌍이 맞지 않는 경우
                result = 'no'
                break
    # 연산이 끝났을 때, STACK에 괄호가 있으면 쌍이 맞지 않는 것임
    if target == True and len(stack) == 0:
        result = 'yes'
    else :
        result = 'no'

    print(result)
