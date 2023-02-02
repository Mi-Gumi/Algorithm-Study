def find(n):

    # case 갯수를 담을 변수
    count = 0

    # 모든 case를 탐색해야 함으로 elif대신 if사용
    # n이 3이상이라면
    if n >= 3:
        # n - 3 에서 다시 case 탐색 시작
        count += find(n - 3)

    # n이 2이상이라면
    if n >= 2:
        # n - 2 에서 다시 case 탐색 시작
        count += find(n - 2)
    
    # n이 1이상이라면
    if n >= 1:
        # n - 1 에서 다시 case 탐색 시작
        count += find(n - 1)
    
    # n이 0이라면
    if n == 0:
        # 하나의 케이스를 찾아낸 것임으로 count + 1
        count += 1

    # count 반환
    return count

T = int(input())

# 매번 n에서 부터 case탐색을 시작하면 오래걸림
# 중간 계산값부터 case탐색을 시작하기 위해 재귀함수 사용
for _ in range(T):
    n = int(input())
    print(find(n))