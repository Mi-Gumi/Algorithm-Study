import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def postorder(tree, start, end):
    # start가 end보다 커지면 멈추도록 설정
    if start > end:
        return
    # mid를 end + 1로 설정
    mid = end + 1
    for i in range(start + 1, end + 1):
        # start보다 큰 부분이 나온다면 그 부분을 중심으로 좌측은 왼쪽 트리를 전위순회한 결과 우측은 오른쪽 트리를 전위순회한 결과로 나눌 수 있음
        if tree[start] < tree[i]:
            mid = i
            break
    
    # 좌측 트리 후위 순회
    postorder(tree, start + 1, mid - 1)
    # 우측 트리 후위 순회
    postorder(tree, mid, end)
    # 현재 노드 출력
    print(tree[start])

num_list = []
while True:
    try:
        num_list.append(int(input()))
    except:
        break

postorder(num_list, 0, len(num_list) - 1)