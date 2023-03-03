import sys

input = sys.stdin.readline
# 입력량이 많으므로

string = list(input().strip())  # strip으로 '\n' 제거

N = int(input())
# 오른쪽 문자열을 담아둘 리스트
tmp = []

for i in range(N):
    commend, *c = input().split()

    if commend == 'L':  # 끝 문자를 tmp에 넣어 커서가 왼쪽으로 움직인 것으로 봄
        if string:      # 왼쪽 끝이면 pass
            tmp.append(string.pop())
    elif commend == 'D': # tmp에서 다시 넣어 커서가 오른쪽으로 움직인 것으로 봄
        if tmp:          # 오른쪽 끝이면 pass
            string.append(tmp.pop())
    elif commend == 'B': # 하나 삭제
        if string:
            string.pop()
    else:
        string.extend(c) # 커서 왼쪽에 추가

while tmp:              # 남아있는 문자 다시 붙임
    string.append(tmp.pop())

print(''.join(string))
