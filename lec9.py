
game=[[0,0,0],
      [0,0,0],
      [0,0,0]]


def game_board(game_varible,player=0,row=0,col=0,just_print=False):

    try:

        print("  a   b   c")
        if not just_print:
            game_varible[row][col] = player

        for count, abc in enumerate(game):
            print(count, abc)

    except Exception as i:

        print("Something Wrong has happened",i)


game_board(game,1,5,1)
