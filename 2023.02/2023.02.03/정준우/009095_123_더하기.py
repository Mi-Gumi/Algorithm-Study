# 1에서 3까지 직접 구한 후, 4를 구할 때는
# 3을 구성하는 요소에 다 1을 더하고, 2를 구성하는 요소에 2, 1을 구성하는 요소에 3을 더하면 4의 요소들이 나온다
# 5의 경우에는 2, 3, 4에서 똑같이 적용되는 것을 확인했고 그저 숫자를 더한 것이기 때문에 가짓수는 앞 3가지 경우의 가짓수를 더한 것

def tool(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    else:
        return tool(x-1) + tool(x-2) + tool(x-3)


T = int(input())
for test_case in range(T):
    num = int(input())
    print(tool(num))
