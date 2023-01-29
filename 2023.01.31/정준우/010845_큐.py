import sys

N = int(sys.stdin.readline())

# 큐로 사용할 빈 리스트 생성
queue = []

for _ in range(N):
    command = sys.stdin.readline()
    # command를 한칸 공백으로 나눈 것 중 두 번째 요소를 리스트에 추가
    if 'push' in command:
        queue.append(int(command.split(' ')[1]))
    elif 'pop' in command:
        if not queue:
            print(-1)
        # queue 리스트의 0번 인덱스 요소를 제거하면서 동시에 반환해 출력력
        else:
            print(queue.pop(0))
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if not queue:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in command:
        if not queue:
            print(-1)
        else:
            print(queue[-1])