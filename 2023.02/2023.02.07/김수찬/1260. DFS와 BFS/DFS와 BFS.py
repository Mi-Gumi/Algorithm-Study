from collections import deque

# T = int(input())

N,M,V = map(int,input().split())

net = dict()
for _ in range(M):
  s, e = map(int,input().split())
  if not net.get(s) or not net.get(e):
    net.setdefault(s, set())
    net.setdefault(e, set())
  net[s].add(e)
  net[e].add(s)
  
is_travel_dfs = [False for _ in range(N+1)]
is_travel_bfs = [False for _ in range(N+1)]


def dfs(n):

  print(n,end =' ')
  
  if net.get(n):
    connect = sorted(list(net[n]))
    for item in connect:
      if is_travel_dfs[item]: continue
      is_travel_dfs[item] = True
      dfs(item)

queue = deque()
def bfs(n):
  
  is_travel_bfs[n] = True
  
  
  queue.append(n)
  
  while queue:
    now = queue.popleft()
    print(now,end =' ')
    if net.get(now):
      now_lst = sorted(list(net[now]))
      for item in now_lst:
        if is_travel_bfs[item]:
          continue
        is_travel_bfs[item] = True
        queue.append(item)
        
  
  # if net.get(n):
  #   connect = sorted(list(net[n]))
  #   for item in connect:
  #     if is_travel_bfs[item]: continue
  #     is_travel_bfs[item] = True
  #     queue.append(item)
    
  #   try:
  #     bfs(queue.pop(0))
  #   except:
  #     return 

is_travel_dfs[V] = True
dfs(V)
print()
bfs(V)