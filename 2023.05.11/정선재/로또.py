import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break

    length = nums.pop(0)

    for comb in combinations(nums, 6):
        temp = list(map(str, comb))
        print(" ".join(temp))
    print()
