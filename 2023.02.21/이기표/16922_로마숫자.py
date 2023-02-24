import sys
from itertools import combinations_with_replacement
# 중복 조합 개수 카운트 X
input = sys.stdin.readline
N = int(input())
roma = [1,5,10,50]
ans = list(combinations_with_replacement(roma, N))
ans_li = []
for num in ans:
    ans_li.append(sum(num))
ans_li = set(ans_li) # 중복 제거
print(len(ans_li))