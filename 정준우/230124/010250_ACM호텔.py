N = int(input())

for i in range(N):
    max_floor, max_room, customer = map(int, input().split())
    
    # 손님 번호가 층 개수와 나누어떨어지면,
    # 층은 최고층 고정, 방 번호는 손님 번호를 최고층으로 나눴을 때의 몫
    # 방 번호가 10 이상이 아니라면, 사이에 '0' 넣어주기
    if customer % max_floor == 0:
        if (customer // max_floor) >= 10:
            room = str(max_floor) + str(customer // max_floor)
        else:
            room = str(max_floor) + '0' + str(customer // max_floor)

    # 손님 번호가 층 개수와 나누어떨어지지 않으면,
    # 손님 번호를 최고층으로 나눴을 때의 나머지는 층, 방 번호는 1부터 시작하므로 몫 + 1
    # 방 번호가 10 이상이 아니라면, 사이에 '0' 넣어주기    
    else:
        if ((customer // max_floor) + 1) >= 10:
            room = str(customer % max_floor) + str((customer // max_floor) + 1)
        else:
            room = str(customer % max_floor) + '0' + str((customer // max_floor) + 1)

    # 문자열로 데이터를 얻었으니, 마지막에 정수로 형변환
    print(int(room))