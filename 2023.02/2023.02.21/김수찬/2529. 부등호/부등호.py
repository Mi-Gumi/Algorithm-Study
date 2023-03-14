def compare(oper, num1, num2):
    if num1 > num2 and oper == '>' :
        return True
    if num1 < num2 and oper == '<':
        return True
    return False


def bt(depth, number, numbers):
    global is_used

    if len(ans) > K:
        return True

    for i in numbers:
        if is_used[i] : 
            continue

        if compare(target[depth], number, i):
            is_used[i] = True
            ans.append(i)

            if bt(depth+1, i, numbers):
                return True
            
            is_used[i] = False
            ans.pop()

    return False

K = int(input())



rlt = []
target = list(map(str, input().split()))
## 9부터 1까지의 조합
nums = [ (9 - i) for i in range(10)]
is_used = [False for _ in range(10)]
ans =[]
for num in nums:
    ans.append(num)
    is_used[num] = True
    
    is_passed = bt(0, num, nums)
    if is_passed :
        rlt.append(ans)
        break

    ans.pop()
    is_used[num] = False

## 1부터 9까지의 조합
nums = [ i for i in range(10)]
is_used = [False for _ in range(10)]
ans =[]
for num in nums:
    ans.append(num)
    is_used[num] = True
    
    is_passed = bt(0, num, nums)
    if is_passed :
        rlt.append(ans)
        break

    ans.pop()
    is_used[num] = False

for row in rlt:
    print(*row, sep='', end='\n')
