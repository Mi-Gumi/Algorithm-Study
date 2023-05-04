'''
두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나,
하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에
이들 두 단어를 서로 비슷한 단어라고 한다.

1. 목표값과 비교 (같은 글자와 같지 않지 글자 수를 카운트)
2. 같은 글자가 존재하면 타겟값의 글자를 삭제
3. 존재하지 않으면 check변수에 증가
4. 최종적으로 단어에서 한 문자를 더하고 뺀 경우를 구하기
'''
N = int(input())
lst = [input() for _ in range(N)]
target = list(lst.pop(0))

ans = 0
for word in lst:
    tmp = target[:] # 타겟값
    check = 0
    for w in word:
        if w in tmp: # 같은 글자가 존재하면 삭제
            for i in range(len(tmp)):
                if w == tmp[i]:
                    tmp.pop(i)
                    break
        else:
            check += 1

    if check <= 1: # 다른 글자가 한 개 있거나
        if len(tmp) <= 1: # 글자가 하나 부족하면
            ans += 1 # 비슷한 단어
print(ans)