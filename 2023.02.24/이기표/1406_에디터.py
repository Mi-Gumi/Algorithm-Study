data = list(input())
N = int(input())
backup = [] # 커서 기준으로 분리
for i in range(N):
    com = input().split()
    if com[0] == 'L':
        if len(data) == 0: # 문자 처음
            continue
        backup.append(data.pop()) # 커서 기준으로 오른쪽
    elif com[0] == 'D':
        if len(backup) == 0: # 문자 끝
            continue
        data.append(backup.pop()) # 커서 기준으로 왼쪽
    elif com[0] == 'B':
        if len(data) == 0:
            continue
        data.pop() # 커서 왼쪽 리스트 pop
    else:
        data.append(com[1]) # 커서 왼쪽 리스트에 push
for j in range(len(backup)):
    data.append(backup.pop())
