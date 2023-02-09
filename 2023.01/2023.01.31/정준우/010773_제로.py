import sys
input = sys.stdin.readline

N = int(input())

# 입력되는 수를 담아둘 빈 리스트 생성
account_book = []

for n in range(N):
    num = int(input())

    # 0이 입력되면, 가장 최근에 추가된 요소를 제거
    if num == 0:
        account_book.pop()
    # 0이 아닌 수가 입력되면 리스트에 추가
    else:
        account_book.append(num)

# 완성된 리스트의 요소 합 출력력
print(sum(account_book))