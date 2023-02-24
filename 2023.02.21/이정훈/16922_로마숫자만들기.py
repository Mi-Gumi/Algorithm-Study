import itertools

N = int(input())
roma_val = {'I':1,'V':5,'X':10,'L':50}

#중복 제거를 위한 Set
ans = set()
# 중복 조합
combination = itertools.combinations_with_replacement(roma_val.keys(), N)
for i in combination:
    # dict의 value로 매핑해서 sum
    ans.add(sum(map(lambda x: roma_val[x],i)))
print(len(ans))


# 중복순열 - 시간초과
# from itertools import product

# N = int(input())
# roma = {'I':1,'V':5,'X':10,'L':50}
# prod = product(roma.keys(),repeat=N)
# ans = set()
# for p in prod :
#     n = 0
#     for num in p :
#         n += roma[num]
#     ans.add(n)
# print(len(ans))