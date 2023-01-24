# '(' 없이 ')'가 나왔을 때 끝내는 것 필요

N = int(input())

for i in range(N):
    gwal_ho = input()
    list_gwal_ho = list(gwal_ho)
    checking = 0

    # 괄호 종류에 따라 checking에 1을 더하고 빼며 판단
    for check in list_gwal_ho:
        if check == '(':
            checking += 1
        elif check == ')':
            checking -= 1

        # checking < 0 은 '(' 없이 ')' 먼저 나왔을 때의 조건
        if checking < 0:
            break

    if checking == 0:
        print('YES')
    else:
        print('NO')

'''
.pop() 이용한 다른 코드

for i in range(N):
    gwal_ho = input()

    # 체크용으로 사용할 빈 리스트
    checking = []

    # 리스트 안에 ()가 완성되면 리스트 제거 [.pop()] 후 반복
    # '(' 없는데 ')' 입력되면 반복 중지 후 'NO' 출력
    for j in gwal_ho:
        if j == '(':
            checking.append('(')
        elif j == ")":
            if len(checking) != 0:
                checking.pop()
            else:
                checking.append(')')
                break

    # 괄호 개수가 딱 맞으면 체크용 리스트 길이는 0
    if len(checking) == 0:
        print('YES')
     else:
        print('NO')
'''