N = int(input())
c = 0
nums = map(int, input().split())
for i in nums:
    d = 0
    if i > 1 :

        for j in range(2,i):
            if i%j == 0 :
                d += 1
        if d == 0:
            c += 1
print(c)
