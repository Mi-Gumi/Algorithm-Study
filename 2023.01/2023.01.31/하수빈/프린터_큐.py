import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    printer_queue = []
    N, M = map(int, input().split())

    # 우선순위 배열 생성
    waiting_list = list(map(int, input().split()))

    # 큐에 들어간 순서를 알려줄 변수 생성
    order = 0

    # 몇번째 인지 알려줄 변수 생성
    count = 1

    # 우선순위와 큐에 들어간 순서를 튜플로 queue에 push
    for num in waiting_list:
        printer_queue.append((num, order))
        order += 1

    # 큐의 길이만큼
    for _ in range(len(printer_queue)):
        while True:

            # 큐의 0인덱스 요소와 1인덱스 이상의 요소들을 비교하기 위해 range를 1부터 시작
            for i in range(1, len(printer_queue)):

                # 0인덱스 요소의 우선순위 보다 j인덱스 요소의 우선순위가 크다면
                # 0인덱스 요소를 큐의 제일 뒤로 보낸 후 break
                if printer_queue[0][0] < printer_queue[i][0]:
                    tmp = printer_queue.pop(0)
                    printer_queue.append(tmp)
                    break
            
            # for 문을 통과했다면 큐의 가장 앞에 있는 값을 pop한 후 break
            else:
                tmp = printer_queue.pop(0)
                break
        
        # pop한 값의 순서가 M과 같다면 count 출력 후 break
        if tmp[1] == M:
            print(count)
            break

        # 아니라면 count + 1
        count += 1
