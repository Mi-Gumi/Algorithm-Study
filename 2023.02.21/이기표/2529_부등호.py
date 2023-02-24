import sys
input = sys.stdin.readline
'''
부등호에 해당하는 조합을 모두 찾아서 result 리스트에 넣기
'''
def backtracking(n,ans_li,dep):
    if dep == N: # 깊이가 같을 때
        result.append(''.join(list(map(str, ans_li)))) # 결과를 추가, 함수 종료
        return
    if arr[dep] == "<":
        for i in range(10):
            if i not in ans_li and i > n: # 해당하는 숫자가 정답 리스트에 없고 and i가 더 큰경우
                backtracking(i,ans_li+[i],dep+1) # 숫자를 리스트에 추가하고, 깊이 증가
    else: # > 일 떄
        for i in range(10):
            if i not in ans_li and i < n: # 해당하는 숫자가 정답 리스트에 없고 and i가 더 작은경우
                backtracking(i,ans_li+[i],dep+1) # 숫자를 리스트에 추가하고, 깊이 증가

N = int(input())
arr = list(input().split())
result = []

for i in range(10): # 낮은 값부터 시작 -> 오름차순으로 생성
    backtracking(i,[i],0)

print(result[-1]) # 최대
print(result[0]) # 최소
# print(result)