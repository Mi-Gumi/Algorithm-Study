import sys
N = int(sys.stdin.readline())
r = []
for _ in range(N):
    r.append(int(sys.stdin.readline()))
r.sort(reverse=True) # 로프가 담길 위치 (역순처리함)

temp_max = r[0] # 처음으로 생각한 가장 큰 무게 = 로프 단일로 버티는 하중
# 로프의 수가 늘어나면 그만큼 하중이 배가 되나, 
# 로프가 버티는 무게가 달라지기 때문에, 이를 고려하여 계산해야함
for i in range(N):
    mr = r[i]*(i+1) # 다음 attempt에서 하중이 얼마나 버티는지 계산
    if mr > temp_max: # 이를 temp_max와 비교
        temp_max = mr

print(temp_max) # 마지막에 나온 결과값 출력
