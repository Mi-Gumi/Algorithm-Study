import sys
input = sys.stdin.readline

N = int(input())
ans = 0
target = input().strip()
target_dict = {}

# 각 스펠링별 dict 생성
for c in target:
    if target_dict.get(c):
        target_dict[c] += 1
    else:
        target_dict[c] = 1

for _ in range(N - 1):
    s = input().strip()
    # 딕셔너리 복사
    new_dict = target_dict.copy()
    o_cnt = 0
    for c in s:
        # 스펠링이 남아있다면 -1
        if new_dict.get(c):
            new_dict[c] -= 1
        # 아니라면 o_cnt + 1
        else:
            o_cnt += 1
    
    i_cnt = 0
    for key in new_dict.keys():
        # 딕셔너리에 남아있는 스펠링 갯수 체크
        i_cnt += new_dict[key]
        
    # o_cnt와 i_cnt가 모두 1이라 한번 교체로 해결할 수 있거나 i_cnt + o_cnt가 1보다 작거나 같다면 ans + 1
    if (i_cnt == 1 and o_cnt == 1) or (i_cnt + o_cnt) <= 1:
        ans += 1

print(ans)