import itertools
N, M = map(int, input().split())
card = [0] * N
card = list(map(int, input().split()))

combi = list(itertools.combinations(card,3))

sum_li = []
for c in combi:
    if sum(c) <= M:
        sum_li.append(sum(c))

print(sorted(sum_li)[-1])
