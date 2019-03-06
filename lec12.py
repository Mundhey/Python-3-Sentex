game=[[8,4,1],
      [2,6,1],
      [2,4,1]]


diag_y=[]

for row,col in enumerate(reversed(range(len(game)))):
    diag_y.append(game[row][col])

diag_x=[]
for ix in range(len(game)):
    diag_x.append(game[ix][ix])
