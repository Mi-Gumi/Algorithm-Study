# import sys

# N = int(sys.stdin.readline())
# num = []
# count = 0

# for i in range(N):
#     num.append(int(sys.stdin.readline()))

# for j in range(N):
#     for i in range(N - 1):
#         if num[i] > num[i + 1]:
#             tmp = num[i + 1]
#             num[i + 1] = num[i]
#             num[i] = tmp


# for n in num:
#     print(n)

import sys

N = int(sys.stdin.readline())
num = []

for i in range(N):
    num.append(int(sys.stdin.readline()))
    
num.sort()

for n in num:
    print(n)