import sys

# 명령어에 따른 처리 함수 구현
# 명령어와 처리할 배열을 인자로 받음
def cmd_queue(cmd, arr):

    # push가 명령어 안에 있다면 cmd를 'push'와 num으로 나눈후 arr 가장 뒤에 num추가
    # None 반환
    if 'push' in cmd:
        tmp_cmd, num = cmd.split()
        arr.append(int(num))
        return
        

    # pop명령어가 들어온다면 배열 가장 앞에 있는 원소를 pop 하고 반환, 배열이 빈 배열이라면 -1 반환
    elif 'pop' in cmd:
        if arr:
            return arr.pop(0)
        else:
            return -1
        
    # size명령어가 들어온다면 배열의 길이를 반환
    elif 'size' in cmd:
        return len(arr)
    
    # empty명령어가 들어온다면 arr가 차있다면 0 반환, 비었다면 1 반환
    elif 'empty' in cmd:
        if arr:
            return 0
        else:
            return 1
    
    # front명령어가 들어온다면 arr 가장 앞에 있는 원소를 반환, 빈 배열이라면 -1 반환
    elif 'front' in cmd:
        if arr:
            return arr[0]
        else:
            return -1    
    
    # back명령어가 들어온다면 arr 가장 뒤에 있는 원소를 반환, 빈 배열이라면 -1 반환
    elif 'back' in cmd:
        if arr:
            return (arr[len(arr) - 1])
        else:
            return -1
        
cnt = int(sys.stdin.readline())
arr_queue = []

for i in range(cnt):
    command = sys.stdin.readline()
    ans = cmd_queue(command, arr_queue)
    # 반환값이 None이 아니라면 ans 출력
    if ans != None:
        print(ans)
