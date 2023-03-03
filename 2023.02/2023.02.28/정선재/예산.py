N = int(input())
_list = list(map(int,input().split())) 
tar = int(input())  # 총 값을 저장
_list.sort(reverse=True) # 리스트를 내림차순으로 정렬

if sum(_list) <= tar: # 만약 리스트를 더한 값이 총 값보다 적다면
    print(_list[0]) # 바로 제일 큰값을 프린트
else:
    flag = 1
    while flag: 
        if tar//len(_list) < _list[-1]: # 만약 전체 평균이 젤 작은 수보다 작다면
            print(tar//len(_list)) # 전체 평균을 프린트
            flag = 0
            break
        else:  
            tar = tar - _list.pop()            # 그렇지 않다면 젤 작은 수를 팝 후 다시 와일문 돌리기.

