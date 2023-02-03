T = int(input())

dp_arr = [0]*11
dp_arr[1] = 1
dp_arr[2] = 2
dp_arr[3] = 4

for i in range(4,10+1) :
    dp_arr[i] = dp_arr[i-3] + dp_arr[i-2] + dp_arr[i-1]

for tc in range(1, 1+T) :
    N = int(input())
    print(dp_arr[N])

