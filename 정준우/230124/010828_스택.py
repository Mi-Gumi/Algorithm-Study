import sys

N = int(sys.stdin.readline())

stack = list()

# 각 명령어별로 수행할 작업 조건문으로 표현
for i in range(N):
    # push 명령 때문에 입력값을 리스트화해 인덱스로 명령과 숫자 구분
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(int(stack[-1]))
            # arr.pop(x) 사용 시, arr[x]를 반환 후 제거 
            # .pop(x)의 x 기본값은 -1
            stack.pop()

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(int(stack[-1]))