
game=[[8,4,1],
      [2,6,1],
      [2,4,1]]




def winner(current_game):

    for col in range(len(current_game)):

        abc=[]

        for row in current_game:

            abc.append(row[col])

        if abc.count(abc[col]) == len(abc) and abc[col]!= 0:
            print("Winner")



winner(game)







'''



def game_board(game_varible,player=0,row=0,col=0,just_print=False):

    try:

        print("  a   b   c")
        if not just_print:
            game_varible[row][col] = player

        for count, abc in enumerate(game):
            print(count, abc)

    except Exception as i:

        print("Something Wrong has happened",i)




def winner(current_game):


    for row in current_game:

        if row.count(row[0])==len(row):

            print("Winner")





winner(game)






game_board(game,1,5,1)

'''