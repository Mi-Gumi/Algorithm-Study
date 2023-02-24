import sys
input = sys.stdin.readline
N = int(input())
print(max([(N - i)*k for i,k in enumerate([int(input()) for i in range(N)].sort())]))

<<<<<<< HEAD
for i in range(N) :
    lopes[i] *= N-i # 아이디어 좋다
print(max(lopes))
=======
ropes = [int(input()) for i in range(N)]
ropes.sort()
for i in range(N) : #최소값 * 사용한 로프 수 
    ropes[i] *= N-i
print(max(ropes)) # 모든 경우의 수중 최대중량
>>>>>>> 56113e9b27f000eb102a402e1e6c19744369df29

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