import sys
input = sys.stdin.readline

n = int(input())

# 비교대상이 될 배열, 인덱스, 스택, 스택에 들어갈 숫자, 정답 배열 선언 및 초기화
comp_list = []
comp_idx = 0
stack = []
i = 1
ans_list = []

# 비교대상 배열에 값 추가
for _ in range(n):
    comp_list.append(int(input()))

# 정답 배열의 길이가 n * 2가 될때 까지
while len(ans_list) < n * 2:

    # 스택이 비어있거나 스택의 마지막 요소가 비교대상 배열의 비고 대상보다 작다면
    # 스택에 i push 후 i + 1 정답 배열에 + 추가
    if stack[-1] < comp_list[comp_idx] or not stack:
        stack.append(i)
        i += 1
        ans_list.append('+')

    # 스택의 마지막 요소가 비교대상 배열의 비교 대상과 같다면
    # 스택의 마지막 요소를 pop하고 비교 대상 인덱스 + 1, 정답 배열에 - 추가
    elif stack[-1] == comp_list[comp_idx]:
        stack.pop()
        comp_idx += 1
        ans_list.append('-')
    
    # 스택의 마지막 요소가 비교대상 배열의 비교 대상보다 크다면
    # 동일 배열 출력이 불가능 함으로 NO 출력 후 break
    else:
        print('NO')
        break

# 정답 배열의 길이가 n * 2라면 while문을 통과한 것임으로 정답 배열 출력
if len(ans_list) == n * 2:
    for pm in ans_list:
        print(pm)