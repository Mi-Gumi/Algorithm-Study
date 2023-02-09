import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
output_li = list(map(int, input().split()))
dual_que = deque(range(1,N+1)) # 데크
cnt = 0
que = []

for i in range(len(output_li)):

    if output_li[i] == dual_que[0]: # 동일한 수면 정답비교 리스트에 추가
        num = dual_que.popleft()
        que.append(num)
        # print('1번', dual_que)
    else:
        if (len(dual_que)//2) >= dual_que.index(output_li[i]):  # 비교수가 더 큰 경우는 2번 연산 ### 조건 추가
            while dual_que[0] != output_li[i]:
                cnt += 1
                num = dual_que.popleft()
                dual_que.append(num)
                # print('2번', dual_que)
            # print('2번 cnt', cnt)
            num = dual_que.popleft()
            que.append(num)
            # print('1번', dual_que)
        else: ###output_li[i] > dual_que[0]:   # 비교수가 더 작은 경우는 3번 연산
            while dual_que[0] != output_li[i]:
                cnt += 1
                num = dual_que.pop()
                dual_que.appendleft(num)
                # print('3번', dual_que)
            # print('3번 cnt', cnt)
            num = dual_que.popleft()
            que.append(num)
            # print('1번', dual_que)

print(cnt)






