import sys
input = sys.stdin.readline


def recur(N, k, s):
    global max_num, min_num

    # 마지막 부등호 까지 모두 처리했을때 최대값 최소값 교환
    if N == k:
        if int(s) > int(max_num):
            max_num = s
        if int(s) < int(min_num):
            min_num = s
        return

    # 사용한 숫자 표기
    visited[int(s[-1])] = 1

    # > 부등호라면
    if inequality[k] == '>':

        # s의 마지막 글자가 0이라면 종료
        if s[-1] == '0':
            visited[int(s[-1])] = 0
            return
        
        # s의 마지막 글자가 0이 아니라면
        else:
            # 사용할 수 있고 사용한적 없는 숫자들에 대해 다시 recur
            for i in range(int(s[-1]) - 1, -1, -1):
                if not visited[i]:
                    recur(N, k + 1, s + str(i))
    # < 부등호라면
    else:

        # s의 마지막 글자가 9라면 종료
        if s[-1] == '9':
            visited[int(s[-1])] = 0
            return
        # s의 마지막 글자가 9가 아니라면
        else:
            # 사용할 수 있고 사용한적 없는 숫자들에 대해 다시 recur
            for i in range(int(s[-1]), 10):
                if not visited[i]:
                    recur(N, k + 1, s + str(i))
    
    # 사용 표기 해제
    visited[int(s[-1])] = 0


N = int(input())
inequality = list(input().split())
visited = [0] * 10
num_list = list(range(10))
max_num = '0' * (N + 1)
min_num = '9' * (N + 1)

for num in num_list:
    recur(N, 0, str(num))

print(max_num)
print(min_num)
