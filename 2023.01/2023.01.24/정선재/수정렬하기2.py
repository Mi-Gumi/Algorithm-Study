import sys
input=sys.stdin.readline

n=int(input())
li=[]

for i in range(n):
    li.append(int(input()))

for i in sorted(li):
    print(i)

# import sys

# n = int(input())
# num = []
# for _ in range(n):
#     num.append(int(sys.stdin.readline()))

# num.sort()

# for i in num:
#     print(i)