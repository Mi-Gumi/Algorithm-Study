n, m, k = map(int,input().split())

fire = dict()

d = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
split_fire = { 0:(0,2,4,6), 1:(1,3,5,7) }
for _ in range(m) :
    i, j, weight, speed, direction = map(int,input().split())
    i, j = i-1, j-1
    di, dj = d[direction]
    # 입력을 받을 때 이동시킨 후 좌표값을 키로 하는 dict에 등록
    ni = (i + speed * di)%n
    nj = (j + speed * dj)%n
    if fire.get((ni,nj)) :
        fire[(ni,nj)].append((weight, speed, direction))
    else :
        fire[(ni,nj)] = [(weight, speed, direction)]

for _ in range(k) :
    # 다음 분기
    next = dict()

    # 좌표마다 합치고 이동
    for (si, sj), lst in fire.items():
        total_weight = 0
        total_speed = 0
        is_same = 0
        fireball_count = 0

        # 총 무게, 속도, 방향 계산
        for weight, speed, direction in lst :
            total_weight+=weight
            total_speed+=speed
            is_same += direction%2
            fireball_count += 1

        # 두개 이상이라서 합쳐지고 쪼개짐
        if fireball_count > 1:
            weight = total_weight//5
            if not weight :
                continue
            speed = total_speed // fireball_count

            # 모두 짝수라면 합은 0, 모두 홀수라면 그 개수와 같다
            if not is_same or is_same == fireball_count :
                is_same = 0
            else :
                is_same = 1
            
            # 네방향 쪼개짐
            for direction in split_fire[is_same] :
                di, dj = d[direction]
                ni = (si + speed * di)%n
                nj = (sj + speed * dj)%n
                if next.get((ni,nj)) :
                    next[(ni,nj)].append((weight, speed , direction))
                else :
                    next[(ni,nj)] = [(weight, speed, direction)]
        # 하나라서 이동만
        else :
            di, dj = d[direction]
            ni = (si + speed * di)%n
            nj = (sj + speed * dj)%n
            if next.get((ni,nj)) :
                next[(ni,nj)].append((weight, speed , direction))
            else :
                next[(ni,nj)] = [(weight, speed, direction)]
    fire = next

# 최종 무게
total_weight = 0
for lst in fire.values():
    for weight, speed, direction in lst :
        total_weight += weight
        
print(total_weight)