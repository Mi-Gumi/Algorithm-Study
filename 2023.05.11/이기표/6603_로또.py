'''
먼저 로또라는 것은 N개의 수에서 6개를 중복없이 뽑는 것이기 때문에
조합(Combination)이라고 할 수 있습니다.
1. 재귀함수를 통해 N개에서 6개를 뽑을 수 있는 조합을 완성한다.
'''
def lotto(n, r, s, k):
    # 뽑은 숫자의 개수가 6개면 종료
    if k == 6:
        print(*tmp)
        return
    # 로또 숫자 뽑기
    for i in range(s, n-r+k+1):
        tmp[k] = lst[i]
        # depth를 1 늘려주어 재귀 진행
        lotto(n, r, i+1, k+1)

while 1:
    lst = list(map(int, input().split()))
    # 개수가 0개이면 종료
    N = lst.pop(0)
    if N == 0:
        break
    # 6개의 로또 숫자가 들어갈 리스트
    tmp = [0] * 6
    lotto(N, 6, 0, 0)
    print()