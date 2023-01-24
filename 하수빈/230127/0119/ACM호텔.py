T = int(input())

for test_case in range(T):
    H, W, N = map(int, input().split())
 
    # N % H가 0이면 꼭대기 층이므로 floor = H
    # 몫도 1증가함으로 -1
    if N % H == 0:
        floor = H
        room = N // H
    # N % H가 층수 N // H + 1이 호수
    else:
        floor = N % H
        room = N // H + 1
    # 호수 최대치가 99임으로 두자리 까지 0추가
    ans = str(floor) + str(room).zfill(2)

    print(f'{ans}')