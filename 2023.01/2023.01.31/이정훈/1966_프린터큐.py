T = int(input())

for testcase in range(T) :
    N , M = map(int,input().split())
    count = 0
    queue = list(map(int,input().strip().split(' ')))

    now_index = M
    flag = True

    while flag :
        for i in range(1, len(queue)) :
            if queue[0] < queue[i] :
                queue.append(queue.pop(0))
                if now_index == 0 :
                    now_index = len(queue)-1
                else :
                    now_index -= 1
                break
        else :
            queue.pop(0)
            if now_index == 0 :
                flag = False
                count += 1 
                break
            else :
                now_index -= 1
                count += 1
    print(count)

        
            



