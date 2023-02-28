# from collections import deque
# parent = dict()

# def bfs(start):
#     que = deque()
#     que.append(start)
#     while que:
#         now = que.popleft()
#         is_visited[now] = True
#         for item in nodes[now]:
#             if is_visited[item] == True: continue
#             parent[item] = now
#             que.append(item)

# def dfs(start):
#     is_visited[start] = True

#     if nodes.get(start):
#         for item in nodes[start]:
#             if is_visited[item] == True: continue
#             is_visited[item] = False
#             parent[item] = start
#             dfs(item)



# N = int(input())
# nodes = dict()
# is_visited = [False for _ in range(N+1)]
# nodes = [list() for _ in range(N+1)]
# for i in range(N-1):
#     s, e = map(int,input().split())
#     nodes[s].append(e)
#     nodes[e].append(s)
# bfs(1)

# s 하고 e 가 있으면
# s 가 부모, e 가 자식
# nodes[e].append(s)

# 1. 양방향 연결이 되어있구나.
# -> 당연히 부모를 우리가 알 수 없음....

# 탐색 방법 중에 쓸 수 있는게....
# 1. bfs
# 2. dfs

# 전위 중위 순회를 사용을 해볼꺼야 -> 왜? -- 그냥 많이쓰니까

# left - right 라는 단어는 사실 이진트리에서 쓰는거임,,,,
# -- > 단어 선택이 잘못되 있는데,,

# 뭐냐면.. 뭔지는 잘 모르겠지만, 일단 다른 노드를 탐색 해야 되겠다. 
# -> 다른 노드를 탐색을 하려면 뭐가 필요할까요?
# = > 노드에 뭐가 들어가있는지를 알아야겠죠,
# def inorder(v):
#     if v :
        
#         inorder(v.left) # 죄측 탐색
#         print(v)        # 우리가 원하는 수식 짜주면 되는 부분
#         inorder(v.right)# 우측 탐색
N = int(input())
rlt = [list(map(int,input().split())) for i in range(N-1)]

nodes = [list() for o in range(N+1)]
for i in range(N-1):
    nodes[rlt[i][0]].append(rlt[i][1])
    nodes[rlt[i][1]].append(rlt[i][0])

is_traveled = [False for _ in range(N+1)]
ans = [0 for _ in range(N+1)]
def inorder(v):
    # if v= 1 일 겨우에는 -> 6번하고 4번이
    # if v= 6 일 경우에는 -> 1하고 3 // 아니? 1은 부모아니였어?
    for node in nodes[v]: # -> 모르겠으니까 for문을 돌린거야
        if is_traveled[node] == True:
            continue
        is_traveled[node] = True
        inorder(node) # -> 6번하고 4번 탐색 할 수 있겠찌
        # 우리가 원하는 수식 == 이친구의 부모 노드가 뭐야!!!
        # 이곳에서 우리는 알 수 있다!
        ans[node] = v

    
is_traveled[1] = True
inorder(1)
    
for idx in range(2,N+1):
    print(ans[idx])
# nodes = [[], [6,4],  [4], [6,5], [1,2,7], [3], [1,3], [4]]

# nodes[i][0] ==> 왜 안됬을까요? // 왜 테케는 맞았는데 틀렸다고 떴을까.
# Hint = 테케는 운이 좋았다.
# A. 들어오는 값 대로 리스트에 저장이 되잖아.

# n = sorted(list(parent.items()),key= lambda x: x[0])
# for key, value in n:
#     print(value)