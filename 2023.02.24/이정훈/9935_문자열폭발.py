
s = list(input())
c4 = list(input())
stack = []       # 새로 만들 문자열을 담을 stack
length = 0       # len 함수의 사용을 최소화  , stack 의 길이를 의미
c4len = len(c4)  # 폭발하는 문자열
for c in s :
    stack.append(c)
    length += 1

    if length >= c4len and stack[-c4len:] == c4: # 길이가 유망하며 마지막 부분이 c4와 같으면
        for i in range(c4len) :     # pop
            stack.pop()
            length -= 1
if length :             # 끝났는데 남아있으면
    print(''.join(stack))
else :
    print('FRULA')      # 아무것도 없으면

# replace 를 사용해서 풀어본 코드 ==> 시간초과

# cnt = True
# while cnt:
#     s = s.replace(c4, '')
#     cnt = c4 in s
#
# if s:
#     print(s)
# else:
#     print('FRULA')
