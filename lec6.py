game=[[0,0,0],
      [0,0,0],
      [0,0,0]]


def game_board():
    print("   a  b  c")
    for count, abc in enumerate(game):
        print(count, abc)



game_board()

game[0][1]=1

game_board()




