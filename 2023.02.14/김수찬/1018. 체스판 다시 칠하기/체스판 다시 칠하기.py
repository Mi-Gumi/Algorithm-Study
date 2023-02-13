size = input()
size = size.split()
M = int(size[0])
N = int(size[1])

line1 = ['W','B','W','B','W','B','W','B']
line2 = ['B','W','B','W','B','W','B','W']

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


board = list()
for _ in range(M):
    line = input()
    line = list(line)
    board.append(line)

draw = []


for i in range(M - 7): 
    
    for j in range(N - 7): 
        
        draw1 = 0
        draw2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if(board[a][b] != chess1[i-a][j-b]):
                    draw1 +=1
                    
                if(board[a][b] != chess2[i-a][j-b]):
                    draw2 +=1
        draw.append(draw1)
        draw.append(draw2)

print(min(draw))