import sys

# 명령어에 따른 처리 함수 구현
# 명령어와 처리할 배열을 인자로 받음
def stack(cmd, arr):
    # push가 명령어 안에 있다면 cmd를 'push'와 num으로 나눈후 arr 가장 뒤에 num추가
    if 'push' in cmd:
        tmp_cmd, num = cmd.split()
        arr.append(int(num))
    # pop명령어가 들어온다면 배열 가장 뒤에 있는 원소를 pop 하고 출력, 배열이 빈 배열이라면 -1 출력
    elif 'pop' in cmd:
        if arr:
            print(arr.pop(len(arr) - 1))
        else:
            print(-1)
    # size명령어가 들어온다면 배열의 길이를 출력
    elif 'size' in cmd:
        print(len(arr))
    # empty명령어가 들어온다면 arr가 차있다면 0 출력, 비었다면 1 출력
    elif 'empty' in cmd:
        if arr:
            print(0)
        else:
            print(1)
    # top명령어가 들어온다면 arr 가장 뒤에 있는 원소를 출력, 빈 배열이라면 -1 출력
    elif 'top' in cmd:
        if arr:
            print(arr[len(arr) - 1])
        else:
            print(-1)

cnt = int(sys.stdin.readline())
arr_stack = []

for i in range(cnt):
    command = sys.stdin.readline()
    stack(command, arr_stack)
