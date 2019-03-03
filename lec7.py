game=[[0,0,0],
      [0,0,0],
      [0,0,0]]


def game_board(player=0,row=0,col=0,just_display=False):
    print("   a  b  c")
    if not just_display:
        game[row][col] = player
    for count, abc in enumerate(game):
        print(count, abc)



game_board(just_display=True)
game_board(2,2,2)





