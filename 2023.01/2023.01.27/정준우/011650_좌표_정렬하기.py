N = int(input())

# [x, y]를 리스트 안에 넣고 정렬 후, 각 요소를 한 줄씩 출력
# * 를 통해 [  ]를 없애고 형식에 맞게 출력
lists = []

for i in range(N):
    x, y = map(int, input().split())
    lists.append([x, y])

lists.sort()

for i in range(N):
    print(*lists[i])