import sys
input = sys.stdin.readline

N = int(input())
lst_num = list()

# 배열에 입력된 두 수로 만든 배열을 추가
for i in range(N):
    lst_num.append(list(map(int, input().split())))

# 정렬
lst_num = sorted(lst_num)

# 출력
for i in range(N):
    print(lst_num[i][0], lst_num[i][1])
