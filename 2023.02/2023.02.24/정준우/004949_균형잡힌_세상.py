# 몇 개의 문장이 입력될 지 몰라서 for 반복문은 사용하기 힘들다
# . 하나만 있는 문장이 입력될 시 종료되므로, 해당 조건으로 무한 반복 종료
while True:
    word = input()

    if word == '.':
        break

    check = []

    for i in word:
        if i == '(' or i == '[':
            check.append(i)

        elif i == ')':
            if check and check[-1] == '(':
                check.pop()
            else:
                check.append(i)
                break

        elif i == ']':
            if check and check[-1] == '[':
                check.pop()
            else:
                check.append(i)
                break

    if not check:
        print('yes')
    else:
        print('no')