import sys

N = int(input())
arr_stack = []
for _ in range(N) :
    commend = input()
    
    if commend[0:4] == 'push' :
        arr_stack.append(int(commend[5::]))
    if commend == 'pop' :
        if len(arr_stack) != 0 :
            print(arr_stack.pop())
        else : 
            print(-1)
    if commend == 'empty' :
        if len(arr_stack) != 0 :
            print(0)
        else :
            print(1)
    if commend == 'size' :
        print(len(arr_stack))
    if commend == 'top' :
        if len(arr_stack) != 0 :
            print(arr_stack[-1])
        else :
            print(-1)