import sys
input = sys.stdin.readline

N = int(input())
# 첫번째 스위치를 누른 경우와 누르지 않은 경우 리스트 두개 생성
light = [list(map(int, input().strip()))]
light_2 = light[0][:]
light_2[0] = 1 - light_2[0]
light_2[1] = 1 - light_2[1]
light.append(light_2)
result = list(map(int, input().strip()))
ans = -1

for i in range(2):
    # 스위치를 누른 경우는 count 1부터 시작
    count = i
    for j in range(1, N):
        # 만약 전 스위치가 정답과 다르다면 스위치 누름
        if light[i][j - 1] != result[j - 1]:
            if j != N - 1:
                for k in range(3):
                    light[i][j - 1 + k] = 1 - light[i][j - 1 + k]
            # 마지막 스위치라면 범위 안나가게 조절
            else:
                for k in range(2):
                    light[i][j - 1 + k] = 1 - light[i][j - 1 + k]
            count += 1
    # 정답과 같다면 ans 교체
    if light[i] == result:
        ans = count
        break

print(ans)