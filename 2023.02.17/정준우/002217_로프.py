num_of_ropes = int(input())

ropes = [int(input()) for _ in range(num_of_ropes)]

# 로프를 최대한 달며 버틸 수 있는 중량을 늘리려면, 로프의 수가 적을 때 감당할 수 있는 중량이 커야 하므로,
# 가장 강한 로프부터 매달기 위해 내림차순으로 로프의 리스트 정렬
ropes.sort(reverse = True)

possible_weight = []

# 가장 약한 로프가 버틸 수 있는 무게를 weak 라고 했을 때,
# w / k = weak
# 버틸 수 있는 중량 w = 로프의 개수 k * 가장 약한 로프가 버틸 수 있는 무게
# 로프가 추가될 때마다 버틸 수 있는 중량은 k를 1씩 더해주며 가장 약한 로프가 버틸 수 있는 무게에 곱한 값
for rope in range(num_of_ropes):
    possible_weight += [ropes[rope] * (rope + 1)]

print(max(possible_weight))
