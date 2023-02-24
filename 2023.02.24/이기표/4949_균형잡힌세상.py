def check(lst):
    stack = []
    for t in lst:
        if t =='(' or t == '[':
            stack.append(t)
        elif t == ')' or t == ']':
            if stack:
                if stack[-1] == '(' and t == ')':
                    stack.pop()
                elif stack[-1] == '[' and t == ']':
                    stack.pop()
                else:
                    stack.append(t)
            else:
                stack.append(t)
    if stack:
        return 'no'
    else:
        return 'yes'

data = 0
text_li = []
while 1:
    data = input()
    if data == '.':
        break
    text_li.append(data)

for lst in text_li:
    print(check(lst))