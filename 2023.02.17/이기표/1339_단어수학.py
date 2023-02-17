import sys
from collections import deque
input = sys.stdin.readline
'''
단어 길이가 같을 때 짧을 때 길 때 -> 다른 글자와 동일한 글자 처리
중복을 제거하기 위한 딕셔너리 사용 / 추가 삭제가 편리한 덱 사용
'''
score = {} # 덱
N = int(input())
arr = []
arr_len = 0
ans = 0
for _ in range(N):
    arr.append(deque(input().rstrip()))

for lst in arr:
    for _ in lst:
        arr_len += 1

arr.sort(key=len, reverse=True)
result = [[] for _ in range(len(arr))]

for i in range(len(arr)): # 딕셔너리 생성 / 중복을 글자를 고려해서 사용할 수 있는 문자열
    for j in range(len(arr[i])):
        score[arr[i][j]] = -1 # 초기에 -1로 할당

cnt = 9
while 1: # 마지막 데크가 비었으면 종료
    if arr_len == 0:
        break
    target = max(arr, key=len) # 길이 비교
    idx = arr.index(target) # target의 위치 인덱스
    num = target.popleft() # target 값의 가장 큰 문자

    if score[num] == -1: # score 딕셔너리에 값이 없으면
        score[num] = cnt # score 설정
        result[idx].append(str(score[num])) # 해당 인덱스 위치에 입력
        cnt -= 1
    else:
        result[idx].append(str(score[num])) # 값이 있으면 그 값을 그대로 추가
    arr_len -= 1 # 길이 감소

for re in result: # 정답 리스트를 join으로 합치기
    ans += int(''.join(re))
print(ans)


