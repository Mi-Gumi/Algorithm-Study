import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline())

# '('의 갯수와 ')'의 갯수를 저장할 변수
count_l = 0
count_r = 0
# '('가 나온다면 count_l + 1 ')'가 나온다면 count_r + 1
for i in range(len(arr)):
    for c in arr[i]:
        if c == '(':
            count_l += 1
        elif c == ')':
            count_r += 1
        # ')'가 '(' 보다 먼저 나오는 경우가 있다면 for문 중지
        if count_r > count_l:
            break
    # count_l과 count_r이 같다면 YES출력 아니면 NO출력
    if count_l == count_r:
        print('YES')
    else:
        print('NO')
    # count_l, count_r 초기화
    count_l = 0
    count_r = 0