T = int(input())

# 동일 거리 아래층 선호
for t in range(T):
    H, W, N = map(int, input().split())
    rooms = list()
    for i in range(1, W+1):
        for j in range(1, H+1):
            if i >= 10:
                room = f'{j}{i}'
                rooms.append(room)
            else:
                room = f'{j}0{i}'
                rooms.append(room)
                # f'{j} {i}'
    print(rooms[N-1])
