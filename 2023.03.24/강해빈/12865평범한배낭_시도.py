N, K = map(int, input().split()) # 물건 수 N, 버틸 수 있는 무게 K

items = [list(map(int, input().split())) for _ in range(N)] # 물건 무게 W, 가치 V

print(items)


bb = []
for n in range(N):

    bag = []
    idx = []
    for w, v in items:
        while sum(bag) < K:
            bag.append(w)
            idx.append()
            print(bag)
            if sum(bag) > K:
                bag.pop()
                break
            
    bb.append(bag)
    items.pop(0)

print(bb)
