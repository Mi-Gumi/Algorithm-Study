N = input()
n = int(N)

n_lst = list(map(int, list(N)))

size = len(n_lst)
is_used = [False for _ in range(size)]
n_lst.sort()

# 156 = 100 + 50 + 6
rlt = 0
def bt(depth, target, ans):    
    global rlt
    if depth == (size+1):
        if ans > target:
            rlt = ans
            return True
        return False

    for i in range(len(n_lst)):
        if is_used[i] : 
            continue
        a = n_lst[i] * 10**(size - depth)
        t = target - target%10**(size-depth)

        if a + ans < t:
            continue 
        
        ans += a
        is_used[i] = True
        trigger = bt(depth+1, target,ans)

        if trigger:
            return True

        is_used[i] = False
        ans -= a

bt(1, n, 0)
print(rlt)