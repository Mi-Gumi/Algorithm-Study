from itertools import combinations

while True :
    n, *arr = list(map(int,input().split()))

    if arr == [] : 
        break
    combi = list(combinations(arr, 6))

    for c in combi :
        print(*c)
    print()