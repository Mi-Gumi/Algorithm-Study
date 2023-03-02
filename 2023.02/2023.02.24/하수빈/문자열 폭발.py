import sys
input = sys.stdin.readline

s = input()[:-1]
bbam = list(input()[:-1])
stack = []

for c in s:
    # s의 한문자씩 stack에 push
    stack.append(c)
    # push한 글자가 폭탄 문자열의 마지막 글자와 같다면
    if c == bbam[-1]:
        # 문자열 패턴 비교 후 같다면 pop
        if stack[-len(bbam):] == bbam:
            for _ in range(len(bbam)):
                stack.pop()

if stack:
    print(*stack, sep='')
else:
    print('FRULA')