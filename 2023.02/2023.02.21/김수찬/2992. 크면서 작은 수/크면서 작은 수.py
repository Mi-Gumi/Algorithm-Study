N = input()
n = int(N)

n_lst = list(map(int, list(N)))

size = len(n_lst)
is_used = [False for _ in range(size)]
n_lst.sort() # 최솟값부터 배열을 만들어둠

# 156 = 100 + 50 + 6
rlt = 0
def bt(depth, target, ans): 
    global rlt
    if depth == (size+1): # 편의성을 위해 1으로 depht를 지정했으므로, size +1 을 해줘야 자릿수를 맞춰줄 수 있다.
        if ans > target:
            rlt = ans
            return True
        return False

    for i in range(len(n_lst)):
        if is_used[i] : # 백트래킹 부분 : 사용된 숫자는 다시 사용안하는게 문제의 조건
            continue
        a = n_lst[i] * 10**(size - depth)
        t = target - target%10**(size-depth)

        if a + ans < t: # 백트래킹 부분  숫자를 앞에서 부터 비교할텐데,
            continue   #  ex) 1516일 경우 연산을 할 때 11xx일 경우 고려할 필요가 없음
        
        ans += a # target으로 고려할 값은 더해줌
        is_used[i] = True # 사용했다고 흔적을 남김
        
        trigger = bt(depth+1, target,ans) # 재귀함수 시작

        if trigger: # True가 나올경우 계산을 멈춰도 상관없다.
            return True

        is_used[i] = False
        ans -= a # 연산을 했기 때문에 다시 빼줘야함

bt(1, n, 0) # 1의 자리부터 탐색하기 때문에 편의성의 측면에서 1을 사용
print(rlt)