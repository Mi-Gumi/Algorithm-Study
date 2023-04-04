import sys
input = sys.stdin.readline


def check(p, n):
    # 종이 첫 부분 저장
    tmp = p[0][0]
    # 혼합 종이 표시
    flag = 0
    for l in p:
        for c in l:
            # 첫 부분과 다른 부분이 있다면 break
            if c != tmp:
                flag = 1
                break
        if flag:
            break
    
    # 종이가 섞여있다면
    if flag:
        for i in range(3):
            for j in range(3):
                divide_paper = []
                # 9등분 해서 다시 확인
                for k in range(n // 3):
                    divide_paper.append(p[i * n // 3 + k][j * n // 3:(j + 1) * n // 3])
                check(divide_paper, n // 3)
    # 한 숫자로 된 종이라면
    else:
        # 각 종이에 맞는 count + 1
        if tmp == -1:
            ans[0] += 1
        elif tmp == 0:
            ans[1] += 1
        else:
            ans[2] += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]

check(paper, N)

for num in ans:
    print(num)