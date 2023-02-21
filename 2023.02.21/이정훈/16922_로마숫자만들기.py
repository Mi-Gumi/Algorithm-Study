import itertools

N = int(input())
roma_val = {'I':1,'V':5,'X':10,'L':50}

ans = set()
combination = itertools.combinations_with_replacement(roma_val.keys(), N)
for i in combination:
    ans.add(sum(map(lambda x: roma_val[x],i)))
print(len(ans))



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