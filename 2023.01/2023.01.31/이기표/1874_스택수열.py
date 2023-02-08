import sys
input = sys.stdin.readline
T = int(input())
stack = []
push_pop_li = []
start = 1
for t in range(T):
    n = int(input())

    for i in range(start, n+1): # 시작점부터 해당 수까지 push
        stack.append(i)
        push_pop_li.append('+')
        start += 1 # 시작점을 증가하여 새로운 시작점으로 초기화

    if stack[-1] == n: # stack에 들어가야 될 수라면 pop
        stack.pop()
        push_pop_li.append('-')

if len(stack) == 0:
    print(*push_pop_li, sep='\n')
else:
    print('NO')
