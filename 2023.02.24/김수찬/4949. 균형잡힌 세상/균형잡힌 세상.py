
import sys
texts = sys.stdin.readlines()


gal = '()[]'
for i in range(len(texts) - 1):
    stack = []
    text = list(texts[i].rstrip())
    result = None
    target = False
    for item in text:
        if item == '.':
            target = True

        if item not in gal : continue

        if (len(stack) == 0) and (item == ']' or item ==')'):
            result = 'no'
            break

        if item == '[' or item == '(':
            stack.append(item)
        elif item ==']' or item ==')':
            if stack[-1] == '[' and item == ']' :
                stack.pop()
            elif stack[-1] == '(' and item == ')' :
                stack.pop()
            else :
                result = 'no'
                break
    if target == True and len(stack) == 0:
        result = 'yes'
    else :
        result = 'no'

    print(result)
