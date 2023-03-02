size = input()
size = size.split()
M = int(size[0])
N = int(size[1])

line1 = ['W','B','W','B','W','B','W','B'] # 흰색줄로 시작
line2 = ['B','W','B','W','B','W','B','W'] # 검은색줄로 시작

chess1 = []
chess2 = []
for i in range(8):
    if(i%2 == 0):
        chess1.append(line1)
    else:
        chess1.append(line2)
for i in range(8):
    if(i%2 != 0):
        chess2.append(line1)
    else:
        chess2.append(line2) 
## 체스판 두개 제작

board = list()
for _ in range(M):
    line = input()
    line = list(line)
    board.append(line)
# 보드 제작


draw = [] # 색칠한 정도를 저장

for i in range(M - 7): # 8*8 칸으로 나눠서 체스판을 찾는다 생각함
    
    for j in range(N - 7): 
        
        draw1 = 0
        draw2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if(board[a][b] != chess1[i-a][j-b]): # 1번체스판과 다를경우
                    draw1 +=1
                    
                if(board[a][b] != chess2[i-a][j-b]): # 2번체스판과 다를경우
                    draw2 +=1
        
        draw.append(draw1)
        draw.append(draw2)

print(min(draw))