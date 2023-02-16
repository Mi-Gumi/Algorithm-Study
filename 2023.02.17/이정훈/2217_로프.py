import sys
input = sys.stdin.readline
N = int(input())

lopes = [int(input()) for i in range(N)]
lopes.sort()
for i in range(N) :
    lopes[i] *= N-i
print(max(lopes))

# cnt = 1
# last = 0
# while cnt < N+1 :
#     tmp = lopes[-cnt] * cnt
#     if last >= tmp :
#         break
#     else:
#         cnt += 1
#         last = tmp
#
# print(last)

# 4  5  6  7  8  10 15
# 28 30 30 28 24 20 15