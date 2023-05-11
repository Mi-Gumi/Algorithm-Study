'''
1. 오름차순으로 정렬 진행
2. 리스트에서 가장 작은 값인 첫번째와 두번째값을 합치기
3. 정답 변수에 합친 값을 누적
4. 위의 과정을 리스트 요소가 하나가 될 때까지 반복
'''
import sys
input = sys.stdin.readline
N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))
ans = 0

while len(lst) != 1:
    lst.sort()
    num = lst.pop(0)
    lst[0] += num
    ans += lst[0]
print(ans)