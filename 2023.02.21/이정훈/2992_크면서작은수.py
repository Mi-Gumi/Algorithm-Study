from itertools import permutations

n = input()
m = sorted(list(n))
p = map(lambda x : int(''.join(x)),permutations(m, len(n)))

n = int(n)
ans = 0
for num in p :
    if n < num:
        ans = num
        break
print(ans)