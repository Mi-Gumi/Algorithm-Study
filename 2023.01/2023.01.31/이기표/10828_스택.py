import sys
T = int(input())
stack = []
for t in range(T):
    func = sys.stdin.readline().rstrip()

    if func[1] == 'u':
        func = func.split()
        stack.append(int(func[1]))

    elif func == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(len(stack) - 1)

    elif func == 'size':
        print(len(stack))

    elif func == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)

    elif func == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
