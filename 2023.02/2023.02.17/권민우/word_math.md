import sys
input = sys.stdin.readline

N = int(input())
lst = []
lst_dict = {}

# 리스트화
for _ in range(N):
    lst.append(input().strip())

# 모든 배열을 lst의 i번째 단어의 길이 만큼 
for i in range(N):
    for j in range(len(lst[i])):
        if lst[i][j]:
            pass

# cnting으로 해줘야하나...?
