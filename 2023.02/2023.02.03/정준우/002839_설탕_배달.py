import sys

sugar = int(sys.stdin.readline())

# 3kg, 5kg 관계 없이 옮긴 설탕 봉지의 수
sugar_bag = 0

# 설탕이 남아있는 한 반복
while sugar >= 0:
    # 처음부터 설탕이 5kg로 딱 맞게 나누어지면 5로 나눈 몫을 sugar_bag 으로 지정하고 출력 후 반복 중단
    if sugar % 5 == 0:
        sugar_bag += (sugar // 5)
        print(sugar_bag)
        break
    # 5kg으로 딱 맞게 나누어지지 않으면, 일단 3kg만큼 빼고 봉지 수 +1 해준 후, 다시 반복
    else:
        sugar -= 3
        sugar_bag += 1

# 정확히 나눌 수 없는 경우 반복문이 끝나면 설탕의 양은 음수가 되므로, 그럴 때는 -1 출력
if sugar < 0:
    print(-1)