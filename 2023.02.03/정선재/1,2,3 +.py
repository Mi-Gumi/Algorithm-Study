T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    ans = [1,2,4,7]

    if 0 < n < 4:
        print(ans[n-1])

    else:
        for i in range(4, n):
            ans_value = ans[i-1]+(ans[i-1]-ans[i-4])
            ans.append(ans_value)
        print(ans[-1])