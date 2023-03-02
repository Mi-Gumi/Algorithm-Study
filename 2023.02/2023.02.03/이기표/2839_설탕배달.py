import sys
input = sys.stdin.readline

N = int(input())

ans = 0
if N % 5 == 0: # 5 배수일 때
    ans = N//5

elif N >= 5: # 5 이상일 때
    while 1:
        N = N - 3
        ans += 1

        if N % 5 == 0:
            ans += N//5
            break

        if N == 0:
            break

        if N == 4: # 4가 나오는 경우의 수는 불가
            ans = -1
            break

else: # 5 이하일때
    if N % 3 == 0:
        ans += 1

    else: # 1,2,4는 불가
        ans = -1

print(ans)


